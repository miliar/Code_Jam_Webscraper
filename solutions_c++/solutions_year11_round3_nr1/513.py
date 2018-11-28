#include <iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

char smap[51][51];
int r,c,p;

bool look()
{
	int i,j,k;
	for(i=1;i<=r;i++)
		for(j=1;j<=c;j++)
		if(smap[i][j]=='#')
		{
			if(j==c || i==r) return false;
			if( !(smap[i][j+1]=='#' && smap[i+1][j]=='#' && smap[i+1][j+1]=='#') )
				return false;
			smap[i][j]='/';
			smap[i][j+1]='\\';
			smap[i+1][j]='\\';
			smap[i+1][j+1]='/';
		}
	return true;
}

void work()
{
	int i,j,k;

	scanf("%d%d",&r,&c);
	for(i=1;i<=r;i++)
	{
		scanf("\n");
		for(j=1;j<=c;j++)
		scanf("%c",&smap[i][j]);
    }
    printf("Case #%d:\n",p);
    if(look())
	{
		for(i=1;i<=r;i++)
		{
			for(j=1;j<=c;j++)
				printf("%c",smap[i][j]);
			printf("\n");
		}
    }
    else 
      printf("Impossible\n");
	
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(p=1;p<=T;p++)
		work();
	return 0;
}
