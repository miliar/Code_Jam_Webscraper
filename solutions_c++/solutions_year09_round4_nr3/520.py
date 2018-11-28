#include "stdio.h"
#include "string.h"
int con[101][101];
int n,m,res,x[101][30],list[17][17],num[17];
void search(int now,int col)
{
	int i,k;
	if(col>=res)
		return;
	if(now==n+1)
	{
		if(col<res)
			res=col;
		return;
	}
	for(i=1;i<=col;i++)
	{
		for(k=0;k<num[i];k++)
			if(con[list[i][k]][now]==0)
				break;
		if(k==num[i])
		{
			list[i][num[i]++]=now;
			search(now+1,col);
			num[i]--;
		}
	}
	list[col+1][0]=now;
	num[col+1]=1;
	search(now+1,col+1);
}
int main()
{
	int t,kase,i,k,j;
	scanf("%d",&kase);
	for(t=1;t<=kase;t++)
	{
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			for(k=0;k<m;k++)
				scanf("%d",&x[i][k]);
		for(i=1;i<=n;i++)
		{
			con[i][i]=0;
			for(k=i+1;k<=n;k++)
			{
				con[i][k]=con[k][i]=1;
				for(j=1;j<m;j++)
					if( (x[i][j-1]>=x[k][j-1]&&x[i][j]<=x[k][j])||(x[i][j-1]<=x[k][j-1]&&x[i][j]>=x[k][j]) )
					{
						con[i][k]=con[k][i]=0;
						break;
					}
			}
		}
		for(i=1;i<=n;i++)
			num[i]=0;
		res=1000;
		search(1,0);
		printf("Case #%d: %d\n",t,res);
	}
	return 0;
}