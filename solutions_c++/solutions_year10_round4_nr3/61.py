#include <cstdio>
#include <map>
#include <string>
#include <vector>
using namespace std;

#define CODE C-small-attempt0

#define INPUT QUOTE(CODE)".in"
#define OUTPUT QUOTE(CODE)".out"
#define _QUOTE(x) #x
#define QUOTE(x) _QUOTE(x)

#define MAXR 1005

int r;
int x1[MAXR], y1[MAXR], x2[MAXR], y2[MAXR];
bool used[MAXR];

void read() {
	scanf("%d", &r);
	for (int i = 0; i < r; ++i)
		scanf("%d %d %d %d", &x1[i], &y1[i], &x2[i], &y2[i]);
}

bool cross(int i, int j) {
	if (x1[i] > x2[j] + 1) return false;
	if (x2[i] + 1 < x1[j]) return false;
	if (y1[i] > y2[j] + 1) return false;
	if (y2[i] + 1 < y1[j]) return false;
	return true;
}

int live(int i) {
	int q[MAXR], qn = 0;
	q[qn++] = i;
	used[i] = true;
	int low = x1[i] + y1[i];
	int highx = x2[i], highy = y2[i];
	for (int ii = 0; ii < qn; ++ii) {
		int z = q[ii];
		low = min(low, x1[z] + y1[z]);
		highx = max(highx, x2[z]);
		highy = max(highy, y2[z]);
		for (int j = 0; j < r; ++j)
			if (!used[j] && cross(z, j)) {
				used[j] = true;
				q[qn++] = j;
			}
	}
	return highx + highy - low + 1;
}

int solve() {
	read();
	fill(used, used+MAXR, false);
	int res = 0;
	for (int i = 0; i < r; ++i)
		if (!used[i])
			res = max(res, live(i));
	return res;
}

int main() {
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}
