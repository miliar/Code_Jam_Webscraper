#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

int a[102][102];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t,tt;
	int i,j,ii,jj;
	int x1,x2,y1,y2;
	int r,num,ans;
	scanf("%d",&t);
	for (tt=0; tt<t; ++tt)
	{
		scanf("%d",&r);
		memset(a,0,sizeof(a));
		for (i=0; i<r; ++i)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (ii=x1; ii<=x2; ++ii)
				for (jj=y1; jj<=y2; ++jj)
					a[ii][jj]=1;
		}
		num=0;
		for (i=0; i<=100; ++i)
			for (j=0; j<=100; ++j)
				num+=a[i][j];
	   ans=0;
		while(num>0)
		{
			ans++;
			for (i=100; i>0; --i)
				for (j=100; j>0; --j)
					if (a[i][j]==0 && a[i-1][j]==1 && a[i][j-1]==1)
					{
						num++;
						a[i][j]=1;
					}
					else if (a[i][j]==1 && a[i-1][j]==0 && a[i][j-1]==0)
					{
						num--;
						a[i][j]=0;
					}
		}
		printf("Case #%d: %d\n",tt+1,ans);
	}
	return 0;
}