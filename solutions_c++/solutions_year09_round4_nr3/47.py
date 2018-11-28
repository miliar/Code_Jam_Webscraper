#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

const int MAXN = 256;
const int MAXK = 32;

bool good(int n, int a[], int b[]) {
	for (int i = 0; i < n; ++i) {
		if (a[i] >= b[i]) {
			return false;
		}
	}
	return true;
}

int hungary(int nl, int nr, int ml[], int mr[], const vector<int> e[]) {
	int ret = 0;
	static int p, t, q[MAXN], pre[MAXN];

	memset(ml, 0xff, nl * sizeof(int));
	memset(mr, 0xff, nr * sizeof(int));
	for (int i = 0; i < nl; i++) {
		memset(pre, 0xff, nr * sizeof(int));
		q[0] = i;
		p = 0;
		t = 1;
		while (p < t) {
			for (vector<int>::const_iterator i = e[q[p]].begin(); i < e[q[p]].end(); ++i) {
				if (pre[*i] == -1) {
					pre[*i] = q[p];
					if (mr[*i] == -1) {
						int y, yy = *i;

						do {
							y = yy;
							yy = ml[pre[y]];
							ml[pre[y]] = y;
							mr[y] = pre[y];
						} while (yy != -1);		
						++ret;
						t = -1;
						break;
					}
					else {
						q[t++] = mr[*i];
					}
				}
			}
			++p;
		}
	}

	return ret;
}

int main() {
	int re, n, k;
	int p[MAXN][MAXK], ml[MAXN], mr[MAXN];
	vector<int> e[MAXN];

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < k; ++j) {
				scanf("%d", &p[i][j]);
			}
		}
		for (int i = 0; i < n; ++i) {
			e[i].clear();
			for (int j = 0; j < n; ++j) {
				if (good(k, p[i], p[j])) {
					e[i].push_back(j);
				}
			}
		}
		printf("Case #%d: %d\n", ri, n - hungary(n, n, ml, mr, e));
	}

	return 0;
}

