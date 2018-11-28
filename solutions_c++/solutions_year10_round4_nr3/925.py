#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
using namespace std;

int a[110][110];
int b[110][110];

void solve()
{
	memset(a,0,sizeof(a));
	int x1,x2,y1,y2;
	int n;
	scanf("%d",&n);
	while(n--)
	{
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		for(int i=x1;i<=x2;i++) for(int j=y1;j<=y2;j++) a[i][j]=1;
	}
	n=0;
	while(1)
	{
		n++;
		memcpy(b,a,sizeof(a));
		memset(a,0,sizeof(a));
		int flag = 0;
		for(int i=1;i<=100;i++)for(int j=1;j<=100;j++)
		{
			if(b[i][j])
			{
				if(b[i-1][j] || b[i][j-1])
				{
					a[i][j]=1;
					flag++;
				}
			}
			else
			{
				if(b[i-1][j] && b[i][j-1])
				{
					a[i][j]=1;
					flag++;
				}
			}
		}
		/*
		for(int i=1;i<=6;i++)
		{
			for(int j=1;j<=6;j++) printf("%d",a[j][i]);
			puts("");
		}
		puts("");
		*/
		if(!flag)
			break;
	}
	printf("%d\n",n);
}
int main()
{


	int Ti,T;
	scanf("%d",&T);
	for(Ti = 1; Ti <= T; Ti++)
	{
		printf("Case #%d: ",Ti);
		solve();
	}
}
