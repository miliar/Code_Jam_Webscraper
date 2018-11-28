#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <iostream>
#include <sstream>

using namespace std;

typedef long long i64;
typedef unsigned long u32;
template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T sqr(const T &a) {
	return a * a;
}
char s[510][510];
struct Val {
	i64 si, sj;
	i64 w;
	Val(i64 si, i64 sj, i64 w): si(si), sj(sj), w(w) {
	}
	Val() {
		si = sj = 0;
		w = 0;
	}
	Val operator + (const Val &b) const {
		return Val(si + b.si, sj + b.sj, w + b.w);
	}
	Val operator - (const Val &b) const {
		return Val(si - b.si, sj - b.sj, w - b.w);
	}
} a[510][510];
Val GetVal(int i, int j, int d) {
	if (i > 0 && j > 0) {
		return Val((i64(d) + (s[i][j] - '0')) * i, (i64(d) + (s[i][j] - '0')) * j, d + s[i][j] - '0');
	} else {
		return Val(0, 0, 0);
	}
}
int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int itest = 1; itest <= T; itest++) {
		int n, m, d;
		scanf("%d %d %d", &n, &m, &d);
		d = 0;
		for (int i = 1; i <= n; i++) {
			scanf("%s", s[i] + 1);
		}
		for (int i = 1; i <= n; i++) {
			Val sum(0, 0, 0);
			for (int j = 1; j <= m; j++) {
				sum = sum + GetVal(i, j, d);
				a[i][j] = a[i - 1][j] + sum;
			}
		}
		int res = -1;
		for (int k = 3; k <= min(n, m); k++) {
			//i64 ncells = sqr(k) - 4;
			for (int i = k; i <= n; i++) {
				for (int j = k; j <= m; j++) {
					Val cur = a[i][j] - a[i - k][j] - a[i][j - k] + a[i - k][j - k];
					cur = cur - GetVal(i, j, d) - GetVal(i - k + 1, j, d) - GetVal(i, j - k + 1, d) \
							- GetVal(i - k + 1, j - k + 1, d);
					i64 si = cur.w * (i + i - k + 1);
					i64 sj = cur.w * (j + j - k + 1);
					if (cur.si + cur.si == si && cur.sj + cur.sj == sj) {
						res = k;
						goto ok;
					}
				}
			}
ok:
			;
		}
		if (res == -1) {
			printf("Case #%d: IMPOSSIBLE\n", itest);
		} else {
			printf("Case #%d: %d\n", itest, res);
		}
		fflush(stdout);
	}
	return 0;
}
