#include <cstdio>
#include <cstring>

static char hit[2000000 + 4];

static inline int
mark(int a, int b, int n, int m, int p)
{
	int ret = 0;
	for (int i = 0; i < m; i++) {
		if (n >= a and n <= b and !hit[n]) {
			//printf("%d ", n);
			hit[n] = 1;
			ret++;
		}
		n = (n % 10) * p + n / 10;
	}
	//printf("\n");
	return ret;
}

static int
get(int a, int b)
{
	memset(hit + a, 0, b - a + 1);
	int m = 0, p = 1;
	while (p <= a) {
		p *= 10;
		m++;
	}
	p /= 10;

	int ret = 0;
	for (int i = a; i <= b; i++)
		if (!hit[i]) {
			int here = mark(a, b, i, m, p);
			ret += here * (here - 1) / 2;
		}
	return ret;
}

int
main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		printf("Case #%d: %d\n", i, get(a, b));
	}
	return 0;
}
