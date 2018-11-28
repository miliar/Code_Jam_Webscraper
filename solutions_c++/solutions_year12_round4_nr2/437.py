#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
using namespace std;

const int N = 2000;
const int inf = 1e9;
int r[N], n, x[N], y[N], p[N], time, used[N];

int get_last() {
	int last = -1;
	for (int i = n - 1; i >= 0; --i)
		if (!used[i]) {
			last = i;
			break;
		}
	return last;
}

void generate(int x1, int y1, int x2, int y2) {
	bool swapped = false;
	if (y2 - y1 > x2 - x1) {
		swapped = true;
		swap(x1, y1);
		swap(x2, y2);
	}
	int last = get_last();
	if (last == -1)
		return;
	int sum = -r[last];
	int curtime = ++time;
	for (int i = n - 1; i >= 0; --i) {
		if ((used[i] != 0) || (sum + r[i] > x2 - x1)) continue;
		used[i] = curtime;
		x[p[i]] = x1 + sum + r[i];
		y[p[i]] = y1;
		sum += 2 * r[i];
	}
	y1 += r[last];
	last = get_last();
	if (last != -1)
		generate(x1, y1 + r[last], x2, y2);
	if (swapped)
		for (int i = 0; i < n; ++i)
			if (used[i] >= curtime)
				swap(x[i], y[i]);
}

int main() {
	int t, w, l;
	scanf("%d", &t);
	for (int it = 0; it < t; ++it) {
		scanf("%d%d%d", &n, &w, &l);
		for (int i = 0; i < n; ++i) {
			p[i] = i;
			scanf("%d", &r[i]);
		}
		for (int i = 0; i < n; ++i)
			for (int j = i + 1; j < n; ++j)
				if (r[i] > r[j]) {
					swap(r[i], r[j]);
					swap(p[i], p[j]);
				}
		memset(used, 0, sizeof(used));
		//sort(r, r + n);
		generate(0, 0, w, l);
		printf("Case #%d:", it + 1);
		for (int i = 0; i < n; ++i) {
			printf(" %d %d", x[i], y[i]);
			assert(x[i] <= w && y[i] <= l);
		}
		printf("\n");
	}
}