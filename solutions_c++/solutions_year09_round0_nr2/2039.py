#include<stdio.h>
#include<string.h>
int mat[102][102];
char flw[102][102];
char st;
int H,W;
char dfs(int r,int c)
{
	if(flw[r][c]!=0)
		return flw[r][c];

	int val=mat[r][c];
	int pos_x=r;
	int pos_y=c;

	if((r-1)>=0&&mat[r-1][c]<val)
	{
		val=mat[r-1][c];
		pos_x=r-1;
		pos_y=c;
	}
	if((c-1)>=0&&mat[r][c-1]<val)
	{
		val=mat[r][c-1];
		pos_y=c-1;
		pos_x=r;
	}
	if((c+1)<W&&mat[r][c+1]<val)
	{
		val=mat[r][c+1];
		pos_y=c+1;
		pos_x=r;
	}
	if((r+1)<H&&mat[r+1][c]<val)
	{
		val=mat[r+1][c];
		pos_x=r+1;
		pos_y=c;
	}

	if(val<mat[r][c])
		flw[r][c]=dfs(pos_x,pos_y);
	else
	{
		flw[r][c]=st++;
	}
	return flw[r][c];

}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int CS,i,j,cs=1;
	scanf("%d",&CS);
		
	while(CS--)
	{

		scanf("%d %d",&H,&W);

		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				scanf("%d",&mat[i][j]);

		st='a';
		memset(flw,0,sizeof(flw));
	

		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				if(flw[i][j]==0)
					dfs(i,j);
	
		printf("Case #%d:\n",cs++);
		
		for(i=0;i<H;i++)
		{
			printf("%c",flw[i][0]);
			for(j=1;j<W;j++)
				printf(" %c",flw[i][j]);
			printf("\n");
		}
		
	}

	return 0;
}