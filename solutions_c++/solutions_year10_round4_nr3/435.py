#include<stdio.h>
#include<string.h>

int mat[105][105],temp[105][105];

int count(void)
{
	int i,j,ret=0;
	for(i=1;i<=100;i++)
		for(j=1;j<=100;j++)
			ret+=mat[i][j];
	return ret;
}

int main()
{
	int t,cs,n,i,j,k;
	freopen("bacteria.in","r",stdin);
	freopen("bacteria.out","w",stdout);
	scanf("%d",&t);
	for(cs=0;cs<t;cs++)
	{
		scanf("%d",&n);
		memset(mat,0,sizeof(mat));
		for(k=0;k<n;k++)
		{
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(i=y1;i<=y2;i++)
				for(j=x1;j<=x2;j++)
					mat[i][j]=1;
		}
		k=0;
		while(count())
		{
			k++;
			memset(temp,0,sizeof(temp));
			for(i=1;i<=100;i++)
				for(j=1;j<=100;j++)
					if(mat[i][j] && (mat[i-1][j]+mat[i][j-1]>0))
						temp[i][j]=1;
					else if(!mat[i][j] && (mat[i-1][j]+mat[i][j-1]==2))
						temp[i][j]=1;
			for(i=1;i<=100;i++)
				for(j=1;j<=100;j++)
					mat[i][j]=temp[i][j];
		}
		printf("Case #%d: %d\n",cs+1,k);
	}
	return 0;
}
