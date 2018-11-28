#include <stdafx.h>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <ctime>
#include <cassert>

using namespace std;

const long maxn=1005;

long ansx[maxn];
pair <long,long> list1[maxn];
pair <long,long> list2[maxn];
long ansy[maxn];
bool used[maxn];
long r[maxn];
long xl,yl,n;

void go(long x1,long y1,long x2,long y2)
{
	if (x1<0)
		x1=0;
	x2=min(x2,xl);
	if (x1>=x2) return;
	for (long choice=1;choice<=n;choice++) if (!used[choice])
	{
		//if ((r[choice]<=y2-y1)&&(r[choice]<=x2-x1))
		if (2*r[choice]<=y2-y1)
		{
			//ansx[choice]=x1+(double)r[choice]/2.0;
			//ansy[choice]=y1+(double)r[choice]/2.0;
			ansx[choice]=x1+r[choice];
			ansy[choice]=y1+r[choice];
			used[choice]=true;

			go(x1,y1+2*r[choice],x1+2*r[choice],y2);
			go(x1+2*r[choice],y1,x2,y2);
			break;
		}
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long tests;
	scanf("%ld",&tests);
	for (long test=1;test<=tests;test++)
	{
		long q;
		printf("Case #%ld: ",test);
		scanf("%ld%ld%ld",&n,&xl,&yl);
		for (q=1;q<=n;q++)
			scanf("%ld",&r[q]);
		sort(r+1,r+n+1);
		reverse(r+1,r+n+1);
		for (q=1;q<=n;q++)
			used[q]=false;
		long now=0;
		long amount=0;
		for (long it=1;it<=n;it++)
		{
			if (now>xl)
				break;
			used[it]=true;
			ansx[it]=now;
			ansy[it]=0;
			amount++;
			list1[amount].first=now-r[it];
			list1[amount].second=r[it];
			list2[amount].first=now+r[it];
			list2[amount].second=yl;
			//go(now-r[it],r[it],now+r[it],yl);
			now+=(r[it]+r[it+1]);
		}
		for (long it=1;it<=amount;it++)
			go(list1[it].first,list1[it].second,list2[it].first,list2[it].second);
		for (q=1;q<=n;q++)
			assert(used[q]);
		for (long j=1;j<=n;j++)
		{
			if (ansx[j]>xl)
				ansx[j]=xl;
			printf("%ld %ld ",ansx[j],ansy[j]);
		}
		printf("\n");
	}
}