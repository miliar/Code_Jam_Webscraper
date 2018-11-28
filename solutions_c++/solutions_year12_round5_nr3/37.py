#include <stdio.h>
#include <assert.h>
#include <climits>
#include <utility>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

long long p[300], s[300];
long long bestPrice[300];
long long changed[300];
int len;
long long f;

const long long INF = 1000000000000000001LL;

inline long long getAdd(long long a, long long b) {
	if (a >= INF - b)
		return INF;
	return a + b;
}

inline long long getMult(long long a, long long b) {
	if (a >= (INF-1) / b + 1)
		return INF;
	return a * b;
}

long long getBestPrice(long long day) {
	if (day > changed[len-1])
		return INF;
	long long res = f;
	long long cur = 0;
	for (int i=0; i<len; ++i)
	{
		if (changed[i] >= day)
		{
			long long temp = getMult(day-cur, bestPrice[i]);
			if (temp >= INF)
				return INF;
			res = getAdd(res, temp);
			if (res >= INF)
				return INF;
			return res;
		}
		else {
			long long temp = getMult(changed[i]-cur, bestPrice[i]);
			if (temp >= INF)
				return INF;
			res = getAdd(res, temp);
			if (res >= INF)
				return INF;
			cur = changed[i];
		}
	}
	return INF;
}

int main() {
	int tc, n;
	long long m;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		scanf("%lld %lld %d", &m, &f, &n);
		priority_queue< pair<long long, long long> > Q;
		for (int i=0; i<n; ++i) {
			scanf("%lld %lld", &p[i], &s[i]);
			Q.push(make_pair(-p[i], s[i]));
		}
		long long cur = 0;
		len = 0;
		while(!Q.empty()) {
			while(!Q.empty() && Q.top().second < cur-1) {
				Q.pop();
			}
			if (Q.empty())
				break;
			changed[len] = Q.top().second + 1;
			bestPrice[len] = -Q.top().first;
			assert(len == 0 || bestPrice[len] >= bestPrice[len-1]);
			cur = changed[len] + 1;
			++len;
		}
		// try how many days it lasts by binary search
		long long lo = 0, hi = m +  1;
		while(lo < hi) {
			long long mid = (lo + hi + 1) / 2;
			long long best = INF;
			// try to divide it into chunks
			// find the biggest groups which fit into the same range of bestPrice
			for (int add=-2; add<=2; ++add)
				for (int i=0; i < len; ++i) {
					// want changed[i] * parts >= mid
					long long parts = mid / changed[i] + add;
					if (parts <= 0)
						parts = 1;
					long long size_per_part = mid / parts;
					long long how_many = mid % parts;
					long long val;
					if (how_many == 0)
					{
						val = getMult(getBestPrice(size_per_part), parts);
					}
					else {
						val = getMult(how_many, getBestPrice(size_per_part+1));
						long long temp = getMult(parts - how_many, getBestPrice(size_per_part));
						if (temp == INF)
							val = INF;
						else if (val < INF)
							val = getAdd(val, temp);
					}
					if (val < best)
						best = val;
				}
			if (best <= m) {
				lo = mid;
			}
			else
				hi = mid-1;
		}
		printf("Case #%d: %lld\n", scen, lo);
	}
	return 0;
}
