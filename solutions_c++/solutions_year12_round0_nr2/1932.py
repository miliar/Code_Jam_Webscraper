//============================================================================
// Name        : gcj2012b.cpp
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
int a[1005];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("2.out","w",stdout);
	int txt,n,s,p,l,x,cnt,i,cas=1,temp;
	scanf("%d",&txt);
	while(txt--)
	{
		l=0;cnt=0;
		scanf("%d %d %d",&n,&s,&p);
		for(i=0;i<n;i++)
		{
			scanf("%d",&x);
			a[l++]=x;
		}
		sort(a,a+l);
		for(i=l-1;i>=0;i--)
		{
			temp=a[i]/3;
			if(a[i]%3)temp+=1;
			if(temp>=p)cnt++;
			else break;
		}
		for(int j=0;j<s;j++)
		{
			if(!a[i])break;
			temp=a[i]/3+1;
			if(a[i]%3==2)temp++;
			if(temp>=p){cnt++;i--;}
			else break;
		}
		print(cas);
		printf("%d\n",cnt);
	}
	return 0;
}
