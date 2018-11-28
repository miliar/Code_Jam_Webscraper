#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i, lo, hi) for(int i = (lo); i < (hi); ++i)
#define MP make_pair
#define PB push_back

typedef long long ll;

int MAX = 1000000;
int p[1000001], psz;
bool taken[1000001];

int main()
{
	int numCases;
	scanf("%d", &numCases);

	bool sieve[1000001];
	FOR(i, 0, MAX + 1) sieve[i] = true;
	sieve[0] = sieve[1] = false;
	for(int i = 0; i * i <= MAX; ++i)
	{
		if(sieve[i])
		{
			for(int j = 2 * i; j <= MAX; j += i) sieve[j] = false;
		}
	}

	for(int i = 0; i <= MAX; ++i) if(sieve[i]) p[psz++] = i;

	FOR(tc, 1, numCases + 1)
	{
		ll A, B, P;
		scanf("%d %d %d", &A, &B, &P);
		int pos = 0;
		while(pos < psz && p[pos] < P) ++pos;
		
		int ct = 0;
		
		for(int i = 0; i < B - A + 1; ++i) taken[i] = false;
		for(int i = pos; i <= psz && p[i] <= B; ++i)
		{
			int pr = p[i];
			ll st = A / pr, end = B / pr;
			if(st * (ll)pr != A) st++;
			if(st * pr > B) continue;
			bool flag = false;
			for(ll f = st; f <= end; ++f)
			{
				ll num = f * pr;
				if(taken[num - A]) { flag = true; }
				taken[num - A] = true;
			}
			if(flag) continue;
			++ct;
		}
		for(int i = A; i <= B; ++i) if(!taken[i - A]) ++ct;
		printf("Case #%d: %d\n", tc, ct);
	}

	return 0;
}
