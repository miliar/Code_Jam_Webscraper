#include<cstdio>
#include<cstring>

bool f[160][160];
int g[160][160];
int n;

int main()
{
    freopen("C-small-attempt0.in","r", stdin);
    freopen("output.txt", "w" ,stdout);
	int cases;
	scanf("%d" , &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		memset( f, false , sizeof(f));
		scanf("%d" , &n);
		for (int t = 0; t < n; ++t)
		{
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (int i = y1; i <= y2; ++i)
				for (int j = x1; j <= x2; ++j)
					f[i][j] = true;
		}
		int times = 0;
		bool finish = false;
		for (; !finish; ++times)
		{
			finish = true;
			memset( g, 0, sizeof(g));
			for (int i = 1; i <= 150; ++i)
				for (int j = 1; j <= 150; ++j)
					if (f[i][j])
					{
						++g[i][j + 1]; ++g[i + 1][j];
					}
			for (int i = 1; i <= 150; ++i)
				for (int j = 1; j <= 150; ++j)
				{
					if ((g[i][j] == 1 && f[i][j]) || g[i][j] == 2) f[i][j] = true , finish = false; else f[i][j] = false;
				}
		}
		printf("Case #%d: %d\n", ca, times);
	}
	fclose(stdin); fclose(stdout);
}
