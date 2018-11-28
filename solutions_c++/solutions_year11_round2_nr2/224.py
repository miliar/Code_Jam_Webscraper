#include <stdio.h>

int cs, ct;
int c, d, p, v, n;
int a[1100000];

int main()
{
	int i, j;
	double lb, ub, time, left, right;
	scanf("%d", &ct);
	for (cs = 1; cs <= ct; cs++) {
		scanf("%d%d", &c, &d);
		n = 0;
		for (i = 0; i < c; i++) {
			scanf("%d%d", &p, &v);
			for (j = 0; j < v; j++)
				a[n++] = p;
		}
		lb = 0;
		ub = 1e30;
		while (lb + 1e-3 < ub) {
			time = (lb + ub) / 2;
			left = a[0] - time;
			for (i = 1; i < n; i++) {
				if (a[i] - time <= left + d) left += d;
				else left = a[i] - time;
				if (left > a[i] + time) break;
			}

			if (i < n) lb = time;
			else ub = time;
//			printf("%lf %lf\n", lb, ub);
		}

		printf("Case #%d: %.1lf\n", cs, ub);
	}	
	return 0;
}
