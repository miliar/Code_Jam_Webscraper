#include "StdAfx.h"
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <algorithm>
#define eps 1e-12
#define MAX 1000000000
using namespace std;

struct node
{
	int x,y;
	double w;
};
node a[3000];

int mark[1000001];

int cmp(const void *a,const void *b)
{
	struct node *aa=(node *) a;
	struct node *bb=(node *) b;
	return aa->w>bb->w?1:-1;
}
int main()
{
	
	freopen("out.txt","w",stdout);
	int repeat,i,j,k;
	int cases=1;
	cin>>repeat;
	double l,s,r,t,ans,T,L;
	int n;
	while(repeat--)
	{
		cin>>l>>s>>r>>t>>n;
		memset(mark,0,sizeof(mark));
		for(i=0;i<n;i++)
		{
			cin>>a[i].x>>a[i].y>>a[i].w;
			mark[a[i].x]+=1;
			mark[a[i].y]+=1;
			for(j=a[i].x+1;j<=a[i].y-1;j++)
				mark[j]=2;
		}
		printf("Case #%d: ",cases++);
		for(i=0;i<=l;i++)
		{
			if(mark[i]<=1)
			{
				if(i==0&&mark[i]==1)
					continue;
				if(i==l&&mark[i]==1)
					continue;
				for(j=i+1;j<=l;j++)
					if(mark[j]>=1)
						break;
				node ss;
				ss.x=max(0,i);
				ss.y=min(j,(int)l);
				ss.w=0;
				i=j;
				a[n++]=ss;
			}
		}
		qsort(a,n,sizeof(a[0]),cmp);
		ans=0;
		for(i=0;i<n;i++)
		{
			//cout<<a[i].x<<" "<<a[i].y<<" "<<a[i].w<<endl;
			L=a[i].y-a[i].x;
			if(t>0)
			{
				T=L/(r+a[i].w);
				if(T<t)
				{
					t-=T;
					ans+=T;
				}
				else
				{
					ans+=t;
					L-=t*(r+a[i].w);
					T=L/(s+a[i].w);
					t=0;
					ans+=T;
				}
			}
			else
			{
				T=L/(s+a[i].w);
				ans+=T;
			}
			
		}
		printf("%.7lf\n",ans);
	}
	return 0;
}