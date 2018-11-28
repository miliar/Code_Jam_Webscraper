#include<stdio.h>
#include<string.h>
#include<algorithm>

#define INF 0x7f7f7f7f

using namespace std;

struct swinging{int d, l;} sw[60010];

int n, D;
int dp[60010];

bool cmp(const swinging &A, const swinging &B){ return A.d < B.d; }


//swinging
bool mysearch()
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

//main
int main()
{
	int T, t, i;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t++) 
	{
		//input
		scanf("%d", &n);
		for (i = 0; i < n; i++) 
			scanf("%d%d", &sw[i].d, &sw[i].l);
		scanf("%d", &D);
		//sort
		sort(sw, sw + n, cmp);
		printf("Case #%d: ", t);
		if (mysearch())  printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
