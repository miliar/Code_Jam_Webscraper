#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define RESET(a,c) memset(a,(c),sizeof(a))


/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

const int MAX = 20000;
int gate[MAX], chg[MAX], leaf[MAX];
int t[MAX][2], cost[MAX][2];

void solve(void)
{
	int N, V;
	scanf("%d %d", &N, &V);
	int inter = (N-1)/2;
	FOR(i,1, inter) 
		scanf("%d %d",&gate[i], &chg[i]);
	
	FOR(i,inter+1, N) scanf("%d", &leaf[i]);
	
	RESET(t, 0);

	FOR(i,1, N) cost[i][0] = cost[i][1] = INF;

	FOR(i, inter+1, N) { t[i][ leaf[i] ] = 1; cost[i][leaf[i]] = 0; }

	FORD(i, inter, 1) {
		
		int x = i*2, y = i*2+1;
		
		if(gate[i] == 1 || chg[i]) {//bramka and 
		  	cost[i][1] = min(cost[i][1], cost[x][1] + cost[y][1] + (gate[i] != 1)); 
			cost[i][0] = min(cost[i][0], min( cost[x][0] + min(cost[y][0], cost[y][1]), cost[y][0] + min(cost[x][0], cost[x][1]))+(gate[i] != 1) );
		}
		if(gate[i] == 0 || chg[i]) { //bramka or
			cost[i][1] = min(cost[i][1],  min( cost[x][1] + min(cost[y][0], cost[y][1]), cost[y][1] + min(cost[x][0], cost[x][1]))+(gate[i]!=0)); 
			cost[i][0] = min(cost[i][0], cost[x][0] + cost[y][0] + (gate[i] != 0)); 
		}
	}

	if(cost[1][V] < INF) printf("%d\n", cost[1][V]);
	else printf("IMPOSSIBLE\n");
}

int main(void)
{
	int T, C = 1;
	scanf("%d", &T);
	while(T--) { printf("Case #%d: ",C++); solve(); }
	return (0);
}
