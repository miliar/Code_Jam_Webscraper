#include <cstdio>
#include <cstdlib>

#define NGOOGS 128

int points[NGOOGS];

int intcomp(const void *a, const void *b)
{
	int c = *(int *)a;
	int d = *(int *)b;
	return c > d;
}

int main(void)
{
	int t;
	scanf("%d",&t);
	for(int z(0); z < t; ++z)
	{
		printf("Case #%d: ",z+1);
		int n;
		int s;
		int p;
		int y = 0;
		scanf("%d%d%d",&n,&s,&p);

		for(int x(0); x < n; ++x)
		{
			scanf("%d",&points[x]);
		}
		qsort(points, n, sizeof(points[0]), intcomp);
		for(int i(0); i < n; ++i)
		{
			int j1, j2, j3, r;
			r = points[i] % 3;
			j1 = j2 = j3 = points[i] / 3;
			if(r > 0)
			{
				++j1;
				--r;
			}
			if(r > 0)
			{
				++j2;
				--r;
			}
			if(j1 >= p)
			{
//			printf("%d %d %d + %d\n", j1, j2, j3, r);
				++y;
				continue;
			}
			if(j2 > 0)
			{
				--j2;
				++j1;
			}
			if(j1-j2 <= 2 && j1-j3 <= 2)
			{
				if(s > 0 && j1 >= p)
				{
//			printf("**%d %d %d + %d\n", j1, j2, j3, r);
					--s;
					++y;
					continue;
				}
			}
//			printf("*%d %d %d + %d\n", j1, j2, j3, r);

		}
		printf("%d",y);
		printf("\n");
	}

	return 0;
}
