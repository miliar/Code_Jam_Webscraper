#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
using namespace std;

bool map[105][105],save[105][105];
void solve()
{
	int n,i,j,X1,Y1,X2,Y2;
	scanf("%d",&n);
	memset(map,false,sizeof(map));
	while(n--)
	{
		scanf("%d%d%d%d",&X1,&Y1,&X2,&Y2);
		for(i=X1;i<=X2;i++)
			for(j=Y1;j<=Y2;j++)
				map[i][j]=true;
	}
	int days=0;
	bool flag=true;
	while(flag)
	{
		flag=false;
		for(i=1;i<=100;i++)
			for(j=1;j<=100;j++)
			{
				if(map[i][j])
				{
					if(map[i-1][j]||map[i][j-1])
						save[i][j]=true;
					else
						save[i][j]=false;
				}
				else
				{
					if(map[i-1][j]&&map[i][j-1])
						save[i][j]=true;
					else
						save[i][j]=false;
				}
				if(save[i][j])
					flag=true;
			}
		for(i=1;i<=100;i++)
			for(j=1;j<=100;j++)
				map[i][j]=save[i][j];
		days++;
	}
	printf("%d\n",days);
}
int main()
{
	freopen("D:\\C-small-attempt0.in","r",stdin);
	freopen("D:\\C-small-attempt0.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		solve();
	}
}