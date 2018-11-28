#include <stdio.h>
#include <string.h>

char g[2][102][102];

int now,last;

bool zero()
{
	int i,j;
	for(i=0;i<=101;i++)
		for(j=0;j<=101;j++)
            if(g[last][i][j])
				return false;
	return true;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int caset = 1;
	int r1,r2,c1,c2;
	int ct;scanf("%d",&ct);
	while(ct--)
	{
       memset(g,0,sizeof(g));
	   int i,n,j,k;
	   scanf("%d",&n);
	   last = 0,now = 1;
	   for(i=0;i<n;i++)
	   {
           scanf("%d%d%d%d",&c1,&r1,&c2,&r2);
		   for(j=r1;j<=r2;j++)
			   for(k=c1;k<=c2;k++)
				   g[last][j][k] = 1;
	   }
	   int ret = 0;
	   while(1)
	   {
		   if(zero())
			   break;
		   for(i=1;i<=100;i++)
		   for(j=1;j<=100;j++)
			   if(g[last][i][j]==0 && g[last][i-1][j] && g[last][i][j-1])
				   g[now][i][j] = 1;
			   else if(g[last][i][j]==1)
			   {
				    if( g[last][i-1][j] || g[last][i][j-1])
						g[now][i][j] = 1;
					else
						g[now][i][j] = 0;
			   }
			   else
				   g[now][i][j] = 0;
       
		  last = 1-last,now = 1-now;
		  ret++;
	   }
	   printf("Case #%d: %d\n",caset++,ret);
	}
	return 0;
}