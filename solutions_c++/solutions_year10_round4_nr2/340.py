#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define CLEAR(a,v) memset((a), (v), sizeof(a))
#define POW2(x) (1<<(x))

const double eps = 1e-9;
const int INF = 500000010;
const long long LLINF = (long long)INF * INF;
const double PI = 2 * acos(.0);

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

const int MAXN = 1030;
int a[MAXN];
int cost[12][MAXN];
int vis[12][MAXN][12];
int dp[12][MAXN][12];

int solve(int round, int idx, int hav) {
	if (vis[round][idx][hav]) {
		return dp[round][idx][hav];
	}
	if (round == 0) {
		if (hav >= a[idx]) return 0;
		return INF;
	}
	int tmp = INF;
	tmp <?= solve(round-1, idx*2, hav) + solve(round-1, idx*2+1, hav);
	tmp <?= cost[round][idx] + solve(round-1, idx*2, hav+1) + solve(round-1, idx*2+1, hav+1);
	vis[round][idx][hav] = 1;
	//printf("dp[%d][%d][%d] = %d\n",round,idx,hav,tmp);
	return dp[round][idx][hav] = tmp;
}

int main() {
	//freopen("b-small-attempt0.in","r",stdin);
	//freopen("b-small-attempt0.out","w",stdout);
	freopen("b-large.in","r",stdin);
	freopen("b-large.out","w",stdout);
	int T, ca, i, j, P;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++) {
		scanf("%d",&P);
		for (i = 0 ; i < POW2(P) ; i++) {
			scanf("%d",&a[i]);
			a[i] = P - a[i];
		}
		CLEAR(vis, 0);
		CLEAR(dp, 0);
		for (i = 1 ; i <= P ; i++)
			for (j = 0 ; j < POW2(P-i) ; j++)
				scanf("%d",&cost[i][j]);
		/*
		int ans = 0;
		for (i = 0 ; i < POW2(P) ; i++) {
			int tmp = i;
			for (j = 0 ; j < P - a[i] ; j++) {
				printf("idx:%d need:%d\n",i,cost[j][tmp/2]);
				if (mp[j][tmp/2] == 0) {
					mp[j][tmp/2] = 1;
					ans += cost[j][tmp/2];
				}
				tmp /= 2;
			}
		}
		*/
		int ans = solve(P, 0, 0);
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
/*
2
2
1 1 0 1
1 1
1
3
1 2 3 2 1 0 1 3
100 150 50 90
500 400
800
*/
