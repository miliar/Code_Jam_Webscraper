#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))
#define maxn 10005
#define inf 1000000

using namespace std;

int m, v, a, b;
int t[maxn], can[maxn], value[maxn];
int dp[maxn][2];

void solvecase() {
	scanf("%d%d", &m, &v);
	a = (m-1)/2;
	for (int i = 1; i <= a; i++) {
		scanf("%d%d", &t[i], &can[i]);
	}
	for (int i = a+1; i <= m; i++) { 
		scanf("%d", &value[i]);
		dp[i][value[i]] = 0;
		dp[i][1-value[i]] = inf;
	}
	for (int i = a; i >= 1; i--) FOR(j, 2) {
		dp[i][j] = inf;
		// or
		int cost;
		if (t[i] == 0) cost = 0;
		else if (can[i]) cost = 1;
		else cost = inf;		
		FOR(x1, 2) FOR(x2, 2) if ((x1 | x2) == j) dp[i][j] = min(dp[i][j], dp[2*i][x1] + dp[2*i+1][x2] + cost);
		// and
		if (t[i] == 1) cost = 0;
		else if (can[i]) cost = 1;
		else cost = inf;		
		FOR(x1, 2) FOR(x2, 2) if ((x1 & x2) == j) dp[i][j] = min(dp[i][j], dp[2*i][x1] + dp[2*i+1][x2] + cost);		
	}
	if (dp[1][v] == inf) printf("IMPOSSIBLE"); else printf("%d", dp[1][v]);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("y", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}