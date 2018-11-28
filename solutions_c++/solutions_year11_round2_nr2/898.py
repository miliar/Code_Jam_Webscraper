#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
#include<cmath>
#include<vector>
#define MAXL 210
#define INF 1000000000.0
using namespace std;

int main()
{
	int T;
	int t = 0;
	int i,j,C,D;
	int p,v;
	double now;
	double local[MAXL][2];
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d %d",&C,&D);
		for(i=0;i<C;i++)
		{
			scanf("%d %d",&p,&v);
			local[i][0] = (double)p;
			local[i][1] = (double)v;
		}
		now = local[0][0];
		double max = -INF;
		double min = INF;
		for(i=0;i<C;i++)
		{
			if(local[i][0] - now >= D)
				now = local[i][0];
			for(j=0;j<local[i][1];j++)
			{	
				if(local[i][0] - now > max)
					max = local[i][0] - now;
				if(local[i][0] - now < min)
					min = local[i][0] - now;
				now += D;
			}
		}
		if(min != max)
			max =  ((max-min)/2);
		printf("Case #%d: %lf\n", ++t, fabs(max));
	}
	return 0;
}
