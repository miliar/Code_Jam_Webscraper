#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

const int MAXN = 1000;

int matr[MAXN][MAXN];
int abs(int x)
{
	return x<0 ? -x: x;
}
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
		memset(matr,0,sizeof(matr));
		int r;
		scanf("%d",&r);
		for (int k=0;k<r;k++)
		{
			int x,y,X,Y;
			scanf("%d%d%d%d",&x,&y,&X,&Y);
			if (x>X)
				swap(x,X);
			if (y>Y)
				swap(y,Y);
			for (int i=x;i<=X;i++)
				for (int j=y;j<=Y;j++)
					matr[i][j]=1;
		}
		int c;
		for (c=0;;c++)
		{
			int ind=0;
			for (int i=MAXN-1;i>=0;i--)
			for (int j=MAXN-1;j>=0;j--)
			{
				if (matr[i][j])
					ind=1;
				if (i>0 && j>0 && matr[i-1][j] && matr[i][j-1] && !matr[i][j])
					matr[i][j]=1;
				if (i>0 && j>0 && !matr[i-1][j] && matr[i][j] && !matr[i][j-1])
					matr[i][j]=0;
			}
			if (!ind)
				break;
		}
		printf("Case #%d: %d\n",t1+1,c);
	}
	return 0;
}
