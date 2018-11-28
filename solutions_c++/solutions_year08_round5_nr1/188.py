const double pi=3.1415926535897932, e=2.7182818284590452;
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:160000000")
#include <cstdio>
#include <cmath>
#include <complex>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

int N,T,x,y,dir,k,cnt;
int a[7000][7000];
char c[100];
int ll[7000],rr[7000],uu[7000],dd[7000];

void Rec(int x, int y)
{
	if (a[x+3500][y+3500]==0 && labs(x)<222 && labs(y)<222)
	{
		a[x+3500][y+3500]=-1;
		Rec(x+1,y);
		Rec(x-1,y);
		Rec(x,y+1);
		Rec(x,y-1);
	}
}

int n1,n2;

void reg(int x)
{
	if (x==1)
		++n1;
	if (x==-2)
		++n2;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d",&N);
	for (int ii=1; ii<=N; ++ii)
	{
		scanf("%d",&T);
		x=y=dir=0;
		memset(a, 0, sizeof a);
		a[x+3500][y+3500]=1;
		for (int i=0; i<T; ++i)
		{
			scanf("%s %d ", c, &k);
			for (int jj=0; jj<k; ++jj)
				for (int i=0; i<(int)strlen(c); ++i)
				{
					if (c[i]=='L')
						dir=(dir+3)%4;
					else
					if (c[i]=='R')
						dir=(dir+1)%4;
					else
					if (c[i]=='F')
					{
						switch (dir)
						{
						case 0:
							++x;
							break;
						case 1:
							--y;
							break;
						case 2:
							--x;
							break;
						case 3:
							++y;
							break;
						}
						a[x+3500][y+3500]=1;
						switch (dir)
						{
						case 0:
							++x;
							break;
						case 1:
							--y;
							break;
						case 2:
							--x;
							break;
						case 3:
							++y;
							break;
						}
						a[x+3500][y+3500]=1;
					}
				}
		}
		// flood
		Rec(-210,-210);
		// fill ll, rr, uu, dd
		for (int i=0; i<7000; ++i)
			ll[i]=10000,
			rr[i]=-10000,
			uu[i]=10000,
			dd[i]=-10000;
		for (int x=-205; x<=205; ++x)
			for (int y=-205; y<=205; ++y)
				if (a[x+3500][y+3500]==1)
				{
					if (x==-12 && y==-6)
						printf("");
					ll[y+3500]=min(ll[y+3500],x);
					rr[y+3500]=max(rr[y+3500],x);
					uu[x+3500]=min(uu[x+3500],y);
					dd[x+3500]=max(dd[x+3500],y);
				}
		for (int x=-205; x<=205; ++x)
			for (int y=-205; y<=205; ++y)
			{
				if (x==-6 && y==-6)
					printf("");
				if (a[x+3500][y+3500]==-1 && (x>=ll[y+3500] && x<=rr[y+3500] || y>=uu[x+3500] && y<=dd[x+3500]))
					a[x+3500][y+3500]=-2;
			}
		cnt=0;
		for (int x=-205; x<=205; ++x)
			for (int y=-205; y<=205; ++y)
			{
				if (x==-6 && y==-6)
					printf("");
				n1=n2=0;
				reg(a[x+3500][y+3500]);
				reg(a[x+3501][y+3500]);
				reg(a[x+3500][y+3501]);
				reg(a[x+3501][y+3501]);
				if (n1+n2==4 && n2)
					++cnt;
			}
		printf("Case #%d: %d\n",ii,cnt/4);
	}
	return 0;
}
