#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;

const int maxn = 2000001;
bool prime[maxn];
vector<int> primes;
void sieve()
{
	memset(prime, true, sizeof prime);
	prime[0] = prime[1] = false;
	int sq = sqrt(maxn + 0.0) + 1;
	for(int i = 2; i <= sq; ++i) if(prime[i])
	{
		for(int j = i * i; j < maxn; j += i)
			prime[j] = false;
	}
	for(int i = 0; i < maxn; ++i)
		if(prime[i])
			primes.pb(i);
}

int mpow(LL a, LL n, LL mod)
{
	if(n == 0) return 1 % mod;
	LL res = mpow(a, n / 2, mod);
	res *= res;
	res %= mod;
	if(n & 1)
		res *= a,
		res %= mod;
	return res;
}

struct striple
{
	int a, b, p;
	striple() { a = b = p = 1; }
	striple(int a, int b, int p) : a(a), b(b), p(p) { }
	
};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	sieve();
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int d, k;
		scanf("%d%d", &d, &k);
		vector<int> a(k);
		for(int i = 0; i < k; ++i)
			scanf("%d", &a[i]);
		bool eq = false;
		for(int i = 0; i + 1 < k; ++i)
			if(a[i] == a[i + 1])
			{
				eq = true;
			}
		int pow10 = 1;
		for(int i = 0; i < d; ++i)
			pow10 *= 10;

		if(k == 1)
		{
			printf("Case #%d: I don't know.\n", z + 1);
		} else
		{
			if(eq)
			{
				printf("Case #%d: %d\n", z + 1, a.back());
			} else
			{
				if(k == 2)
				{
					// solve me
					set<int> ex;
					/*
					
					for(int i = 0; i < primes.size(); ++i) if(primes[i] < pow10)
						for(int A = 0; A < primes[i]; ++A)
						{
							int B = (a[1] - LL(a[0]) * A) % primes[i];
							B += primes[i];
							B %= primes[i];
							int next = (A * LL(a[1]) + B) % primes[i];
							if(a[0] < primes[i] && a[1] < primes[i] && (a[0] * LL(A) + B) % primes[i] == a[1])
								ex.insert(next);
							
						}
					if(ex.size() == 1)
					{
						int s = *ex.begin();
						printf("Case #%d: %d\n", z + 1, s);
					} else
						printf("Case #%d: I don't know.\n", z + 1);
						*/
					
					vector<int> p;
					for(int i = 0; i < primes.size(); ++i)
						if(primes[i] < pow10 && a[0] < primes[i] && a[1] < primes[i])
							p.pb(primes[i]);
					if(p.size() == 1)
					{
						for(int A = 0; A < p[0]; ++A)
						{
							int B = (a[1] - a[0] * A) % p[0];
							B += p[0];
							B %= p[0];
							ex.insert((A * a[1] + B) % p[0]);
						}
						if(ex.size() == 1)
						{
							int s = *ex.begin();
							printf("Case #%d: %d\n", z + 1, s);
						} else
							printf("Case #%d: I don't know.\n", z + 1);
					} else
						printf("Case #%d: I don't know.\n", z + 1);
						
				} else
				{
					vector<striple> w;
					set<int> ex;
					for(int i = 0; i < primes.size(); ++i)
						if(primes[i] < pow10)
						{
							int p = primes[i];
							// A * (a[1] - a[0]) == a[2] - a[1] (mod p)
							// A = (a[2] - a[1]) * (a[1] - a[0])^(-1)  (mod p)
							int A = ((((a[2] - a[1] + p)) % p) * (LL)mpow((p + a[1] - a[0]) % p, p - 2, p)) % p;
							A = (A + p) % p;
							int B = (a[1] - A * a[0]) % p;
							B = (B + p) % p;
							bool fl = true;
							
							int s = a[0];
							for(int i = 0; i < a.size(); ++i)
							{
								if(a[i] != s || a[i] >= p)
								{
									fl = false;
									break;
								}
								s = (A * LL(s) + B) % p;
							}
							
							if(fl)
							{
								w.pb(striple(A, B, p));
								ex.insert(s);
							}

						}
					if(ex.size() == 1)
					{
						int s = *ex.begin();
						printf("Case #%d: %d\n", z + 1, s);
					} else
						printf("Case #%d: I don't know.\n", z + 1);
				}
			}
		}
	}
	return 0;
}
#endif