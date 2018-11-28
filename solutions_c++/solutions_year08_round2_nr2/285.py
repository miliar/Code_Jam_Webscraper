#include <stdio.h>
#include <string.h>

using namespace std;

bool v[1000010];
long long prime[100000], cnt, r[1000010];

void ciur();
long long f(long long);

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	long long a, b, p, div, i, j, t, test;
	long long nr, first, sol;
	scanf("%lld", &t);

	ciur();
	memset(v, 0, sizeof(v));

	for(test = 1; test <= t; ++test)
	{
		scanf("%lld %lld %lld", &a, &b, &p);
		for(i = a; i <= b; ++i)
		{
			r[i - a] = i - a;
		}
		for(div = 1; prime[div] < p; ++div);
		
		do
		{
			first = ((a - 1) / prime[div] + 1) * prime[div];
			for(i = first; i <= b; i += prime[div], ++nr)
			{
				if(f(i - a) != f(first - a))
				{
					if(r[i - a] > r[first - a])
						r[r[i - a]] = r[first - a];
					else
						r[r[first - a]] = r[i - a];
				}
			}
			++div;
		}
		while(prime[div] != 0 && prime[div] <= b - a);
		sol = 0;
		memset(v, 0, sizeof(v));
		for(i = 0; i <= b - a; ++i)
		{
			(void) f(i);
		//	printf("%lld %lld\n", i + a, r[i] + a);
			if(!v[r[i]])
			{
				++sol;
				v[r[i]] = 1;
			}
		}
		printf("Case #%lld: %lld\n", test, sol);
	}

	return 0;
}

void ciur()
{
	int i, j;

	for(i = 2; i <= 1000001; ++i)
	{
		if(!v[i])
		{
			prime[++cnt] = i;
			for(j = 2 * i; j <= 1000001; j += i)
			{
				v[j] = 1;
			}
		}
	}
}

long long f(long long nod)
{
	if(r[nod] != r[r[nod]])
	{
		r[nod] = f(r[nod]);
	}
	return r[nod];
}

