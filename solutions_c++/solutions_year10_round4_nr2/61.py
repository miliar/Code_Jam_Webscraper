#include <cstdio>
#include <map>
#include <string>
#include <vector>
using namespace std;

#define CODE B-large

#define INPUT QUOTE(CODE)".in"
#define OUTPUT QUOTE(CODE)".out"
#define _QUOTE(x) #x
#define QUOTE(x) _QUOTE(x)

#define MAXP 10
#define MAXEP (1<<MAXP)

int p;
int m[MAXEP];
int price[MAXP][MAXEP];

int sum[MAXP][MAXEP][MAXP];

void read() {
	scanf("%d", &p);
	for (int i = 0; i < (1 << p); ++i)
		scanf("%d", &m[i]);
	for (int i = 0; i < p; ++i) {
		for (int j = 0; j < (1 << (p - i - 1)); ++j)
			scanf("%d", &price[i][j]);
	}
}

int get(int i, int j, int t) {
	if (i < 0) {
		if (p - t <= m[j])
			return 0;
		return -1;
	}
	int &r = sum[i][j][t];
	if (r > -2)
		return r;
	r = -1;
	int a1 = get(i - 1, 2 * j, t), a2 = get(i - 1, 2 * j + 1, t);
	int a = a1 >= 0 && a2 >= 0 ? a1 + a2 : -1;
	int b1 = get(i - 1, 2 * j, t + 1), b2 = get(i - 1, 2 * j + 1, t + 1);
	int b = b1 >= 0 && b2 >= 0 ? b1 + b2 + price[i][j] : -1;
	if (a >= 0 && (r < 0 || a < r))
		r = a;
	if (b >= 0 && (r < 0 || b < r))
		r = b;
	return r;
}

int solve() {
	read();
	fill(sum[0][0], sum[MAXP][0], -2);
	return get(p - 1, 0, 0);
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
