#include <stdio.h>
#include <string.h>
const int MAXN = 100;

char matr[MAXN][MAXN];
int dirx[4] = {1,0,1,1};
int diry[4] = {0,1,1,-1};
int canwin[300];
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	scanf("%d",&T);
	for (int t1=0;t1<T;t1++)
	{
		memset(canwin,0,sizeof(canwin));
		int n,k;
		scanf("%d%d",&n,&k);
		for (int i=0;i<n;i++)
			scanf("%s",matr[i]);
		for (int i=0;i<n;i++)
		{
			int c = n-1;
			for (int j=n-1;j>=0;j--)
				if (matr[i][j]!='.')
					matr[i][c--] = matr[i][j];
			for (int j=0;j<=c;j++)
				matr[i][j]='.';
		}


		for (int s=0;s<n;s++)
			for (int t=0;t<n;t++)
			{
				char c = matr[s][t];
				for (int j=0;j<4;j++)
				{
					int cnt=0;
					for (int i=0;i<k;i++)
					{
						int x = s+dirx[j]*i;
						int y = t+diry[j]*i;
						if (x>=0 && y>=0 && x<n && y<n && matr[x][y] == c)
							cnt++;
					}
					if (cnt==k && c!='.')
						canwin[c]=1;
				}
			}
		if (canwin['R'] && canwin['B'])
			printf("Case #%d: Both\n",t1+1);
		if (canwin['R'] && !canwin['B'])
			printf("Case #%d: Red\n",t1+1);
		if (!canwin['R'] && canwin['B'])
			printf("Case #%d: Blue\n",t1+1);
		if (!canwin['R'] && !canwin['B'])
			printf("Case #%d: Neither\n",t1+1);
	}
	return 0;
}
