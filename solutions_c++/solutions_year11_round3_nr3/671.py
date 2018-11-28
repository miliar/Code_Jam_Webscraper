//============================================================================
// Name        : gcj_b.cpp
// Author      : yb
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#define ll long long
#define _clr(a) memset(a,0,sizeof(a));
#define FOR(i,x,n) for(int i=x;i<n;i++)
#define max(a,b) a>b?a:b
#define min(a,b) a<b?a:b
#define abs(a) a>0?a:a*-1
#define re return
#define sqr(x) ((x) * (x))
#define inf 268435456;
using namespace std;
const double eps=1e-10;
const double pi=acos(-1);
//ll time;
//int l,c,n;
//int a[100005];
int a[105];
int main()
{
	int cas=1,t,n,i,j;
	//freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		//scanf("%d %lld %d %d",&l,&time,&n,&c);
		scanf("%d",&n);
		int l,r;
		scanf("%d %d",&l,&r);
		int ans=-1;
		for(i=0;i<n;i++)scanf("%d",&a[i]);
		for(i=l;i<=r&&ans==-1;i++)
		{
			//i=10;
			for(j=0;j<n;j++)
			{
				if((i%a[j])&&(a[j]%i)){break;}
			}
			if(j==n)ans=i;
		}
		//printf("Case #%d:\n",cas++);
		printf("Case #%d: ",cas++);
		if(ans==-1)puts("NO");
		else printf("%d\n",ans);
		//puts("");
	}
	re 0;
}
