#include<stdio.h>
#include<string.h>
#include<time.h>
#include<cstdlib>
#define MAXD 1010
int N, W, L, x[MAXD], y[MAXD], r[MAXD];
long long sqr(int x)
{
	return (long long)x * x;
}
int intersect(int x1, int y1, int r1, int x2, int y2, int r2)
{
	return sqr(x2 - x1) + sqr(y2 - y1) < sqr(r1 + r2);
}
void init()
{
	int i, j, k;
	scanf("%d%d%d", &N, &W, &L);
	for(i = 0; i < N; i ++)
		scanf("%d", &r[i]);
}
int can()
{
	int i, j;
	for(i = 0; i < N; i ++)
		for(j = i + 1; j < N; j ++)
			if(intersect(x[i], y[i], r[i], x[j], y[j], r[j]))
				return 0;
	return 1;
}
void solve()
{
	int i, j, k;
	for(;;)
	{
		for(i = 0; i < N; i ++)
		{
			x[i] = ((rand() << 15 + rand()) & 0x7fffffff) % W;
			y[i] = ((rand() << 15 + rand()) & 0x7fffffff) % L;
		}
		if(can())
			break;
	}
	for(i = 0; i < N; i ++)
		printf(" %d %d", x[i], y[i]);
	printf("\n");
}
int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	srand((unsigned)time(NULL));
	int t, tt;
	scanf("%d", &t);
	for(tt = 0; tt < t; tt ++)
	{
		init();
		printf("Case #%d:", tt + 1);
		solve();
	}
	return 0;
}
