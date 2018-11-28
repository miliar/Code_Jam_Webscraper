#include <cstdio>
#include <cstring>

const int maxx = 1000000;
const int maxp = 100000;
const int maxn = 10;
const int maxd = 6;
const int power[maxd + 1] = {1, 10, 100, 1000, 10000, 100000, 1000000};
int prime[maxp];
int a[maxn];
int np;
int d, n;

bool pri(int x)
{
	for (int i = 2; i * i <= x; i++)
		if (x % i == 0) return false;
	return true;
}

void getPrime()
{
	np = 1;
	prime[0] = 2;
	for (int i = 3; i <= maxx; i += 2)
		if (pri(i)) prime[np++] = i;
}

bool equal()
{
	for (int i = 1; i < n; i++)
		if (a[i] != a[0]) return false;
	return true;
}

int gcd(long long a, long long b, long long &x, long long &y, long long p)
{
	if (b == 0)
	{
		x = 1;
		y = 0;
		return a;
	}
	else
	{
		long long x1, y1;
		int d = gcd(b, a % b, x1, y1, p);
		x = y1;
		y = x1 - (a / b) * y1;
		x = (x % p + p) % p;
		y = (y % p + p) % p;
		return d;
	}
}

bool existpri(int max)
{
	for (int i = 0; i < np && prime[i] <= power[d]; i++)
		if (prime[i] > max) return true;
	return false;
}

void getAB(int p, long long &x, long long &y)
{
	long long c1 = ((a[1] - a[0]) % p + p) % p;
	long long c2 = ((a[2] - a[1]) % p + p) % p;
	
	long long x1, y1;
	gcd(p, c1, x1, y1, p);
	x = ((c2 * y1) % p + p) % p;
	y = ((a[1] -a[0] * x) % p + p) % p;
}

int main()
{
	int testnumber;
	long long x, y;
	
	getPrime();
	fprintf(stderr, "finished");
	
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d", &testnumber);
	for (int testcount = 0;  testcount < testnumber; testcount++)
	{
		scanf("%d%d", &d, &n);
		int max = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
			if (a[i] > max) max = a[i];
		}
		
		if (n == 1)
		{
			printf("Case #%d: I don't know.\n", testcount + 1);
		}
		else
		if (a[0] == a[1])
		{
			if (existpri(max) && equal()) printf("Case #%d: %d\n", testcount + 1, a[0]);
			else printf("Case #%d: I don't know.\n", testcount + 1);
		}
		else
		if (n == 2)
		{
			printf("Case #%d: I don't know.\n", testcount + 1);
		}
		else
		{
			int ans = -1;
			bool noans = true;
			for (int i = 0; i < np && prime[i] <= power[d]; i++)
			if (prime[i] > max)
			{
				getAB(prime[i], x, y);
				bool vali = true;
				for (int j = 0; j < n - 1; j++)
					if ((x * a[j] + y) % prime[i] != a[j + 1])
					{
						vali = false;
						break;
					}
				if (vali)
				{
					noans = false;
					int a1 = (x * a[n - 1] + y) % prime[i];
					if (ans == -1 || a1 == ans) ans = a1;
					else
						{
							noans = true;
							break;
						}
				}
			}
			if (!noans) printf("Case #%d: %d\n", testcount + 1, ans);
			else printf("Case #%d: I don't know.\n", testcount + 1);
		}
	}
	
	return 0;
}
