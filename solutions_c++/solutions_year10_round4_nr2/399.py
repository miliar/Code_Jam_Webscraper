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
#include <string.h>
using namespace std;

#define FOR(a,b,c) for(long long a=(long long)(b);a<(long long)(c);a++)
#define ITER(a,b) for(__typeof((b).begin()) a = (b).begin(); a!=(b).end(); a++)
#define SUBSET(a,b) for(long long a = b; a!=0; a = (b & (a-1)))
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

long long dp[12][12][SHIFT(10)+5];
long long values[12][SHIFT(10)+5];

int _T;
int P;

long long solve(int skipped, int row, int col){
   long long &ret = dp[skipped][row][col]; if(ret != -1) return ret; 
//   cout << "SOLVE: " << skipped << " " << row << " " << col << " " << values[row][col] << endl;
   if(row == 0) ret = (skipped > values[row][col])?INF:0;
   else         ret = min(values[row][col] + solve(skipped,row-1,col*2) + solve(skipped,row-1,col*2+1),
	              solve(skipped+1,row-1,col*2) + solve(skipped+1,row-1,col*2+1));
//   cout << "SOLVE: " << skipped << " " << row << " " << col << " " << values[row][col] << " -> " << ret << endl;
   ret = min(ret,(long long)INF);
   return ret;
}

int main(){
  cin >> _T;
  FOR(i,0,_T){
    MEMSET(dp,-1);
    cout << "Case #" << (i+1) << ": ";
    cin >> P;

    FOR(j,0,SHIFT(P)) cin >> values[0][j];
    FOR(j,0,P) FOR(k,0,SHIFT(P-j-1)) cin >> values[j+1][k];

    cout << solve(0,P,0);
    cout << endl;
  }
  return 0;
}

