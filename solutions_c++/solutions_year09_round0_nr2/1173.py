#include <stdio.h>
#include <string.h>

int matr[110][110];
char color[110][110];
int di[4]={-1,0,0,1};
int dj[4]={0,-1,1,0};
char curcolor;
int h,w;

int inboard(int i,int j)
{
	return i>=0 && i<h && j>=0 && j<w;
}
void dfs(int i, int j)
{
	if (color[i][j])
		return;
	int lowest=-1,min=1000000;
	for (int k=0;k<4;k++)
	{
		if (inboard(i+di[k],j+dj[k]) && matr[i+di[k]][j+dj[k]]<min)
		{
			lowest=k;
			min=matr[i+di[k]][j+dj[k]];
		}
	}
	if (min>=matr[i][j])
	{
		color[i][j]=curcolor++;
		return;
	}
	dfs(i+di[lowest],j+dj[lowest]);
	color[i][j]=color[i+di[lowest]][j+dj[lowest]];
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for (int tt=0;tt<t;tt++)
	{
		curcolor = 'a';
		memset(color,0,sizeof(color));
		scanf("%d%d",&h,&w);
		for (int i=0;i<h;i++)
			for (int j=0;j<w;j++)
				scanf("%d",&matr[i][j]);
		for (int i=0;i<h;i++)
			for (int j=0;j<w;j++)
				dfs(i,j);
		printf("Case #%d:\n",tt+1);
		for (int i=0;i<h;i++)
			for (int j=0;j<w;j++)
			{
				printf("%c",color[i][j]);
				if (j==w-1)
					printf("\n");
				else
					printf(" ");
			}
	}
	return 0;
}