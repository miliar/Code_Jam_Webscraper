#include <stdio.h>
#include <algorithm>

using namespace std;

struct VENDOR
{
	long long p, v;
	bool operator < (const VENDOR &o) const
	{
		return p<o.p;
	}
} v[210];

int c;
long long d;

bool can(long long sec, long long d)
{
	long long rmost=-2000000000000LL;
	int i;
	for (i=0; i<c; i++)
	{
		long long l = v[i].p-sec;
		if (l<rmost+d) l = rmost+d;
		long long r = l+d*(v[i].v-1);
		if (v[i].p+sec<r) return false;
		rmost = r;  		
	}
	return true;
}

int main()
{
	long long l, r, mid;
	int T, cas, i;

	scanf("%d", &T);
	for (cas=1; cas<=T; cas++)
	{
		scanf("%d%I64d", &c, &d);
		for (i=0; i<c; i++)
		{
		  scanf("%I64d%I64d", &v[i].p, &v[i].v);
		  v[i].p*=2;
		}
		sort(v, v+c);
		l = 0; 
		r = 2000000000000LL;
		while (l<=r)
		{
			mid = (l+r)/2;
			if (can(mid, d*2)) r = mid-1;
			else l = mid+1;
		}
		printf("Case #%d: %.1lf\n", cas, (double)l/2);
	}
	return 0;
}
/*
1
1 1000000
0 1000000

*/