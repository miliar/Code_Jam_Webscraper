#include <cstdio>
#include <map>
#include <string>
#include <vector>
#include <queue>
using namespace std;

#define CODE C-small-attempt0

#define INPUT QUOTE(CODE)".in"
#define OUTPUT QUOTE(CODE)".out"
#define _QUOTE(x) #x
#define QUOTE(x) _QUOTE(x)

#define RANGE 1100100

int arr[2*RANGE];
int *st = arr + RANGE;
queue<int> q;

int solve() {
	fill(arr, arr + 2 * RANGE, 0);
	int c;
	scanf("%d", &c);
	for (int i = 0; i < c; ++i) {
		int p, v;
		scanf("%d %d", &p, &v);
		st[p] = v;
		if (v > 1)
			q.push(p);
	}
	
	int split = 0;
	while (!q.empty()) {
		int p = q.front(); q.pop();
		int v = st[p] / 2;
		st[p] -= 2 * v;
		split += v * (v + 1) * (2 * v + 1) / 6;
		for (int i = 1; i <= v; ++i) {
			if ((++st[p-i]) == 2)
				q.push(p-i);
			if ((++st[p+i]) == 2)
				q.push(p+i);
		}
	}
	return split;
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
