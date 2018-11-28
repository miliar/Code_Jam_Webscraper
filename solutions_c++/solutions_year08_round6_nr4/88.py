#include <iostream>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <vector>
using namespace std;

#define maxn 10
int n,m;

bool b[maxn][maxn], a[maxn][maxn];

int c[maxn];
bool f[maxn];

bool solve(int y)
{
	int i,j;
	if(y==m)
	{
		for(i=1;i<=m;i++)
			for(j=1;j<=m;j++)
			{
				if(b[i][j]!=a[c[i]][c[j]])
					return false;
			}
		return true;
	}
	for(i=1;i<=n;i++)
	{
		if(!f[i])
		{
			f[i]=true;
			c[y+1]=i;
			if(solve(y+1))
				return true;
			f[i]=false;
		}
	}
	return false;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	//freopen("lin.txt","r",stdin);
	//freopen("lout.txt","w",stdout);

	int cases,casenum;
	bool ff;
	scanf("%d",&cases);
	for(casenum=1;casenum<=cases;casenum++)
	{
		printf("Case #%d: ",casenum);

		int i,x,y;

		scanf("%d",&n);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));


		for(i=1;i<n;i++)
		{
			scanf("%d%d",&x,&y);
			a[x][y]=a[y][x]=true;
		}		

		scanf("%d",&m);
		for(i=1;i<m;i++)
		{
			scanf("%d%d",&x,&y);
			b[x][y]=b[y][x]=true;
		}
		memset(f,0,sizeof(f));
		if(solve(0))
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}
