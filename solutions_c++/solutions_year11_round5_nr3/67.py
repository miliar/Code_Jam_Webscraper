#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

struct T
{
	int i,j;
}a[10][10];

int n,m;
char s[10];
int i,j,k,f,ans,T,ts;
int u[10][10];

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&m);
		ans=0;
		for(i=0;i<n;i++)
		{
			scanf("%s",&s);
			for(j=0;j<m;j++)
				switch(s[j])
				{
					case '|':
						a[i][j].i=1;
						a[i][j].j=0;
						break;
					case '-':
						a[i][j].i=0;
						a[i][j].j=1;
						break;
					case '\\':
						a[i][j].i=1;
						a[i][j].j=1;
						break;
					case '/':
						a[i][j].i=-1;
						a[i][j].j=1;
						break;
				}
		}
		for(k=0;k<1<<n*m;k++)
		{
			for(i=0;i<n;i++)
				for(j=0;j<m;j++)
				{
					u[i][j]=0;
					if(k&(1<<i*m+j))
					{
						a[i][j].i=-a[i][j].i;
						a[i][j].j=-a[i][j].j;
					}
				}
			for(i=0;i<n;i++)
				for(j=0;j<m;j++)
					u[(i+a[i][j].i+n)%n][(j+a[i][j].j+m)%m]++;
			f=0;
			for(i=0;i<n;i++)
				for(j=0;j<m;j++)
					f|=u[i][j]>1;
			ans+=!f;
			for(i=0;i<n;i++)
				for(j=0;j<m;j++)
				{
					u[i][j]=0;
					if(k&(1<<i*m+j))
					{
						a[i][j].i=-a[i][j].i;
						a[i][j].j=-a[i][j].j;
					}
				}
		}
		printf("Case #%d: %d\n",++ts,ans%1000003);
	}
	return 0;
}