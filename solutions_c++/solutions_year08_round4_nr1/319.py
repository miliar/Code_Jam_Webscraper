#include <cstdio>
#include <cstdlib>
#define INF 500000

int type[10010], gate[10010], ch[10010], val[10010];
int dp[10010][3];

int min(int a, int b) { return (a < b ? a : b); }

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, a, b, c, d, A, B, M, V, T, test;
	
	scanf("%d", &T);
	
	for (test=1; test<=T; test++) {
		scanf("%d %d", &M, &V);
		A = (M-1)/2;
		B = (M+1)/2;
		
		if ( A + B != M ) {
			printf("Err\n");
			
			return 0;
		}
		
		for (i=1; i<=A; i++) {
			scanf("%d %d", &gate[i], &ch[i]);
			type[i] = 0;
		}
		
		for (i=1; i<=B; i++) {
			scanf("%d", &val[A+i]);
			type[A+i] = 1;
		}
		
		for (i=M; i>=1; i--) {
			if ( type[i] == 1 ) {
				dp[i][0] = (val[i] == 0 ? 0 : INF);
				dp[i][1] = (val[i] == 1 ? 0 : INF);
				dp[i][2] = 0;
			}
			else {
				a = b = c = d = INF;
				
				if ( ch[i] || gate[i] == 1 ) {
					a = dp[i*2][1] + dp[i*2+1][1];
					b = min(dp[i*2][2] + dp[i*2+1][0], dp[i*2][0] + dp[i*2+1][2]);
					
					if ( gate[i] != 1 ) {
						a++;
						b++;
					}
				}
				if ( ch[i] || gate[i] == 0 ) {
					c = min(dp[i*2][2] + dp[i*2+1][1], dp[i*2][1] + dp[i*2+1][2]);
					d = dp[i*2][0] + dp[i*2+1][0];
					
					if ( gate[i] != 0 ) {
						c++;
						d++;
					}
				}
				
				dp[i][0] = min(b, d);
				dp[i][1] = min(a, c);
				
				if ( dp[i][0] > INF ) dp[i][0] = INF;
				if ( dp[i][1] > INF ) dp[i][1] = INF;
			}			
		}
		
		printf("Case #%d: ", test);
		
		if ( dp[1][V] >= INF ) {
			printf("IMPOSSIBLE\n");
		}
		else {
			printf("%d\n", dp[1][V]);
		}
	}
	
	return 0;
}
