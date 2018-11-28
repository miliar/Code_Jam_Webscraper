#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

	
int t;
int map[110][110];
char basin[110][110];
int di[] = {-1, 0, 0, 1};
int dj[] = {0, -1, 1, 0};
int h, w;

void setbasin(int i, int j, char idx)
{
	basin[i][j] = idx;
	for(int k=0;k<4;++k)
	{
		int ti = i + di[k];
		int tj = j + dj[k];
		if(ti > 0 && ti <= h && tj > 0 && tj <= w && basin[ti][tj] < 4)
		{
			int tti = ti + di[basin[ti][tj]];
			int ttj = tj + dj[basin[ti][tj]];
			if(tti == i && ttj == j)
			{
				setbasin(ti, tj, idx);
			}
		}
	}
}

int main()
{
//	freopen("in.txt", "r", stdin);
	scanf("%d", &t);
	int count = 1;
	while(t)
	{
		scanf("%d %d", &h, &w);
		for(int i=0;i<h;++i)
			for(int j=0;j<w;++j)
			{
				scanf("%d", &map[i+1][j+1]);
				basin[i+1][j+1] = 0;
			}
		for(int i=0;i<=h;++i)
		{
			map[i][0] = map[i][w+1] = 999999999;
		}
		for(int i=0; i<=w;++i)
		{
			map[0][i] = map[h+1][i] = 999999999;
		}

		for(int i=1;i<=h;++i)
			for(int j=1;j<=w;++j)
			{
				int lowv = map[i][j];
				int ld = 4;
				for(int k=0;k<4;++k)
				{	
					int t = map[i+di[k]][j+dj[k]];
					if(t < lowv)
					{
						lowv = t;
						ld = k;
					}
				}
				basin[i][j]=ld;
			}

/*
		for(int i=1;i<=h;++i)
		{
			for(int j=1;j<=w;++j)
			{
				printf("%d ", basin[i][j]);
			}
			printf("\n");
		}
*/
		char idx = 'a';
		for(int i=1;i<=h;++i)
			for(int j=1;j<=w;++j)
			{
				if(basin[i][j] < 5)
				{
					int tmp = basin[i][j];
					int ti = i, tj = j;
					while(tmp != 4)
					{
						ti += di[tmp];
						tj += dj[tmp];
						tmp = basin[ti][tj];
					}
					setbasin(ti, tj, idx);
					++idx;
				}
			}

		printf("Case #%d:\n", count);
		for(int i=1;i<=h;++i)
		{
			for(int j=1;j<=w;++j)
			{
				printf("%c ", basin[i][j]);
			}
			printf("\n");
		}
		++count;
		--t;
	}
	return 0;
}
