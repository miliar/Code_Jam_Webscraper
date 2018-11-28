#include "stdafx.h"
// iii.cpp : Defines the entry point for the console application.
//0-1±³°ü

//#include "stdafx.h"
#include <algorithm>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string.h>
#include<vector>
using namespace std;

char ditu[55][55];
int n,r;
bool check(bool red)
{
	int posx,posy;
	int cnt,tp;
	if(red)
	{
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<n;++j)
			{
				if(i<=n-r)
				{
				cnt = 0;
				tp = r;
				posx = i;posy = j;
				while(tp--)
				{
					if(ditu[posx][posy] == 'R') cnt++;
					posx++;
				}
				if(cnt == r) return true;
				}
				if( j<=n-r)
				{
				cnt = 0;
				tp = r;
				posx = i;posy = j;
				while(tp--)
				{
					if(ditu[posx][posy] == 'R') cnt++;
					posy++;
				}
				if(cnt == r) return true;
				}

				if(i<=n-r &&j<=n-r)
				{
				cnt = 0;
				tp = r;
				posx = i;posy = j;
				while(tp--)
				{
					if(ditu[posx][posy] == 'R') cnt++;
					posx++;posy++;
				}
				if(cnt == r) return true;
				}
				if(i>=r-1)
				{
					cnt = 0;
					tp = r;
					posx = i;posy = j;
					while(tp--)
					{
						if(ditu[posx][posy] == 'R') cnt++;
						posx--;posy++;
					}
					if(cnt == r) return true;
				}
			}
		}
		return false;
	}
	else
	{
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<n;++j)
			{
				if(i<=n-r)
				{
				cnt = 0;
				tp = r;
				posx = i;posy = j;
				while(tp--)
				{
					if(ditu[posx][posy] == 'B') cnt++;
					posx++;
				}
				if(cnt == r) return true;
				}
				if( j<=n-r)
				{
				cnt = 0;
				tp = r;
				posx = i;posy = j;
				while(tp--)
				{
					if(ditu[posx][posy] == 'B') cnt++;
					posy++;
				}
				if(cnt == r) return true;
				}

				if(i<=n-r &&j<=n-r)
				{
					cnt = 0;
					tp = r;
					posx = i;posy = j;
					while(tp--)
					{
						if(ditu[posx][posy] == 'B') cnt++;
						posx++;posy++;
					}
					if(cnt == r) return true;
				}
				if(i>=r-1)
				{
					cnt = 0;
					tp = r;
					posx = i;posy = j;
					while(tp--)
					{
						if(ditu[posx][posy] == 'B') cnt++;
						posx--;posy++;
					}
					if(cnt == r) return true;
				}
			}
		}
		return false;
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int x=1;x<=t;++x)
	{
		scanf("%d%d",&n,&r);
		for(int i=0;i<n;++i)
			scanf("%s",ditu[i]);
		for(int j=n-2;j>=0;--j)
		{
			for(int i=0;i<n;++i)
			{
				if(ditu[i][j] != '.')
				{
					int pos = j+1;
					while(pos <n && ditu[i][pos] == '.')
					{
						swap(ditu[i][pos] , ditu[i][pos-1]);
						pos ++;
					}
				}
			}
		}
		bool red = check(1);
		bool blue = check(0);
		printf("Case #%d: ",x);
		if(red && !blue)
		{printf("Red\n");}
		else if(blue&&!red)
		{printf("Blue\n");}
		else if(red&&blue)
		{printf("Both\n");}
		else printf("Neither\n");
	}
	return 0;
}