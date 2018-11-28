#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

struct Node
{
	double x,y,r;
}list[3];
int n;

double Cal(Node p,Node q)
{
	double d=sqrt( (p.x-q.x)*(p.x-q.x) + (p.y-q.y)*(p.y-q.y) );
	return (d+p.r+q.r)/2.0;
}
double solve()
{
	double ans,p,q;
	double Min;
	int i,j,k;
	if(n==1) return list[0].r;
	if(n==2)
	{
		ans=list[0].r;
		if(ans<list[1].r) ans=list[1].r;
		return ans;
	}
	Min=999999;
	ans=list[0].r; p=Cal(list[1],list[2]); q=ans>p?ans:p; if(q<Min) Min=q;
	ans=list[1].r; p=Cal(list[0],list[2]); q=ans>p?ans:p; if(q<Min) Min=q;
	ans=list[2].r; p=Cal(list[0],list[1]); q=ans>p?ans:p; if(q<Min) Min=q;
	return Min;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ca,T;
	int i;
	scanf("%d",&T);
	for(ca=1; ca<=T; ca++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%lf%lf%lf",&list[i].x,&list[i].y,&list[i].r);
		printf("Case #%d: %.6lf\n",ca,solve());
	}

	return 0;
}