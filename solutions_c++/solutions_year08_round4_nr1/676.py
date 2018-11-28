#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>


const long double eps = 1e-9;

using namespace std;

namespace TTT{


int m, V;

int tp[11111];
int change[11111];

void Load()
{
	cin >> m >> V;
	int i;
	int j, k;
	for (i = 1; i <= m; i++) {
		if ((i<<1) <= m) {
			scanf("%d%d", &j, &k);
			change[i] = k;
			tp[i] = j;
		} else scanf("%d", &tp[i]);
	}
}


int dp[11111][2];
void Solve()
{
	memset(dp, -1, sizeof(dp));
	int i, k;
	int j;
	int tres, tval;
	for (i = m; 2 * i > m; i--) dp[i][tp[i]] = 0;
	for (i = m / 2; i >= 1; i--) {
		for (j = 0; j <= 1; j++) {
			for (k = 0; k <= 1; k++) {
				if (dp[i * 2][j] == -1) continue;
				if (dp[i * 2 + 1][k] == -1) continue;
				tres = dp[i * 2][j] + dp[i * 2 + 1][k];
				if (tp[i] == 1) {
					tval = j & k;
					if (dp[i][tval] == -1 || dp[i][tval] > tres) dp[i][tval] = tres;
					if (change[i]) {
						tval = j | k;
						if (dp[i][tval] == -1 || dp[i][tval] > tres + 1) dp[i][tval] = tres + 1;
					}
				}
				if (tp[i] == 0) {
					tval = j | k;
					if (dp[i][tval] == -1 || dp[i][tval] > tres) dp[i][tval] = tres;
					if (change[i]) {
						tval = j & k;
						if (dp[i][tval] == -1 || dp[i][tval] > tres + 1) dp[i][tval] = tres + 1;
    				}
				}

			}

		}
	}
	if (dp[1][V] == -1) {
		cout << "IMPOSSIBLE\n";
	} else cout << dp[1][V] << "\n";

}

void Save()
{
}
}
using namespace TTT;

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve();
		Save();
	}
	return 0;
}