#include <cstdio>
#include <cstdlib>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 64

int n;
unsigned long long res, dp[MAXN][2][3][5][7];
char inp[MAXN];
bool vis[MAXN][2][3][5][7];

void init() {
    res = 0;
    scanf("%s", &inp);
    n = strlen(inp);
    memset(vis, 0, sizeof(vis));
    memset(dp, 0, sizeof(dp));
}

unsigned long long calc_dp(int i, int m2, int m3, int m5, int m7) {
    if(i == n) {
        return (m2==0 || m3==0 || m5==0 || m7==0) ? 1 : 0;
    }
    if(vis[i][m2][m3][m5][m7]) return dp[i][m2][m3][m5][m7];
    vis[i][m2][m3][m5][m7] = 1;

    int s2=0, s3=0, s5=0, s7=0;
    for(int j=i; j<n;++j) {
        s2 = (s2*10 + inp[j] - '0')%2;
        s3 = (s3*10 + inp[j] - '0')%3;
        s5 = (s5*10 + inp[j] - '0')%5;
        s7 = (s7*10 + inp[j] - '0')%7;
        dp[i][m2][m3][m5][m7] += calc_dp(j + 1, (m2+s2)%2, (m3+s3)%3, (m5+s5)%5, (m7+s7)%7);
        if(i > 0) {
            dp[i][m2][m3][m5][m7] += calc_dp(j + 1, (m2-s2+2)%2, (m3-s3+3)%3, (m5-s5+5)%5, (m7-s7+7)%7);
        }
    }
    return dp[i][m2][m3][m5][m7];
}

void solve() {
    calc_dp(0, 0, 0, 0, 0);
}

int main(void) {
	int n;

	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);

	cin >> n;
	for(int i=1; i<=n; ++i) {
		init();
		solve();
		cout << "Case #" << i << ": " << dp[0][0][0][0][0] << endl;
	}
	return 0;
}
