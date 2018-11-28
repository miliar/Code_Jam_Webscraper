#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
using namespace std;

int a[2000];
int b[100][2000];
int c[100][2000];

void solve()
{
	int n;
	scanf("%d",&n);
	int m=1<<n;
	for(int i=0;i<m;i++) scanf("%d",&a[i]);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<(1<<(n-i-1));j++)
		{
			scanf("%d",&b[i][j]);
		}
	}

	memset(c,0,sizeof(c));
	for(int i=0;i<m;i++)
	{
		int t=n-a[i]; //要看几场
		int x=n-1;
		while(t--)
		{
			c[x][i>>(x+1)] = 1;
			x--;
		}
	}
	int flag=0;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<(1<<(n-i-1));j++)
		{
			if(c[i][j]) flag ++;
		}
	}


	printf("%d\n",flag);
}
int price(int x,int y)
{
	return price(x-1,y*2) + price(x-1,y*2+1);
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
