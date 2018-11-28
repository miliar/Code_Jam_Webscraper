#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x,b,e) for (int x = (b); x < (e); ++x)
#define FORD(x,b,e) for (int x = (b); x >= (e); --x)
#define REP(x,n) for (int x = 0; x < (n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) c.begin(), c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for (VAR(i,c.begin()); i != c.end(); ++i)
#define PB push_back
#define ST first
#define ND second
const int MAXM = 10000;
const int MAXT = 2*MAXM-1;
const int INF = 1000000000;
int t[MAXT][2];

int g[MAXM], c[MAXM];
int main() {
	int z;
	scanf("%d",&z);
	FOR(a,1,z+1) {
		int m, v;
		scanf("%d%d",&m,&v);
		REP(i,m/2) { scanf("%d%d",&g[i],&c[i]); }
		REP(i,m) REP(j,2) t[i][j] = INF;
		FOR(i,m/2,m) { int lv; scanf("%d",&lv); t[i][lv] = 0; }
		FORD(i,m/2-1,0) {
				if (g[i] == 1) { 
					t[i][1] = min(t[2*i+1][1] + t[2*i+2][1],INF);
					t[i][0] = min(t[2*i+1][0],t[2*i+2][0]);
				}
				else {
					t[i][1] = min(t[2*i+1][1], t[2*i+2][1]);
					t[i][0] = min(t[2*i+1][0] + t[2*i+2][0],INF);
				}
			if (c[i] == 1) {
				if (g[i] == 0) { 
					t[i][1] = min(t[i][1],min(t[2*i+1][1] + t[2*i+2][1],INF)+1);
					t[i][0] = min(t[i][0],min(t[2*i+1][0],t[2*i+2][0])+1);
				}
				else {
					t[i][1] = min(t[i][1],min(t[2*i+1][1], t[2*i+2][1])+1);
					t[i][0] = min(t[i][0],min(t[2*i+1][0] + t[2*i+2][0],INF)+1);
				}
			}
		}
		if (t[0][v] != INF)
			printf("Case #%d: %d\n",a,t[0][v]);
		else
			printf("Case #%d: IMPOSSIBLE\n",a);
	}
	return 0;
}
