#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <iostream>

#define LL long long

using namespace std;

LL par[1001];
pair<LL, LL> best[1001];

LL calc1(LL res, LL i, LL C, LL N, LL L)
{
	LL dist[1001];
	memset(dist, 0, sizeof dist);
	res += par[i%C]*2;
	// calc distributions
	for (LL j = i+1; j < N; ++j)
		dist[j%C]++;
	for (LL j = C-1; j >= 0 && L > 0; --j)
	{
		LL times = dist[best[j].second];
		times = min(times, L);
		L -= times;
		res += times*best[j].first;
		dist[best[j].second]-=times;
	}
	for (LL j = 0; j < C; ++j)
		res += dist[j]*par[j]*2;
	return res;
}

LL calc2(LL res, LL i, LL C, LL N, LL L, LL t)
{
	LL dist[1001];
	memset(dist, 0, sizeof dist);
	--L;
	res += t;
	res += par[i%C]-t/2;
	// calc distributions
	for (LL j = i+1; j < N; ++j)
		dist[j%C]++;
	for (LL j = C-1; j >= 0 && L > 0; --j)
	{
		LL times = dist[best[j].second];
		times = min(times, L);
		L -= times;
		res += times*best[j].first;
		dist[best[j].second]-=times;
	}
	for (LL j = 0; j < C; ++j)
		res += dist[j]*par[j]*2;
	return res;
}

int main()
{
	int Q;
	scanf("%d", &Q);
	
	for (int q = 1; q <= Q; ++q)
	{
		printf("Case #%d: ", q);
		
		LL L, t, N, C;
		scanf("%lld%lld%lld%lld", &L, &t, &N, &C);
		for (LL i = 0; i < C; ++i)
		{
			scanf("%lld", &par[i]);
			best[i].first = par[i];
			best[i].second = i;
		}
		sort(best, best+C);
			
		LL res = 0;
		bool boosted = false;
			
		for (LL i = 0; i < N; ++i)
		{
			if (L == 0)
			{
				res += par[i%C]*2;
				continue;
			}
			LL d = par[i%C]*2;
			if (d >= t)
			{
				boosted = true;
				LL f = calc1(res, i, C, N, L);
				LL s = calc2(res, i, C, N, L, t);
				res = min(f, s);
				break;
			}
			else
			{
				res += par[i%C]*2;
				t -= par[i%C]*2;
			}
		}
		
		printf("%lld\n", res);
	}
	
	return 0;
}

