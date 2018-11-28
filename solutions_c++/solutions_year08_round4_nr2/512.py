#include <stdio.h>
#include <math.h>

#define MAX 1

int abs(int x) {
	if(x < 0)
		return -x;
	return x;
}

void find_ans() {
	int i, j, k, l, x, y;
	double l1, l2, l3, s, area;
	int n, m, a;

	scanf("%d %d %d", &n, &m, &a);
	/*for(i = 0; i <= n; i++)
		for(j = 0; j <= m; j++)
			if(i * j == a) {
				printf(" 0 0 0 %d %d 0", i, j);
				return;
			}*/
	for(i = 0; i <= n; i++)
		for(j = 0; j <= m; j++) {
			//l1 = sqrt(1.0 * i * i + 1.0 * j * j);
			for(x = i; x <= n; x++)
				for(y = 0; y <= m; y++) {
					area = abs((i * 0 - 0 * j) + (x * j - i * y) + (0 * y - x * 0));
					if(area == a) {
						printf(" 0 0 %d %d %d %d", i, j, x, y);
						return;
					}
					/*l2 = sqrt(1.0 * x * x + 1.0 * y * y);
					l3 = sqrt(1.0 * (x - i) * (x - i) + 1.0 * (y - j) * (y - j));
					s = (l1 + l2 + l3) / 2;
					area = sqrt(s * (s - l1) * (s - l2) * (s - l3)) * 2;
					if(floor((area - floor(area)) * MAX) != 0.0)continue;
					//printf(" %d %d %d %d %lf\n", i, j, x, y, area);
					if(round(area) == a) {
						printf(" 0 0 %d %d %d %d", i, j, x, y);
						return;
					}*/
				}
		}
	printf(" IMPOSSIBLE");
}

int main(int argc, char *argv[])
{
	int i, n;

	scanf("%d", &n);
	for(i = 1; i <= n; i++) {
		printf("Case #%d:", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
