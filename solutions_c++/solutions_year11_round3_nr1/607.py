#include<iostream>
#include<stdio.h>
using namespace std;
#define N 101
int r,c;
char a[N][N],ans[N][N];
bool replace(int x,int y)
{
	if(x==r-1 || y==c-1) return false;
	ans[x][y]='/';
	if(ans[x][y+1]!='#') return false;
	ans[x][y+1]='\\';
	if(ans[x+1][y]!='#') return false;
	ans[x+1][y]='\\';
	if(ans[x+1][y+1]!='#') return false;
	ans[x+1][y+1]='/';
	return true;
}
bool solve(int x,int y)
{
	int i,j;
	if(x==r) return true;
	for(j=y;j<c;j++) 
		if(ans[x][j]=='#') break;
	if(j==c)
	{
		for(i=x+1;i<r;i++)
		{
			for(j=0;j<c;j++)
				if(ans[i][j]=='#') break;
			if(j<c) break;
		}
	}
	if(i==r && j==c) return true;
	if(ans[x][y]=='#') 
		if(!replace(x,y)) return false;
	if(y<c-1)
		return solve(x,y+1);
	else if(y==c-1)
		return solve(x+1,0);
}
int main() 
{	
	int tc;
	scanf("%d",&tc);
	for(int t=0;t<tc;t++)
	{
		scanf(" %d %d ",&r,&c);
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
			{
				scanf(" %c ",&a[i][j]);
				ans[i][j]=a[i][j];
			}
		bool b=solve(0,0);
		printf("Case #%d:\n",t+1);
		if(!b) 
			printf("Impossible\n");
		else
		{
			for(int i=0;i<r;i++)
			{
				for(int j=0;j<c;j++)
					printf("%c",ans[i][j]);
				printf("\n");
			}
		}
	}
	return 0;
}
