#include <stdio.h>
#include <string.h>

#define update if (r1 + r0 < r) r = r1 + r0;

const int INF = 1000000;
int d, i, m, n;

inline int abs(int x) {return x < 0? -x : x;}

int a[128];
//     i, a[i] v
int fc[128][256];
// consider a[0..p), make sure last one is v
int f(int p, int v) {
	if (p == 0) return 0;
	if (fc[p][v] == -1) {
		int r = INF, r1;
		// enum last value
		for (int lv = 0; lv < 256; lv++) {
			int r0 = f(p - 1, lv);
			if (r0 >= INF) continue;
			// delete this item (a[p-1]) then insert(s)
			if (m > 0) {
				r1 = i * ((abs(lv - v) + m - 1) / m) + d;
				update;
			} else {
				if (lv == v) {
					r1 = d;
					update;
				}
			}
			// modify direct ?
			if (abs(v - lv) <= m) {
				// WA #1
				r1 = abs(v - a[p - 1]);
				update;
			}
			// this item is smooth with last one
			if (abs(a[p - 1] - lv) <= m) {
				// insert(s)
				if (m > 0) {
					// WA #1
					r1 = i * ((abs(a[p - 1] - v) + m - 1) / m);
					update;
				} else {
					if (a[p - 1] == v) {
						r1 = 0;
						update;
					}
				}
			}
			// delete, modify last
			r1 = d + abs(v - lv);
			update;
		}
		if(0)
		if (r <= 1000) printf("fc[%d][%d] = %d\n", p, v, r);
		fc[p][v] = r;
	}
	return fc[p][v];
}

int main(int argc, char const* argv[])
{
	int tc;
	scanf("%d", &tc);
	for (int ti = 0; ti < tc; ti++) {
		memset(fc, -1, sizeof(fc));

		printf("Case #%d: ", ti+1);
		scanf("%d%d%d%d", &d, &i, &m, &n);
		for (int j = 0; j < n; j++) {
			scanf("%d", &a[j]);
		}
		int r = INF, r1;
		for (int v = 0; v < 256; v++) {
			r1 = f(n, v);
			if (r1 < r) r = r1;
		}
		printf("%d\n", r);
	}

	return 0;
}
