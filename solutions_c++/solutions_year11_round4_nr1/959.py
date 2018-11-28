#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cmath>
using namespace std;

struct point
{
	double l;
	double w;
};

point node[1005];

bool comp(point a,point b)
{
	return a.w<b.w;
}

int main()
{
	freopen("e:\\A-small.in", "r", stdin);	freopen("e:\\A-small.out", "w", stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		double X,S,R,t;
		int N;
		scanf("%lf%lf%lf%lf%d",&X,&S,&R,&t,&N);
		for(int j=1;j<=N;j++)
		{
			double B,E;
			scanf("%lf%lf%lf",&B,&E,&node[j].w);
			node[j].l=E-B;
			X=X-node[j].l;
		}
		node[0].l=X;
		node[0].w=0;
		sort(node,node+N+1,comp);
		double res=0.0;
		for(int j=0;j<=N;j++)
		{
			double tn=node[j].l/(R+node[j].w);
			if(tn > t)
			{
				res=res+(node[j].l - t*(R+node[j].w))/(node[j].w+S)+t;
				t=0;
				continue;
			}
			res=res+tn;
			t=t-tn;
		}
		printf("Case #%d: %lf\n",i+1,res);
		
	}
	return 0;
}