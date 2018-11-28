#include <iostream>
using namespace std;
int n, r;
const int MAXN = 200;
int g[MAXN][MAXN], p[MAXN][MAXN];

int main()
{
	int t, count, ques;
	scanf("%d", &ques);
	for (int quesnum = 0; quesnum < ques; quesnum++) 
	{
		scanf("%d", &n);
		memset(g, 0, sizeof(g));
		for (int i = 0; i < n; i++)
		{
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; x++)
				for (int y = y1; y <= y2; y++)
					g[x][y]=1;
		}
	    count = 0;

		while (true)
		{
			int c = 0;
			for(int i = 1; i < MAXN; i++)
				for(int j = 1; j < MAXN; j++)
					c += g[i][j];
			if(c==0) break;

			memset(p, 0,sizeof(MAXN));
			for(int i = 2; i < MAXN; i++)
			{
				p[1][i] = g[1][i];
				if(!g[1][i-1])
					p[1][i] = 0;
				p[i][1]=g[i][1];
				if(!g[i-1][1])
					p[i][1] = 0;
			}
			p[1][1]=0;
			for(int i = 2;i < MAXN; i++)
				for(int j = 2; j < MAXN; j++)
					if(g[i][j])
						p[i][j] = g[i-1][j]|g[i][j-1];
					else
						p[i][j] = g[i-1][j]&g[i][j-1];
			memcpy(g, p, sizeof(g));
			count++;
		}
		printf("Case #%d: %d\n", quesnum + 1, count);
	}
	return 0;
}
