#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <algorithm>

using namespace std;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t,i,j,r,c;
	char s[55];
	int a[55][55];
	scanf("%d",&t);
	bool flag;
	for (int cnt=1;cnt<=t;cnt++)
	{
		scanf("%d%d",&r,&c);
		for (i=0;i<r;i++)
		{
			scanf("%s",s);
			for (j=0;j<c;j++)
				if (s[j]=='.')
					a[i][j]=0;
				else
					a[i][j]=1;
		}
		for (i=0;i<r;i++) a[i][c]=0;
		for (j=0;j<c;j++) a[r][j]=0;
		flag=true;
		for (i=0;i<r;i++)
			for (j=0;j<c;j++)
			{
				if (a[i][j]==1)
				{
					a[i][j]=2;
				if (a[i][j+1]==1) a[i][j+1]=3;
				else flag=false;
				if (a[i+1][j]==1) a[i+1][j]=3;
				else flag=false;
				if (a[i+1][j+1]==1) a[i+1][j+1]=2;
				else flag=false;
				}
			}
			printf("Case #%d:\n",cnt);
		if (flag)
			for (i=0;i<r;i++)
			{
				for (j=0;j<c;j++)
				{
					if (a[i][j]==0) printf(".");
					else
					if (a[i][j]==2) printf("/");
					else
					printf("\\");
				}
				printf("\n");
			}
		else 
			printf("Impossible\n");
	}
	return 0;
}