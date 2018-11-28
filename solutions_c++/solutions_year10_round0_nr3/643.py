#include <cstdio>

long long seen[1000];
long long val[1000];
long long g[1000];
long long r, k, n;

int main()
{
	int t;
	int i;
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		long long loopsize;
		long long preloopsize;
		long long loopval = 0;
		long long preloopval = 0;
		long long j, l;
		long long curr;
		long long onride;
		scanf("%lld %lld %lld", &r, &k, &n);
		for (j = 0; j < n; j++)
		{
			scanf("%lld", &g[j]);
			seen[j] = 0;
		}
		curr = 0;
		for (j = 0; j < r && !seen[curr%n]; j++)
		{
			seen[curr%n] = j+1;
			val[curr%n] = preloopval;
			onride = 0;
			for (l = 0; l < n && onride + g[(curr+l)%n] <= k; l++)
				onride+=g[(curr+l)%n];
			preloopval+=onride;
			curr+=l;
		}
		if (j == r) 
		{
			printf("Case #%d: %lld\n", i+1, preloopval);
			continue;
		}
		loopval=preloopval-val[curr%n];
		loopsize = j+1-seen[curr%n];
		preloopval = val[curr%n];
		preloopsize = seen[curr%n]-1;
		long long ans = 0;
		ans+=preloopval;
		ans+=(r - preloopsize) / loopsize * loopval;
		for (j = 0; j < (r-preloopsize) % loopsize; j++)
		{
			onride = 0;
			for (l = 0; l < n && onride + g[(curr+l)%n] <= k; l++)
				onride+=g[(curr+l)%n];
			ans+=onride;
			curr+=l;
		}
		printf("Case #%d: %lld\n", i+1, ans);
		//printf("%lld %lld %lld %lld\n", preloopval, preloopsize, loopval, loopsize);
	}
}