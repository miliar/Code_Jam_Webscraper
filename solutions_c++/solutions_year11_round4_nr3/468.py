/* by Ashar Fuadi [fushar] */

#include <cstdio>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define REPE(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)
#define RESET(c,v) memset(c, v, sizeof(c))

#define pb push_back
#define mp make_pair
#define DEBUG 1
#define PRINT(x...) DEBUG && printf(x)

int T, N, ans[1001];
int mi[1001], ma[1001];
int f[1001];

bool isPrime(int n)
{
	if (n == 2) return true;
	for (int i = 2; i < n; i++)
		if (n%i == 0)
			return false;
	return true;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	//freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	
	for (int n = 2; n <= 1000; n++)
	{
		mi[n] = mi[n-1];
		if (isPrime(n))
			mi[n]++;
	}
	ma[1] = 1;
	for (int n = 2; n <= 1000; n++)
	{
		int x = n;
		int call = 0;
		for (int i = 2; i*i <= x; i++) if (x%i == 0)
		{
			int c = 0;
			while (x%i == 0)
			{
				c++;
				x /= i;
			}
			
			if (c > f[i])
			{
				call = 1;
				f[i] = c;
			}
		}
		
		if (x > 1)
		{
			if (1 > f[x])
			{
				call = 1;
				f[x] = 1;
			}
		}
		ma[n] = call + ma[n-1];
	}
	
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d", &N);
		printf("Case #%d: %d\n", tc+1, N == 1 ? 0 : ma[N]-mi[N]);
	}
}
