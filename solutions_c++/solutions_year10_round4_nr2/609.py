// GCJ 2010 2R
// B. WorldCup

#include <stdio.h>

int n, N;
int miss[1024];

int go(int h, int l, int r)
{
	if(l == r)
		return 0;

	int mid = (l + r) / 2;
	int cost = 0;

	for(int i=l; i<=r; ++i)
	{
		if(h > miss[i]) {
			cost = 1;
			break;
		}
	}
	
	return cost + go(h-1, l, mid) + go(h-1, mid + 1, r);
}

int main()
{
	int T, tt;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);

	scanf("%d", &T);
	for(tt=1; tt<=T; ++tt)
	{
		scanf("%d", &n);
		N = 1<<n;
		for(int i=0; i<N; ++i)
			scanf("%d", &miss[i]);
		for(int gs = N/2; gs >= 1; gs /= 2)
		{
			for(int q=0; q<gs; ++q)
				scanf("%*d");
		}
		printf("Case #%d: %d\n", tt, go(n, 0, N-1) );
	}
	return 0;
}