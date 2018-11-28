#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <map>
#include <complex>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <bitset>
#include <cassert>
using namespace std;

#define FOR(a,b,c) for(long long a=(long long)(b);a<(long long)(c);a++)
#define ITER(a,b) for(__typeof((b).begin()) a = (b).begin(); a!=(b).end(); a++)
#define SUBSET(a,b) for(long long a = 0; a!=0; a = (b & (a-1)))
#define MEMSET(dest,val) memset(dest,val,sizeof(dest))
#define PAIR pair<long long,long long>
#define BEGEND(a) (a).begin(), (a).end()
#define SHIFT(v) (1LL<<(v))
#define SQ(a) ((a) * (a))
#define LSB(a,b) (b<=sizeof(a)?(b & (SHIFT(a)-1)):LLMAX)

#define eps 1E-9
#define PI acos(-1.0)
#define INF 1000000000
#define LLINF ((1LL<<62)-1)


// ---------------------------------------------------------------------------------
//BEGIN CUT - Print Array - O(N)
void printArray(const vector<string> & v) { FOR(i,0,v.size()) cout << v[i] << endl; cout << endl; }
template<class T> 
void printArray(const vector<T> & v) { FOR(i,0,v.size()) cout << v[i] << " "; cout << endl; }
template <class T>
void printArray(const vector<vector<T> > &v){ FOR(i,0,v.size()) printArray(v[i]);}
//END CUT - Print Array


int dr4[] = {-1,0,0,1},           dc4[] = {0,-1,1,0};

//BEGIN CUT - Disjoint Set Forest - O(m*a(n))		NOTE: First Convert to indeces on the range (0.._MAX_DJSFSIZE]
#define _MAX_DJSFSIZE 10000
int _djsParent[_MAX_DJSFSIZE], _djsRank[_MAX_DJSFSIZE];
char djsChar[_MAX_DJSFSIZE];

void djs_init(){ MEMSET(_djsParent,-1); MEMSET(_djsRank,-1);}
bool djs_makeset(int pos){ if(pos < 0 || pos>=_MAX_DJSFSIZE || _djsParent[pos]!=-1) return false;_djsParent[pos]=pos; _djsRank[pos]=0; return true;}
int djs_findset(int pos){ if(_djsParent[pos]!=pos){ _djsParent[pos] = djs_findset(_djsParent[pos]);} return _djsParent[pos];}
bool djs_union(int posA, int posB){ int pA = djs_findset(posA), pB = djs_findset(posB); if(pA==pB) return false; if(_djsRank[pA]>_djsRank[pB]) _djsParent[pB] = pA; else if(_djsRank[pB]>_djsRank[pA]) _djsParent[pA]=pB; else _djsParent[pA]=pB, _djsRank[pA]++; return true;}
//END CUT - Disjoing Set Forest

int _T, H, W;
int alt[100][100];
bool sink[100][100];

bool valid(int i, int j){ return i>=0 && j>=0 && i<H && j<W;}
int main(){
  cin >> _T;
  FOR(_i,0,_T){
    cout << "Case #" << (_i+1) << ":" << endl;
    djs_init();
    cin >> H >> W; FOR(i,0,H) FOR(j,0,W) cin >> alt[i][j], djs_makeset(i*100+j);

//    FOR(ii,0,H) { FOR(jj,0,W) cout << alt[ii][jj] << " "; cout << endl;} cout << "--------" << endl;

    MEMSET(sink,false);

    FOR(i,0,H) FOR(j,0,W){
	int best = INF, bid = -1, cur;
	FOR(k,0,4) if(valid(i+dr4[k],j+dc4[k]) && (cur=alt[i+dr4[k]][j+dc4[k]]) < best){ best = cur, bid = k;}


        if(best < alt[i][j]) djs_union(i*100+j,(i+dr4[bid])*100+j+dc4[bid]);
	else sink[i][j] = true;
    }

//    FOR(ii,0,H) { FOR(jj,0,W) cout << djs_findset(ii*100+jj) << " "; cout << endl;} cout << "-----------" << endl;

    MEMSET(djsChar,-1);
    char ch = 'a'; FOR(i,0,H) FOR(j,0,W) if(djsChar[djs_findset(i*100+j)]==-1) djsChar[djs_findset(i*100+j)] = ch++;

    FOR(i,0,H){ 
	FOR(j,0,W) { if(j!=0) cout << " "; cout << djsChar[djs_findset(i*100+j)];}
	cout << endl;
    }
//    cout << "##################" << endl;
  }
  return 0;
}

