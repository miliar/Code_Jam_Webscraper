#include <stdio.h>
#include <algorithm>

#define INF 0x7f7f7f7f

using namespace std;

struct Swing
{
	int d, l;
} sw[60010];

int n, D;

bool cmp(const Swing &A, const Swing &B)
{
	return A.d < B.d;
}

int dp[60010];

bool search()
{
	int i, j, dis;

	for (i = n - 1; i >= 0; i--) {
		dp[i] = INF;

		for (j = i + 1; j < n; j++) {
			if (sw[j].d > sw[i].d + sw[i].l) break;

			dis = min(sw[j].d - sw[i].d, sw[j].l);
			if (dis >= dp[j]) {
				dp[i] = sw[j].d - sw[i].d;
				break;
			}
		}
		if (sw[i].d + sw[i].l >= D) 
			dp[i] = min(dp[i], D - sw[i].d);
	}

	return sw[0].d >= dp[0];
}

int main()
{
	int T, t, i;

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%d%d", &sw[i].d, &sw[i].l);
		}
		scanf("%d", &D);
		sort(sw, sw + n, cmp);
		
		printf("Case #%d: ", t);
		if (search()) {
			printf("YES\n");
		}
		else printf("NO\n");
	}
	return 0;
}
