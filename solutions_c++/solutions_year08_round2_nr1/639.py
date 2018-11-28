#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	int T;
	scanf("%d", &T);
	for (int test=1; test<=T; test++) {
		int a, b, c, d, n, m, count=0, dup=0;
		long long x, y;
		int p[100006][2];

		scanf("%d%d%d%d%d%d%d%d", &n, &a, &b, &c, &d, &x, &y, &m);
		p[0][0] = x;
		p[0][1] = y;
		for (int i=1; i<n; i++) {
			int isDup = 0;
			x = ((((a%m) * (x%m))%m) + (b%m)) % m;
			y = ((((c%m) * (y%m))%m) + (d%m)) % m;
			for (int j=0; j<i-dup; j++) {
				if (p[j][0] == x && p[j][1] == y) {
					dup ++;
					isDup = 1;
					break;
				}
			}
			if (isDup == 1) continue;

			p[i-dup][0] = x;
			p[i-dup][1] = y;
		}
		int sum[2];
		for (int i=0; i<n-dup; i++) {
			for (int j=i+1; j<n-dup; j++) {
				for (int k=j+1; k<n-dup; k++) {
					sum[0] = p[i][0] + p[j][0] + p[k][0];
					sum[1] = p[i][1] + p[j][1] + p[k][1];
					if ((sum[0] / 3) * 3 == sum[0] && (sum[1] / 3) * 3 == sum[1])
						count ++;
				}
			}
		}
		printf("Case #%d: %d\r\n", test, count);
	}
	return 0;
}
