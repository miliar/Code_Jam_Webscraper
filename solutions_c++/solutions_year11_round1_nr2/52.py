#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

char inp[120000][15];
char alp[30];

map<string,int> cost;
map<string,int> to[1200000];
int U=1200000;
void dfs(int n, int co){
	if(to[n].empty())return;
	char cc = (to[n].begin()->first)[0];
	FORIT(it,to[n]){
		int tt = it->second;
		if((it->first)[0]!=cc){
			co++;
			cc = (it->first)[0];
		}
		if(to[tt].empty()){
			cost[(it->first).substr(1)]=co;
		} else {
			dfs(tt,co);
		}
	}
}
int main(){
	int tc;
	scanf("%d",&tc);
	FOR(tcc,1,tc+1){
		cout <<"Case #"<<tcc<<":";
		int N,M;
		scanf("%d%d",&N,&M);
		FOR(i,0,N)scanf("%s",inp[i]);
		FOR(al,0,M){
			scanf("%s",alp);
			FOR(i,0,U)to[i].clear();
			U = 10;
			FOR(i,0,N){
				string cur(inp[i]);
				int L = sz(cur);
				FOR(j,0,L)cur[j]='a'-1;
				int n = sz(cur)-1;
				cur+=(char)('a'-1);
				FOR(l,0,26){
					bool ch = false;
					FOR(j,0,L){
						if(inp[i][j]==alp[l]){
							ch = true;
							cur[j+1]=alp[l];
						}
					}
					if(ch){
						cur[0]=(char)l;
						if(to[n].find(cur)==to[n].end())to[n][cur]=U++;
						n = to[n][cur];
					}
				}
			}
			cost.clear();
			FOR(i,0,10)dfs(i,0);
			string word = "";
			int res = -1;
			FOR(i,0,N){
				string cur(inp[i]);
				int nc = cost[cur];
				if(nc>res){
					res = nc;
					word = cur;
				}
			}
			cout << " "<< word;
		}
		cout << endl;
	}
	return 0;
}
