#include <stdio.h>

int n,m;
FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");
int a[53][53];
int chk[53][53];
int endf;
char q[4]={'.','/','\\'};
void dfs(int x,int y)
{
	if(x==n)
	{
		int i,j,flag=0;
		
		for(i=1 ; i<=n ; i++)
		{
			for(j=1 ; j<=m ; j++)
			{
				if(a[i][j]==1 && chk[i][j]==0)
				{
					flag=1;
					break;
				}
			}
			if(flag==1)
				break;
		}
		if(flag==0)
		{
			endf=1;
			for(i=1 ; i<=n ; i++)
			{
				for(j=1 ; j<=m ; j++)
				{
					fprintf(out,"%c",q[ chk[i][j] ]);
				}
				fprintf(out,"\n");
			}
		}
		return;
	}

	if(endf==1)
		return;

	if(y>=m)
		dfs(x+1,1);
	else
	{
		if(a[x][y]==1 && a[x][y+1]==1 && a[x+1][y]==1 && a[x+1][y+1]==1 && chk[x][y]==0 && chk[x][y+1]==0 && chk[x+1][y]==0 && chk[x+1][y+1]==0 )
		{
			chk[x][y]=chk[x+1][y+1]=1;
			chk[x+1][y]=chk[x][y+1]=2;
			dfs(x,y+1);
			chk[x][y]=chk[x+1][y]=chk[x][y+1]=chk[x+1][y+1]=0;
		}
		else if(a[x][y]==0 || (a[x][y]==1 && chk[x][y]!=0))
			dfs(x,y+1);
	}
}
int main()
{
	int i,t,j,k;
	char tmp[100];

	fscanf(in,"%d ",&t);

	for(i=1 ; i<=t ; i++)
	{
		fscanf(in,"%d %d ",&n,&m);
		for(j=1 ; j<=n ; j++)
		{
			fscanf(in,"%s ",&tmp);
			for(k=1 ;k<=m ; k++)
			{
				if(tmp[k-1]=='#')
					a[j][k]=1;
				else
					a[j][k]=0;
			}
		}
		fprintf(out,"Case #%d: \n",i);
		endf=0;
		dfs(1,1);
		if(endf==0)
			fprintf(out,"Impossible\n");
	}
	return 0;
}