#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
char a[100][100],b[100][100];
int main()
{
	int repeat,i,j,n,m,ri=1,flag;
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);

	scanf("%d",&repeat);
	while(repeat--)
	{
		flag=0;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			scanf("%s",a[i]);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if( a[i][j]=='#')
				{
					if( i==n-1 || j==m-1 )
						flag=1;
					
					else if(a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#')
					{
						b[i][j]=b[i+1][j+1]='/';
						b[i][j+1]=b[i+1][j]='\\';
						a[i][j]=a[i+1][j+1]='r';
						a[i][j+1]=a[i+1][j]='r';
					}
					else flag=1;
				}
				else if(a[i][j]=='r') continue;
				else b[i][j]=a[i][j];
			}
			b[i][j]=0;
		}
		printf("Case #%d:\n",ri++);
		if( flag ) puts("Impossible");
		else
		{
			for(i=0;i<n;i++)
				printf("%s\n",b[i]);
		}
	}
	return 0;
}