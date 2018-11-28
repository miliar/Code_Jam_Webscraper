#include <stdio.h>

int cs, ct, n;
double wp[110], owp[110], oowp[110];
int a[110][110];

int main()
{
	char s[110];
	int i, j, k;
	double u, v, w, x;

	scanf("%d", &ct);
	for (cs = 1; cs <= ct; cs++) {
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%s", s);
			for (j = 0; j < n; j++) {
				if (s[j] == '1') a[i][j] = 1;
				else if (s[j] == '0') a[i][j] = -1;
				else a[i][j] = 0;
			}
		}
		for (i = 0; i < n; i++) {
			u = v = 0;
			for (j = 0; j < n; j++) {
				if (a[i][j] == 1) u++;
				if (a[i][j] != 0) v++;
			}
			wp[i] = u / v;
		}

		for (i = 0; i < n; i++) {
			w = x = 0;
			for (j = 0; j < n; j++)
			if (j != i && a[i][j] != 0) {
				u = v = 0;
				for (k = 0; k < n; k++)
				if (k != j && k != i) {
					if (a[j][k] == 1) u++;
					if (a[j][k] != 0) v++;
				}
				w += u / v;
				x++;
			}
			owp[i] = w / x;
		}

		for (i = 0; i < n; i++) {
			u = v = 0;
			for (j = 0; j < n; j++)
			if (a[i][j] != 0) {
				u += owp[j];
				v++;
			}
			oowp[i] = u / v;
		}

		printf("Case #%d:\n", cs);
		for (i = 0; i < n; i++)
			printf("%.12lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
	}
	return 0;
}
