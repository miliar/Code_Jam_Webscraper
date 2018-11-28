#include <stdio.h>
#include <memory.h>
#include <algorithm>
#define MN 128
using namespace std;
int n;
char d[MN][MN];
double a[MN], b[MN], c[MN];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T, r, i, j, k, p, q, f, s, m, M;
	char str[4];

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d:\n",t);
		scanf("%d",&n);
		for (i = 0; i < n; i++) scanf("%s",d[i]);
		for (i = 0; i < n; i++) {
			p = q = 0;
			for (j = 0; j < n; j++) {
				if (d[i][j] == '0') {
					q++;
				}
				else if (d[i][j] == '1') {
					p++; q++;
				}
				else {
				}
			}
			a[i] = (double)p/q;
		}
		for (i = 0; i < n; i++) {
			b[i] = 0;
			int cnt = 0;
			for (j = 0; j < n; j++) {
				if (d[i][j] != '.') {
					p = q = 0;
					for (k = 0; k < n; k++) {
						if (k != i) {
							if (d[j][k] == '0') {
								q++;
							}
							else if (d[j][k] == '1') {
								p++; q++;
							}
						}
					}
					b[i] += (double)p/q; cnt++;
				}
			}
			b[i] /= cnt;
		}
		for (i = 0; i < n; i++) {
			c[i] = 0;
			int cnt = 0;
			for (j = 0; j < n; j++) {
				if (d[i][j] != '.') {
					c[i] += b[j];
					cnt++;
				}
			}
			c[i] /= cnt;
		}
		for (i = 0; i < n; i++)
			printf("%.10lf\n",0.25*a[i]+0.50*b[i]+0.25*c[i]);
	}
	return 0;
}