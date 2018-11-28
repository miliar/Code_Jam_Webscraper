#include <cstdio>
#include <cstring>

#define COR_MAX 101

int c, r, x1, y1, x2, y2;
int t[COR_MAX][COR_MAX], _t[COR_MAX][COR_MAX];
int R;

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int lc, i, j, k;
	scanf("%d", &c);
	for (lc = 1; lc <= c; lc++) {
		scanf("%d", &r);
		memset(t, 0, sizeof(t));
		for (i = 0; i < r; i++) {
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			if (x1 > x2) { k = x1; x1 = x2; x2 = k; }
			if (y1 > y2) { k = y1; y1 = y2; y2 = k; }
			for (j = x1; j <= x2; j++)
				for (k = y1; k <= y2; k++)
					t[j][k] = 1;
		}
		for (R = 0; ; R++) {
			k = 0;
			for (i = 1; i < COR_MAX; i++) {
				for (j = 1; j < COR_MAX; j++) {
					_t[i][j] = t[i][j];
					if (_t[i][j]) k = 1;
				}
			}
			if (!k) break;
			for (i = 1; i < COR_MAX; i++) {
				for (j = 1; j < COR_MAX; j++) {
					if (_t[i][j] && !_t[i - 1][j] && !_t[i][j - 1]) t[i][j] = 0;
					else if (!_t[i][j] && _t[i - 1][j] && _t[i][j - 1]) t[i][j] = 1;
					else t[i][j] = _t[i][j];
				}
			}
		}
		printf("Case #%d: %d\n", lc, R);
	}
	return 0;
}