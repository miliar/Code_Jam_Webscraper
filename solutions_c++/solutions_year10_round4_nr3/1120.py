/*

 


*/

#include <stdio.h>
#include <string.h>

int C;
int a[2][110][110];
int n;
int ans;


int ok(int now)
{
	int i,j,k;
	k=0;
	for (i=0;i<101;i++)
		for (j=0;j<101;j++)
			k+=a[now][i][j];
	return k==0;
}

int main()
{
	freopen("C-small-attempt0.in.txt","r",stdin);
//	freopen("c.txt","r",stdin);
	freopen("c.out","w",stdout);

	scanf("%d",&C);
	int i,j,k,l;
	int x,y;
	int len;
	int x1,y1,x2,y2;
	int now,pre;
	int tt;
	for (tt=1;tt<=C;tt++)
	{
		memset(a,0,sizeof(a));
		scanf("%d",&n);
		now=0;pre=1;
		for (i=0;i<n;i++)
		{
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for (j=x1;j<=x2;j++)
			{
				for (k=y1;k<=y2;k++)
				{
					a[now][j][k]=1;
				}
			}
		}

		int ans=0;
		do
		{			
			if (ok(now))
			{
				break;
			}
			ans++;
			pre=now;
			now=1-pre;

			for (i=1;i<101;i++)
			{
				for (j=1;j<101;j++)
				{
					a[now][i][j]=a[pre][i][j];
					if (a[pre][i-1][j]==0 && a[pre][i][j-1]==0)
					{
						a[now][i][j]=0;
					}
					if (a[pre][i-1][j]==1 && a[pre][i][j-1]==1)
					{
						a[now][i][j]=1;
					}
				}
			}
		}
		while (1);

		printf("Case #%d: %d\n",tt,ans);
		
	}

	return 0;
}
