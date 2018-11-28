#include <stdio.h>
#include <string.h>

int n, sn, qn;
char s[105][105], q[1005][105];
int dp[105][1005];
         
void input ()
{
	scanf ("%d", &sn); getchar ();
	for (int i = 0; i < sn; i++) gets (s[i]);
	scanf ("%d", &qn); getchar ();
	for (int i = 0; i < qn; i++) gets (q[i]);
}

void solve ()
{
	int i, j;
	for (i = 0; i < sn; i++){
		if (!strcmp (s[i], q[0])) dp[i][0] = -1;
		else dp[i][0] = 0;
	}
	for (j = 1; j < qn; j++){
		for (i = 0; i < sn; i++){
			if (!strcmp (s[i], q[j])) dp[i][j] = -1;
			else {
				dp[i][j] = 10005;
				for (int k = 0; k < sn; k++)
					if (k == i) {
						if (dp[k][j-1] != -1 && dp[k][j-1] < dp[i][j]) dp[i][j] = dp[k][j-1];
					}
					else {
						if (dp[k][j-1] != -1 && dp[k][j-1] + 1 < dp[i][j]) dp[i][j] = dp[k][j-1] + 1;
					}
			}
		}
	}
}
void output (int x)
{
	int min = 1005;
	for (int i = 0; i < sn; i++) {
		if (dp[i][qn-1] != -1 && dp[i][qn-1] < min)
			min = dp[i][qn-1];
	}
	printf ("Case #%d: %d\n", x, min);
}
int main ()
{
	int cases;
	scanf ("%d", &cases);
	for (int i = 1; i <= cases; i++) {
		input ();
		solve ();
		output (i);
	}
}