#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;

#define LET(x,a) 	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)  	for(int i=(int)(a) ; i < (int)(b);++i)
#define REP(i,n) 	FOR(i,0,n)
#define PB		push_back
#define MP 		make_pair
#define EPS		1e-9
#define INF 2000000000

typedef vector<int>	VI;
typedef long long	LL;
typedef pair<int,int>	PI;
int main() {
	int t;
	scanf("%d",&t);
	for (int kases = 1; kases <= t; ++ kases) { 
		cout << "Case #"<<kases <<": ";
		int n,k;
		cin >> n >> k;
		int mat[200][50];
		REP(i,n) {
			REP(j,k) {
				cin >> mat[i][j];
			}
		}
		int deg[200] = {};
		vector<int> graph[200];
		REP(i,n) {
			FOR(j,i+1,n) {
				if ( i == j) continue;
				int sign = 1;
				int solve = 0;
				if ( mat[i][0] < mat[j][0]) sign = -1;
				REP(l, k) {
					if (mat[i][l] == mat[j][l]) {
						solve = 1;
						break;
					}
					if (mat[i][l] < mat[j][l] && sign == 1) {
						solve = 1;
						break;
					}
					if (mat[i][l] > mat[j][l] && sign == -1) {
						solve = 1;
						break;
					}
				}
				if (solve) {
					graph[i].push_back(j);
					graph[j].push_back(i);
					deg[i]++;
					deg[j]++;
				}
			}
		}
	/*	REP(i,n) {
			cout << deg[i] << " ";
			REP(j,graph[i].size()) cout << graph[i][j] << " " ;
			cout << endl;
		}*/
		vector<pair<int,int> > dag;
		REP(i,n) dag.push_back(make_pair(deg[i],i)),assert(deg[i] == graph[i].size());
	
		sort(dag.begin(),dag.end());
		reverse(dag.begin(),dag.end());
		int color[500];
		memset(color,-1,sizeof(color));
		int ans = 0;
		REP(i,n) {
			int v = dag[i].second;
			int ar[200] = {};
			int sz = graph[v].size();
			REP(j,sz) {
				int v2 = graph[v][j];
				if(color[graph[v][j]] != -1) {
					ar[color[graph[v][j]]] = 1;
				}
			}
			REP(j,n+1)if(!ar[j]) {
				color[v] = j;
				ans = max(ans,j);
				break;
			}
		}
		cout << ans + 1<< endl;
	}
return 0;
}

