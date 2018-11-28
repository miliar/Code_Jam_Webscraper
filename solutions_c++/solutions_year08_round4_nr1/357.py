#include <stdio.h>
#include <algorithm>
using namespace std;
const int maxn = 1000001;
const int infi = 10000000;
int t, i, j, m, final, x;
int ty[maxn], changeable[maxn], f[maxn][2];

int dmin(int a, int b, int c, int d)
{
	return min(min(min(a, b), c), d);
}

void work()
{
	scanf("%d%d", &m, &final);
	for (i=1;i<=(m-1)/2;++i)
		scanf("%d%d", &ty[i], &changeable[i]);
	for (i=1;i<=(m+1)/2;++i)
	{
		scanf("%d", &x);
		if (x == 1)
			f[(m-1)/2 + i][1] = 0, f[(m-1)/2 + i][0] = infi;
		else
			f[(m-1)/2 + i][1] = infi, f[(m-1)/2 + i][0] = 0;
	}
	for (i=(m-1)/2;i>=1;--i)
	{
		f[i][0] = infi; f[i][1] = infi;
		if (changeable[i] == 0)
			if (ty[i] == 1)
			{
				f[i][0] = dmin(f[i][0],
							   f[i * 2][1] + f[i * 2 + 1][0],
							   f[i * 2][0] + f[i * 2 + 1][1],
							   f[i * 2][0] + f[i * 2 + 1][0]);
				f[i][1] = dmin(f[i][1],
							   f[i * 2][1] + f[i * 2 + 1][1],
							   infi,
							   infi);
			}
			else
			{
				f[i][1] = dmin(f[i][1],
								f[i * 2][1] + f[i * 2 + 1][0],
								f[i * 2][0] + f[i * 2 + 1][1],
								f[i * 2][1] + f[i * 2 + 1][1]);
				f[i][0] = dmin(f[i][0],
								f[i * 2][0] + f[i * 2 + 1][0],
								infi,
								infi);
			}
		else
			if (ty[i] == 1)
			{
				f[i][0] = dmin(f[i][0],
							   f[i * 2][1] + f[i * 2 + 1][0],
							   f[i * 2][0] + f[i * 2 + 1][1],
							   f[i * 2][0] + f[i * 2 + 1][0]);
				f[i][0] = dmin(f[i][0],
							   f[i * 2][0] + f[i * 2 + 1][0] + 1,
							   infi,
							   infi);
				f[i][1] = dmin(f[i][1],
							   f[i * 2][1] + f[i * 2 + 1][1],
							   infi,
							   infi);
				f[i][1] = dmin(f[i][1],
							   f[i * 2][1] + f[i * 2 + 1][0] + 1,
							   f[i * 2][0] + f[i * 2 + 1][1] + 1,
							   f[i * 2][1] + f[i * 2 + 1][1] + 1);
			}
			else
			{
				f[i][1] = dmin(f[i][1],
							   f[i * 2][1] + f[i * 2 + 1][0],
							   f[i * 2][0] + f[i * 2 + 1][1],
							   f[i * 2][1] + f[i * 2 + 1][1]);
				f[i][1] = dmin(f[i][1],
							   f[i * 2][1] + f[i * 2 + 1][1] + 1,
							   infi,
							   infi);
				f[i][0] = dmin(f[i][0],
							   f[i * 2][0] + f[i * 2 + 1][0],
							   infi,
							   infi);
				f[i][0] = dmin(f[i][0],
							   f[i * 2][1] + f[i * 2 + 1][0] + 1,
							   f[i * 2][0] + f[i * 2 + 1][1] + 1,
							   f[i * 2][0] + f[i * 2 + 1][0] + 1);
			}
		
	}
	printf("Case #%d: ", t);
	if (f[1][final] == infi)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", f[1][final]);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%d", &test);
	for (t=1;t<=test;++t)
		work();
}
