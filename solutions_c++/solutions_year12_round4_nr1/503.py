#include <cstdio>
#include <map>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define sqr(x) ((x) * (x))
#define two(x) (1 << (x))
#define ord(x, y, z) ((x) <= (y) && (y) <= (z))
#define X first
#define Y second

typedef long long LL;
typedef pair<int, int> pair2;

const int N = 11000;
const double eps = 1e-9;
const int oo = 1000000000;

int n, f[N], d;
pair2 vines[N];
map<int, int> exist;

void init() {
	scanf("%d", &n);
	exist.clear();
	for (int i = 0; i < n; ++i) {
		scanf("%d%d", &vines[i].X, &vines[i].Y);
		exist[vines[i].X] = vines[i].Y;
	}
	scanf("%d", &d);
}

bool solve() {
	int pre = 0;
	f[0] = vines[0].X;
	if (f[0] * 2 >= d) { return true; }
	for (int i = 1; i < n; ++i) {
		while (pre < i && vines[pre].X + f[pre] < vines[i].X) { ++pre; }
		if (pre == i) {
			f[i] = 0;
		} else {
			f[i] = min(vines[i].Y, vines[i].X - vines[pre].X);
		}
		if (f[i] + vines[i].X >= d) {
			return true;
		}
	}
	return false;
}

int main() {
	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		init();
		bool ans = solve();
		printf("Case #%d: ", ++cas);
		if (ans) { puts("YES"); } else { puts("NO"); }
	}
	return 0;
}

