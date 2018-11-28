#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>

using namespace std;

#define MAX 11000

int mark[MAX];
int d[MAX];
int l[MAX];
int v[MAX];
int D;
int n;

int dijkstra()
{
	for(int i=0; i<=n; ++i)
	{
		mark[i] = 0;
		v[i] = -1;
	}
	v[0] = d[0];
	l[n] = 1;
	d[n++] = D;

	int marked = 1;

	while(marked && v[n-1] <0)
	{
		marked = 0;
		int mdist = -1;
		int mi = -1;
		for(int i=0; i<n; ++i)
			if(!mark[i] && v[i] > mdist)
			{
				mdist = v[i];
				mi = i ;
			}
		if(mi < 0)
			break;
		marked = 1;

		int now = mi;
		mark[now] = 1;

		for(int i=0; i<n; ++i)
			if(abs(d[now] - d[i]) <= v[now] && v[i] < min(l[i],abs(d[now]-d[i])))
				v[i] =  min(l[i],abs(d[now]-d[i]));
	}
	if(v[n-1] < 0)
		return 0;
	return 1;
}

int main()
{
	int t;

	scanf("%d",&t);
	for(int tcnt = 1; tcnt <= t; ++tcnt)
	{
		scanf("%d",&n);
		for(int i=0; i<n; ++i)
			scanf("%d %d",&d[i], &l[i]);
		scanf("%d",&D);

		printf("Case #%d: %s\n",tcnt,dijkstra()?"YES":"NO");
	}
	return 0;
}





