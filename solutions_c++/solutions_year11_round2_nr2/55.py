#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

vector<pair<int, int> > vp;
int n, d;

bool isok(long long t)
{
	long long curlim = -1000000000000000LL;
	for (int i = 0; i < n; ++i) {
		long long left = vp[i].first - t;
		left = max(left, curlim);
		long long right = vp[i].first + t;
		long long need = (long long)d * (vp[i].second - 1);
		if (left + need > right) return false;
		curlim = left + need + d;
	}
	return true;
}

double run()
{
	vp.clear();
	scanf("%d %d", &n, &d);
	d <<= 1;
	for (int i = 0; i < n; ++i) {
		int a, b;
		scanf("%d %d", &a, &b);
		vp.push_back(make_pair(a * 2, b));
	}
	sort(all(vp));
	if (isok(0)) return 0;
	long long down = 0, up = 100000000000000LL;
	while (down + 1 < up) {
		long long mid = (down + up) / 2;
		if (isok(mid)) {
			up = mid;
		}
		else {
			down = mid;
		}
	}
	return double(up) / 2;
}

int main()
{
	freopen("B1.in", "r", stdin);
	freopen("B1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %.10lf\n", i, run());
	}
	return 0;
}