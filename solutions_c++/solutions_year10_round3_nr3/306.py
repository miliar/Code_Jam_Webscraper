#include <cstdio>
#include <cctype>
#include <algorithm>
using namespace std;

char ch;
int t, it, m, n, i, j, a[512][512], d[512][512], r[512][512], q[512][512], tmp, b, bi, bj, res[512], c;

void doit() {
	b = 0;
	for(i = 0; i < m; ++i) {
		for(j = 0; j < n; ++j) {
			q[i][j] = 1;
			if(j != 0) { r[i][j] = (a[i][j - 1] != a[i][j] ? r[i][j - 1] : 0) + 1; }
			if(i != 0) { d[i][j] = (a[i - 1][j] != a[i][j] ? d[i - 1][j] : 0) + 1; }
			if(i * j != 0 && a[i - 1][j - 1] == a[i][j]) {
				tmp = min(r[i][j], d[i][j]);
				q[i][j] = q[i - 1][j - 1] + 1;
				if(q[i][j] > tmp) { q[i][j] = tmp; }
			}
			if(a[i][j] < 0) { r[i][j] = d[i][j] = q[i][j] = 0; }
			if(q[i][j] > b) {
				bi = i;
				bj = j;
				b = q[i][j];
			}
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for(it = 1; it <= t; ++it) {
		scanf("%d%d", &m, &n);
		for(i = 0; i < m; ++i) {
			getchar();
			for(j = 0; j < n; j += 4) {
				if(isalpha(ch = getchar())) {
					ch = (ch - 'A') + 10;
				} else {
					ch &= 0xf;
				}
				a[i][j] = (ch & 8) >> 3;
				a[i][j + 1] = (ch & 4) >> 2;
				a[i][j + 2] = (ch & 2) >> 1;
				a[i][j + 3] = ch & 1;
			}
		}
		for(i = 0; i < m; ++i) {
			r[i][0] = 1;
		}
		for(j = 0; j < n; ++j) {
			d[0][j] = 1;
		}

		for(c = i = 0; i < 512; res[i++] = 0);

		do {
			doit();
			if(b == 0) { break; }
			++res[b];
			for(i = bi; i > bi - b; --i) {
				for(j = bj; j > bj - b; --j) {
					a[i][j] = -1;
				}
			}
		}while(true);

		for(i = 512; i >= 1; --i) {
			if(res[i] != 0) {
				++c;
			}
		}
		printf("Case #%d: %d\n", it, c);
		for(i = 512; i >= 1; --i) {
			if(res[i] != 0) {
				++c;
				printf("%d %d\n", i, res[i]);
			}
		}
	}
	return 0; }
