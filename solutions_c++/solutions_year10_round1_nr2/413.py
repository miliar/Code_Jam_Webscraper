#include "stdafx.h"
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <algorithm>
#include <iostream>
#define PI 3.14159265358979323846264338327950288
#define _clr(a,b) memset(a,b,sizeof(a))
template<class T> T _abs(T a)
{ if(a<0) return -a;return a;}
template<class T> void get_min(T& a,T b)
{ if(a>b) a=b;}
template<class T> void get_max(T& a,T b)
{ if(a<b) a=b;}
using namespace std;
int a[105];
int D,I,M,N;
int minCost(int a,int b)
{
	int t;
	if(_abs(a-b)<=M) return 0;
	else t=_abs(a-b)-M;
	int m=min(D,t);
	if(M!=0) 
	{
		int p=_abs(a-b);
		int k=(p/M)*I;
		if(p%M==0) k-=I;
		else
		{
			k=min(k-I+p%M,k);
		}
		m=min(k,m);
	}
	return m;
}
int main()
{
	freopen("e:\\B-small-attempt5.in","r",stdin);
	//freopen("e:\\1.in","r",stdin);
	freopen("e:\\1.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d%d%d%d",&D,&I,&M,&N);
		for(int i=0;i<N;i++)
		{
			scanf("%d",&a[i]);
		}
		int ans=2*D;
		if(N==3)
		{
			ans=minCost(a[0],a[2])+D;
			get_min(ans,minCost(a[1],a[2])+D);
			get_min(ans,minCost(a[0],a[1])+D);
			for(int i=0;i<=255;i++)
			{
				get_min(ans,minCost(i,a[0])+minCost(a[2],i)+_abs(a[1]-i));
			}
		}
		else if(N==2)
		{
			ans=minCost(a[1],a[0]);
		}
		else ans=0;
		printf("%d\n",ans);
	}
	return 0;
}
