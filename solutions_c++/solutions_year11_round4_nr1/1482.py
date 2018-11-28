#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <limits>

#define px first
#define py second
#define mp make_pair
#define pb push_back

using namespace std;

const int INF = numeric_limits<int>::max();

int caseNum;
double x, s, r, t, n;
vector<double> speed;

void solve()
{
	speed.assign(101, 0);
	cin >> x >> s >> r >> t >> n;
	speed[0] = x;
	for (int i = 0; i < n; ++i) {
		int a, b, v;
		cin >> a >> b >> v;
		speed[0] -= double(b - a);
		speed[v] += double(b - a);
	}
	double ans = 0;
	for (int i = 0; i < 101; ++i) {
		if (t > 0) {
			double u = speed[i] / (i + r);
			if (u > t) {
				u = t + (speed[i] - t * (i + r)) / (i + s);
			}
			ans += u;
			t -= u;
		} else {
			ans += speed[i] / (i + s);
		}
	}
	cout << setprecision(8) << fixed << ans << endl;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d\n", &caseNum);
	for (int i = 0; i < caseNum; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}