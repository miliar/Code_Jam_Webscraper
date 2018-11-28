#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <algorithm>
#include <functional>

using namespace std;

string input = "A-large.in", output = input + "___.out";
ifstream ifs(input.c_str());
ofstream ofs(output.c_str());

const int inf = 1 << 20;

int a[10001], c[10001], dp[10001];

#define left(x) (2 * x + 1)
#define right(x) (2 * x + 2)

int dp0(int x)
{
	int& ret = dp[x];

	if (ret != -1) {
		return ret;
	}
	ret = inf;
	if (a[x] == 1) {
		ret = min(ret, min(dp0(left(x)), dp0(right(x))));
	}
	else {
		ret = min(ret, dp0(left(x)) + dp0(right(x)));
		if (c[x] == 1) {
			ret = min(ret, 1 + min(dp0(left(x)), dp0(right(x))));
		}
	}

	return ret;
}

int dp1(int x)
{
	int& ret = dp[x];

	if (ret != -1) {
		return ret;
	}
	ret = inf;
	if (a[x] == 0) {
		ret = min(ret, min(dp1(left(x)), dp1(right(x))));
	}
	else {
		ret = min(ret, dp1(left(x)) + dp1(right(x)));
		if (c[x] == 1) {
			ret = min(ret, 1 + min(dp1(left(x)), dp1(right(x))));
		}
	}

	return ret;
}

int main(void)
{
	int re;
	int m, v;
	int ans;

	ifs >> re;
	for (int ri = 1; ri <= re; ri++) {
		ifs >> m >> v;
		for (int i = 0; i < (m - 1) / 2; i++) {
			ifs >> a[i] >> c[i];
			dp[i] = -1;
		}
		for (int i = (m - 1) / 2; i < m; i++) {
			ifs >> a[i];
			dp[i] = (a[i] == v) ? 0 : inf;
		}
		// output
		ans = (v == 0 ? dp0(0) : dp1(0));
		ofs << "Case #" << ri << ": ";
		if (ans == inf) {
			ofs << "IMPOSSIBLE";
		}
		else {
			ofs << ans;
		}
		ofs << endl;
	}

	return 0;
}
