//============================================================================
// Name        : gcj2012a.cpp
// Author      : yb
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#define inf 1<<25;
#define max(a,b) ((a)>(b)?(a):(b));
#define min(a,b) ((a)>(b)?(a):(b));
#define sqr(x) ((x)*(x));
#define _clr(a,b) (memset((a),(b),sizeof((a))));
#define print(x) (printf("Case #%d: ",(x)++));
using namespace std;

int a[2000005][10];
int vis[2000005];
int judge(int i)
{
	if(i>=1000000)return 1000000;
	if(i>=100000)return 100000;
	if(i>=10000)return 10000;
	if(i>=1000)return 1000;
	if(i>=100)return 100;
	if(i>=10)return 10;
	return 1;
}

void get()
{
	_clr(a,0);
	for(int i=10;i<2000005;i++)
	{
		int temp=i,j=0,flag=1,ind;
		ind=judge(i);
		while(flag)
		{
			//printf("1");
			int val=temp%10;
			temp=temp/10+val*ind;
			if(temp==i){flag=0;break;}
			if(val&&temp>i)a[i][j++]=temp;
		}
	}
}

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	_clr(vis,0);
	get();
	int l,r,i,j;
	int txt,cnt,cas=1;
	scanf("%d",&txt);

	while(txt--)
	{
		print(cas);cnt=0;
		scanf("%d %d",&l,&r);
		if(r<10){printf("0\n");continue;}
		_clr(vis,0);
		for(i=l;i<=r;i++)
		{
			if(!vis[i])
			{
				for(j=0;a[i][j];j++)
					if(a[i][j]>=l&&a[i][j]<=r){cnt++;}
			}
		}
		printf("%d\n",cnt);
	}
	return 0;
}
