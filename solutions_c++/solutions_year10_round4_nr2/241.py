#include <cstdio>
#include <algorithm>
using namespace std;

int m[2100];
long long pr[2100];
long long mem[2100][12];
int p;

long long naj(int v, int has) {
	//printf("? mem[%d][%d]\n", v, has);
	if (mem[v][has] == -1) {
		if (v >= (1<<p)) {  // leaf
			if (has >= m[v]) {
				mem[v][has] = 0;
			} else {
				mem[v][has] = -2;
			}
		} else {
			long long left = naj(v*2, has);
			long long right = naj(v*2+1, has);
			long long left1 = naj(v*2, has+1);
			long long right1 = naj(v*2+1, has+1);

			if (left1 == -2 || right1 == -2) {
				mem[v][has] = -2;
			} else if (left == -2 || right == -2) {
				mem[v][has] = pr[v] + left1 + right1;
			} else {
				mem[v][has] = min(pr[v] + left1 + right1,
					              left + right);
			}
		}
	}
	//printf("mem[%d][%d] = %lld\n", v, has, mem[v][has]);
	return mem[v][has];
}

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		scanf("%d", &p);
		for (int i = (1<<p); i < (1<<(p+1)); ++i) {
			scanf("%d", &m[i]);
			m[i] = p - m[i];
		}
		for (int start = (1<<(p-1)); start >= 1; start >>= 1) {
			for (int i = start; i < (start<<1); ++i) {
				scanf("%lld", &pr[i]);
			}
		}
		for (int i = 0; i < 2100; ++i) {
			for (int j = 0; j < 12; ++j) {
				mem[i][j] = -1;
			}
		}
		printf("Case #%d: %lld\n", tt, naj(1, 0));
	}
}
