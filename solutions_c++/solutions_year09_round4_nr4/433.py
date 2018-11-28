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
int n;
double ans;
double x[5];
double y[5];
double r[5];
double cal(double x,double y)
{
	return sqrt(x*x+y*y);
}
int main()
{
	freopen("e:\\1.in","r",stdin);
	freopen("e:\\1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
		}
		if(n==1) ans=r[0];
		else if(n==2) ans=max(r[0],r[1]);
		else 
		{
			ans=100000000;
			get_min(ans,cal(x[0]-x[1],y[0]-y[1])+r[0]+r[1]);
			get_min(ans,cal(x[0]-x[2],y[0]-y[2])+r[0]+r[2]);
			get_min(ans,cal(x[2]-x[1],y[2]-y[1])+r[2]+r[1]);
			ans=ans/2;
		}
		printf("%.6f\n",ans);
	}
	return 0;
}
