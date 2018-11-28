#include <cstdio>
#include <cstdlib>
using namespace std;

#define MAXN 1024
int g[MAXN];

long long sum[MAXN];
int next[MAXN];

int r, k, n;

void init() {
	scanf("%d%d%d", &r, &k, &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", g + i);
	}

	for (int i = 0; i < n; ++i) {
		sum[i] = g[i];

		int j = (i + 1) % n;

		while (true) {
			if (j == i) break;
			if (sum[i] + g[j] > k) break;			

			sum[i] += g[j];
			j = (j + 1) % n;
		}

		next[i] = j;			
	}
}

long long solve() {
	long long res = 0;
	int index = 0;
	for (int i = 0; i < r; ++i) {
		res += sum[index];
		index = next[index];
	}

	return res;
}

int main(void) {
	int t;
	int r, k, n;
	freopen("inp.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		init();
		printf("Case #%d: %I64d\n", i + 1, solve());
	}
	return 0;
}