#include <cstdio>
#include <sstream>
#include <memory.h>
#include <iostream>
using namespace std;

const int MAX_N = 128;
const int MAX_COORD = 100;

int n;
char who[MAX_N]; // who must press i-th button
int where[MAX_N]; // where is the i-th button
int prev[MAX_N]; // where was the previous button of who[i]

int dp[MAX_N][MAX_COORD+1][MAX_COORD+1]; // dp[buttons_pressed][O_pos][B_pos] -> time
int ans;

int abs(int a) { return a<0?-a:a; }
void optimize(int &dp, int val) { if (dp > val) dp = val; }

void input()
{
	char s[MAX_N*10];
	int i, j;
	
	scanf("%d %[^\n]", &n, s);

	istringstream in(s);
	for(i=1; i<=n; i++) {
		in >> who[i] >> where[i];
		
		prev[i] = 0;
		for (j=i-1; j>=1; j--)
			if (who[j] == who[i]) {
				prev[i] = where[j];
				break;
			}
	}
}

void solve()
{
	int t, pr, from, to, i, j;

	memset(dp,0x77,sizeof(dp));
	dp[0][1][1] = 0;

	for(t=1; t<=n; t++)
		for(pr=1; pr<=MAX_COORD; pr++)
			for(from=1; from<=MAX_COORD; from++)
				for(to=1; to<=MAX_COORD; to++) {
					if(who[t]=='O') { // orange
						//optimize( dp[t][ where[t] ][to], dp[t-1][ prev[t] ][from] + max(abs(prev[t]-where[t]) + 1, abs(from-to)) );
						optimize( dp[t][ where[t] ][to], dp[t-1][ pr ][from] + max(abs(pr-where[t]) + 1, abs(from-to)) );

						//printf ("dp[%d][%d][%d]=%d -> dp[%d][%d][%d]=%d\n", t-1, prev[t], from, dp[t-1][ prev[t] ][from], t, where[t], to, dp[t][ where[t] ][to]);
					}
					else { // blue
						//if ( dp[t-1][from][ pr ] + max(abs(pr-where[t]) + 1, abs(from-to)) == 53 )
						//	if (dp[t][to][ where[t] ] > dp[t-1][from][ pr ] + max(abs(pr-where[t]) + 1, abs(from-to)))
						//		printf ("dp[%d][%d][%d]=%d -> dp[%d][%d][%d]=%d\n", t-1, from, pr, dp[t-1][from][ pr ], t, to, where[t], dp[t-1][from][ pr ] + max(abs(pr-where[t]) + 1, abs(from-to)));

						optimize( dp[t][to][ where[t] ], dp[t-1][from][ pr ] + max(abs(pr-where[t]) + 1, abs(from-to)) );
						//optimize( dp[t][to][ where[t] ], dp[t-1][from][ prev[t] ] + max(abs(prev[t]-where[t]) + 1, abs(from-to)) );
						//printf ("dp[%d][%d][%d]=%d -> dp[%d][%d][%d]=%d\n", t-1, from, pr, dp[t-1][from][ pr ], t, to, where[t], dp[t][to][ where[t] ]);
					}

				}

	ans = dp[0][0][0]; // inf
	for(i=1; i<=MAX_COORD; i++)
		for(j=1; j<=MAX_COORD; j++) {
			//if (dp[n][i][j] < ans) printf ("opt: dp[%d][%d][%d]=%d\n", n, i, j, dp[n][i][j]);
			optimize(ans, dp[n][i][j]);
			
		}
}

void output(int t)
{
	printf("Case #%d: %d\n", t, ans);
}

int main()
{
	int i, t;
	scanf ("%d", &t);

	for (i=1; i<=t; i++) {
		input();
		solve();
		output(i);
	}
	
	return 0;
}