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

const double eps = 1e-9;
const int INF = 1000000010;
const long long LLINF = (long long)INF * INF;
const double PI = 2 * acos(.0);

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

const int MAXN = 128;
const int MAXLEN = MAXN * 10000;
int a[MAXN];
int dp[MAXLEN];

int main() {
	freopen("b-small-attempt0.in","r",stdin);
	freopen("b-small-attempt0.out","w",stdout);
	int T, ca, n, i, j;
	LL L;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ++ca) {
		scanf("%I64d%d",&L,&n);
		for (i = 0 ; i < n ; i++)
			scanf("%d",&a[i]);
		CLEAR(dp, 0x3f);
		dp[0] = 0;
		for (i = 0 ; i < MAXLEN ; i++) {
			if (dp[i] >= INF) continue;
			for (j = 0 ; j < n ; j++) {
				if (i + a[j] >= MAXLEN) continue;
				if (dp[i+a[j]] > dp[i] + 1)
					dp[i+a[j]] = dp[i] + 1;
			}
		}
		//printf("%d\n",dp[301]);
		LL ans = LLINF;
		for (i = 0 ; i < MAXLEN ; i++) {
			if (dp[i] >= INF) continue;
			for (j = 0 ; j < n ; j++)
				if ((L - i) % a[j] == 0)
					ans <?= (LL)dp[i] + (L-i) / a[j];
		}
		printf("Case #%d: ",ca);
		if (ans >= LLINF) printf("IMPOSSIBLE\n");
		else printf("%I64d\n",ans);
	}
	return 0;
}
/*
2
10000000001 3
23 51 100
10000000001 3
100 52 22
*/
