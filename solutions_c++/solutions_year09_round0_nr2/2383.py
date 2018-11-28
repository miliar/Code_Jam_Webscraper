#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<algorithm>
using namespace std;
int a[105][105];
int visited[105][105];
char b[105][105],current;
int H,W;
char rec(int i,int j)
{
	int min=a[i][j];
	visited[i][j]=1;
	if(i-1>=0)
	{
		if(a[i-1][j]<min)
			min=a[i-1][j];
	}
	if(i+1<=H)
	{
		if(a[i+1][j]<min)
			min=a[i+1][j];
	}
	if(j-1>=0)
	{
		if(a[i][j-1]<min)
			min=a[i][j-1];
	}
	if(j+1<=W)
	{
		if(a[i][j+1]<min)
			min=a[i][j+1];
	}
	
	if(min==a[i][j])
	{
		b[i][j]=current++;
		return b[i][j];
	}	

	if(i-1>=0&&min==a[i-1][j])
	{
		if(visited[i-1][j])
		{
			b[i][j]=b[i-1][j];
			return b[i-1][j];
		}
		else
		{
			b[i][j]=rec(i-1,j);
			return b[i][j];
		}
	}
	else if(j-1>=0&&min==a[i][j-1])
	{
		if(visited[i][j-1])
		{
			b[i][j]=b[i][j-1];
			return b[i][j-1];
		}
		else
		{
			b[i][j]=rec(i,j-1);
			return b[i][j];
		}
	}
	else if(j+1<=W&&min==a[i][j+1])
	{
		if(visited[i][j+1])
		{
			b[i][j]=b[i][j+1];
			return b[i][j+1];
		}
		else
		{
			b[i][j]=rec(i,j+1);
			return b[i][j];
		}
	}
	else if(i+1<=H&&min==a[i+1][j])
	{
		if(visited[i+1][j])
		{
			b[i][j]=b[i+1][j];
			return b[i+1][j];
		}
		else
		{
			b[i][j]=rec(i+1,j);
			return b[i][j];
		}
	}
	
	

}
int main()
{
	int i,j,T,x,min;
	//freopen("outB.txt","w",stdout);
	scanf("%d",&T);
	for(x=1;x<=T;x++)
	{
		current = 'a';
		memset(a,10001,sizeof(a));
		memset(b,'1',sizeof(b));
		memset(visited,0,sizeof(visited));
		scanf("%d%d",&H,&W);
		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				scanf("%d",&a[i][j]);
		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
			{
				if(!visited[i][j])
					b[i][j]=rec(i,j);
			}

		printf("Case #%d:\n",x);
			for(i=0;i<H;i++)
			{
				for(j=0;j<W;j++)
				{
					printf("%c",b[i][j]);
					if(j!=W-1)
						printf(" ");
				}
				printf("\n");
			}
	}
}