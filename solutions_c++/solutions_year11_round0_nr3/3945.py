#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<int> a;

void solve_brute() {
	int ma = 0;
	for (int mask = 1;  mask < (1 << n)-1; ++mask) {
		int y1 = 0;
		int x1 = 0, x2 = 0;
		for (int i = 0; i < n; ++i) {
			if ((1 << i) & mask) {
				y1 += a[i];
				x1 ^= a[i];
			} else {
				x2 ^= a[i];
			}
		}
		if (x1 == x2) {
			ma = (y1 > ma ? y1 : ma);
		}
	}
	if (ma)
		printf("%d\n", ma);
	else
		printf("NO\n");
}

void solve() {
	int sum = 0;
	int x = 0;
	for(int i = 0; i < n; ++i) {
		sum += a[i];
		x ^= a[i];
	}
	if(n < 2 || x) printf("NO\n");
	else printf("%d\n", sum - *min_element(a.begin(), a.end()));
}

void input() {
	scanf("%d", &n);
	int t;
	a.clear();
	for(int i = 0; i < n; ++i) {
		scanf("%d", &t);
		a.push_back(t);
	}
}

int main() {
	int m;
	scanf("%d", &m);
	for(int i = 0; i < m; ++i) {
		input();
		printf("Case #%d: ", i+1);
		solve();
	}
}
