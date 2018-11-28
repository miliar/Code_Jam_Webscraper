#include<string.h>
#include<stdio.h>

int graph[100][100];
int h,w;
bool ok[100][100];
char r[100][100];
int dir[4][2] = {1,0,0,1,0,-1,-1,0};

int icon = 0;

bool legal(int x,int y)
{
	if(x<h&&x>=0&&y<w&&y>=0)
		return true;
	return false;
}

void DFS(int i,int j,char &s)
{
	ok[i][j] = true;
	int k;
	int x,y,nx,ny;;
	int mini = 20000;
	for(k=0;k<4;k++)
	{
		x = i+dir[k][0];
		y = j+dir[k][1];
		if(legal(x,y) && graph[x][y] <= mini)
		{
			mini = graph[x][y];
			nx = x;
			ny = y;
		}
	}
	if(mini < graph[i][j])
	{
		DFS(nx,ny,s);
	}
	else
	{
		if(r[i][j] == '1')
		{
			s = r[i][j] = icon+'a';
			icon++;
		}
		else
			s = r[i][j];
		return;
	}
	r[i][j] = s;
}
int main(void)
{
	freopen("E:\\B-small.in","r",stdin);
	freopen("E:\\B-small.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int tes ;
	for(tes = 1; tes <= t;tes++)
	{
		icon = 0;
		memset(ok,0,sizeof(ok));
		memset(r,'1',sizeof(r));
		scanf("%d%d",&h,&w);
		int i,j;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				scanf("%d",&graph[i][j]);
			}
		}
		char trash;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				if(!ok[i][j])
					DFS(i,j,trash);
			}
		}
		printf("Case #%d:\n",tes);
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				if(j)
					printf(" ");
				printf("%c",r[i][j]);
			}
			puts("");
		}
	}
	return 0;
}
				
