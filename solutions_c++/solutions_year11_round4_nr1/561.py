#include <stdio.h>
#include <algorithm>

using namespace std;

struct segment
{
	int s, e, w;
};

segment seg[3000];

bool cmp1(segment a, segment b)
{
	return a.s<b.s;
}

bool cmp2(segment a, segment b)
{
	return a.w<b.w;
}

int X, S, R, N;
double t;

int main()
{
	int T, cas;
	int delta, i, n;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);	
	for (cas=1; cas<=T; cas++)
	{
		scanf("%d%d%d%lf%d", &X, &S, &R, &t, &N);
		delta = R-S;
		for (i=0; i<N; i++)
		  scanf("%d%d%d", &seg[i].s, &seg[i].e, &seg[i].w);
		sort(seg, seg+N, cmp1);  
		n=N;
		if (seg[0].s>0)
		{
			seg[n].s=0;
			seg[n].e=seg[0].s;
			seg[n].w=0;
			n++;
		}
		if (seg[N-1].e<X)
		{
			seg[n].s=seg[N-1].e;
			seg[n].e=X;
			seg[n].w=0;
			n++;
		}
		
		for (i=0; i<N-1; i++)
		  if (seg[i].e<seg[i+1].s)
		  	{
		  		seg[n].s=seg[i].e;
		  		seg[n].e=seg[i+1].s;
		  		seg[n].w=0;
		  		n++;
		  	}
		sort(seg, seg+n, cmp2);  	
		double ans=0;
		for (i=0; i<n; i++)
		{
			double len=seg[i].e-seg[i].s;
			if (t>0)
			{
				double tt =	len/(double)(R+seg[i].w);
				tt = min(tt, t);
				t -= tt;
				ans+=tt;
				len -= tt*(double)(R+seg[i].w);
			} 
			ans += len/(double)(S+seg[i].w);
		}
		printf("Case #%d: %.16lf\n", cas, ans);
	}
	return 0;
}