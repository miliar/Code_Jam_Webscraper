#include <cstdio>
#include <algorithm>

using namespace std;

struct P
{
	int a, b;
};

static P a[20][10000];

static bool cmp1(const P &a, const P &b)
{
	return a.a < b.a;
}

static bool cmp2(const P &a, const P &b)
{
	return a.b < b.b;
}

static long long req(int x, int y, int h)
{
	if ((y - x) == 1)
		return 0;
	for (int i = x; i < y; i++)
		a[h + 1][i] = a[h][i];
	int c = (x + y) / 2;
	long long inv = req(x, c, h + 1) + req(c, y, h + 1);
	int i = 0, j = 0;
	while ((i + j) < (y - x))
		if ((cmp2(a[h + 1][c + j], a[h + 1][x + i])/*(a[h + 1][x + i] > a[h + 1][c + j])*/ && ((j + c) < y)) || ((i + x) >= c))
		{
			a[h][x + i + j] = a[h + 1][c + j];
			inv += c - i - x;
			j++;
		}
		else
		{
			a[h][x + i + j] = a[h + 1][x + i];
			i++;
		}
	return inv;
}

int main(int argc, char *argv[])
{
	int t;
	scanf("%d", &t);
	for (int cs = 0; cs < t; cs++)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d %d", &a[0][i].a, &a[0][i].b);
		sort(a[0], a[0] + n, cmp1);
//		for (int i = 0; i < n; i++)
//			printf("%d ", a[0][i]);
//		printf("\n");
		printf("Case #%d: %lld\n", cs + 1, req(0, n, 0));
	}
	return 0;
}
