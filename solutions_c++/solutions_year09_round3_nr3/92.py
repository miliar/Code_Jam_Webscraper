#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <fstream>
using namespace std;

#ifdef WIN32
//ifstream in("c.in");
//ifstream in("C-small.in");
ifstream in("C-large.in");
#define cin in
//ofstream out("C-small.out");
ofstream out("C-large.out");
#define cout out
#endif

int t, ca = 0, m, n;
int dp[110][110];

int func(int left, int right, vector<int>& a)
{
	if (dp[left][right] >= 0) return dp[left][right];

	if (left > right) {
		return 0;
	}

	int min = -1;
	for (int i = left; i <= right; ++i) {
		int l = a[i] - a[left - 1] - 1;
		int r = a[right + 1] - a[i] - 1;
		int ll = func(left, i - 1, a);
		int rr = func(i + 1, right, a);
		int res = l + r + ll + rr;
		if (min < 0 || min > res) min = res;
	}

	return dp[left][right] = min;
}

int main()
{
	int t, ca = 0, m, n;
	for (cin >> t; t; --t) {
		cin >> n >> m;
		vector<int> a(m + 2);
		for (int i = 1; i <= m; ++i) {
			cin >> a[i];
		}
		a[0] = 0; a[m + 1] = n + 1;

		int min = -1;
		memset(dp, -1, sizeof(dp));

		cout << "Case #" << ++ca << ": " << func(1, m, a) << endl;
	}

	return 0;
}
