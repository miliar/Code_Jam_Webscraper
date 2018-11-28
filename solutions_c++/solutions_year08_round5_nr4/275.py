#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

string input = "D-small-attempt0.in", output = input + "___.out";
ifstream ifs(input.c_str());
ofstream ofs(output.c_str());

bool mp[128][128];
long long dp[128][128];
const long long MOD = 10007;

int main(void)
{
	int re;
	int w, h, n, r, c;

	ifs >> re;
	for (int ri = 1; ri <= re; ri++) {
		ifs >> h >> w >> n;
		for (int i = 1; i <= h; i++) {
			for (int j = 1; j <= w; j++) {
				mp[i][j] = false;
				dp[i][j] = 0;
			}
		}
		while (n--) {
			ifs >> r >> c;
			mp[r][c] = true;
		}
		dp[1][1] = 1;
		for (int i = 2; i <= h; i++) {
			for (int j = 2; j <= w; j++) {
				if (i > 2 && !mp[i - 2][j - 1]) {
					dp[i][j] += dp[i - 2][j - 1];
				}
				if (j > 2 && !mp[i - 1][j - 2]) {
					dp[i][j] += dp[i - 1][j - 2];
				}
				dp[i][j] %= MOD;
			}
		}
		// output
		cerr << ri << endl;
		ofs << "Case #" << ri <<": " << dp[h][w] << endl;
	}

	return 0;
}
