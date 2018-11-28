#include <cstdio>
#define Max 0x3fffffff
int n, v;
int a[10010], c[10010], dp[10010][2];
int min (int x, int y) {return x < y ? x : y;}
int main ()
{
//	freopen ("A-large.in", "r", stdin);
//	freopen ("out.txt", "w", stdout);
	int cases = 0, l, r, i;
	scanf ("%d", &cases);
	for (int k = 1; k <= cases; k++){
		scanf ("%d%d", &n, &v);
		int pos = (n-1) / 2;
		for (i = 1; i <= pos; i++){
			scanf ("%d%d", &a[i], &c[i]);
			dp[i][0] = dp[i][1] = Max;
		}
		for (i = pos+1; i <= n; i++){
			scanf ("%d", &a[i]);
			dp[i][a[i]] = 0;
			dp[i][a[i]^1] = Max;
		}
		for (i = pos; i >= 1; i--){
			l = 2 * i , r = l + 1;
			if (a[i] == 1){
				dp[i][1] = min (dp[i][1], dp[l][1]+dp[r][1]);
				dp[i][0] = min (dp[i][0], dp[l][1]+dp[r][0]);
				dp[i][0] = min (dp[i][0], dp[l][0]+dp[r][1]);
				dp[i][0] = min (dp[i][0], dp[l][0]+dp[r][0]);
			}
			else {
				dp[i][1] = min (dp[i][1], dp[l][1]+dp[r][0]);
				dp[i][1] = min (dp[i][1], dp[l][0]+dp[r][1]);
				dp[i][1] = min (dp[i][1], dp[l][1]+dp[r][1]);
				dp[i][0] = min (dp[i][0], dp[l][0]+dp[r][0]);
			}
			if (c[i] == 1){
				if (a[i] == 1){
					dp[i][1] = min (dp[i][1], dp[l][1]+dp[r][0]+1);
					dp[i][1] = min (dp[i][1], dp[l][0]+dp[r][1]+1);
					dp[i][1] = min (dp[i][1], dp[l][1]+dp[r][1]+1);
					dp[i][0] = min (dp[i][0], dp[l][0]+dp[r][0]+1);					
				}
				else{
					dp[i][1] = min (dp[i][1], dp[l][1]+dp[r][1]+1);
					dp[i][0] = min (dp[i][0], dp[l][1]+dp[r][0]+1);
					dp[i][0] = min (dp[i][0], dp[l][0]+dp[r][1]+1);
					dp[i][0] = min (dp[i][0], dp[l][0]+dp[r][0]+1);
					
				}
			}
		}
		if (dp[1][v] == Max) printf ("Case #%d: IMPOSSIBLE\n", k);
		else printf ("Case #%d: %d\n", k, dp[1][v]);
	}
}
