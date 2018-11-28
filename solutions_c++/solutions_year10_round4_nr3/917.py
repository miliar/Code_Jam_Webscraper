#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>

using namespace std;

int a[2][105][105];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int C,T=0,R;
	scanf("%d",&C);
	while (C-->0)
	{
		T++;
		scanf("%d",&R);
		memset(a,0,sizeof(a));
		while (R-->0)
		{
			int x1,x2,y1,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (int i=x1;i<=x2;i++)
			for (int j=y1;j<=y2;j++)
				a[0][i][j]=1;
		}
		int ans=0,k=0;
		bool check=false;
		while (true)
		{
			check=true;
			for (int i=1;i<=100;i++)
			for (int j=1;j<=100;j++)
				if (a[k][i][j]==1)
					check=false;
			if (check) break;
			ans++;
			for (int i=1;i<=100;i++)
			for (int j=1;j<=100;j++)
			{
				if ((a[k][i-1][j]==1)&&(a[k][i][j-1]==1))
					a[1-k][i][j]=1;
				else
				if ((a[k][i-1][j]==0)&&(a[k][i][j-1]==0))
					a[1-k][i][j]=0;
				else
					a[1-k][i][j]=a[k][i][j];
			}
			k=1-k;
			for (int i=1;i<=100;i++)
			for (int j=1;j<=100;j++)
				a[1-k][i][j]=0;
		}
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}
