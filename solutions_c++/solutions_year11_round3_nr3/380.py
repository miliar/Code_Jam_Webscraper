#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXLEN = 10100;
const long long inf = 1000000000000000001LL;

int n;
long long l, h;
long long f[MAXLEN];

void Scan()
{
	scanf("%d%lld%lld", &n, &l, &h);
	for (int i = 0; i < n; i++)
		scanf("%lld", &f[i]);
	sort(f, f+n);
	n = unique(f, f+n) - f;
	f[n] = 0;
}

long long FindDiv(long long num, long long l1, long long h1)
{	
	long long bestRes = inf;
	for (long long i = 1; i*i <= num; i++)
	{
		if (num % i == 0)
		{
			long long n1 = i;
			if (l <= n1 && n1 <= h && (long long)n1%l1 == 0 && h1%(long long)n1 == 0)
				bestRes = min(n1, bestRes);
			n1 = num / i;
			if (l <= n1 && n1 <= h && (long long)n1%l1 == 0 && h1%(long long)n1 == 0)
				bestRes = min(n1, bestRes);
		}
	}
	return bestRes;
}

long long gcd(long long a, long long b)
{
	if (a % b == 0) return b;
	return gcd(b, a % b);
}

long long mult(long long a, long long b)
{
	if ((double)a*(double)b < (double)inf)
		return a*b;
	else return inf;
}

long long lcm(long long a, long long b)
{
	long long g = gcd(a, b);
	a /= g;
	return mult(a, b);
}

long long gcds[MAXLEN];
long long lcms[MAXLEN];

void Solve2()
{
	int ans = -1;
	for (int i = l; i <= h; i++)
	{
		bool ok = true;
		for (int j = 0; j < n && ok; j++)
			if (f[j] % i == 0 || i % f[j] == 0);
			else ok = false;
		if(ok)
		{
			ans = i;
			break;
		}
	}
	if (ans == -1) printf("NO ");
	else printf("%d ", ans);
}

void Solve()
{
	gcds[n-1] = f[n-1];	
	for (int i = n-2; i >= 0; i--)
		gcds[i] = gcd(gcds[i+1], f[i]);
	lcms[0] = 1;
	for (int i = 1; i <= n; i++)
		lcms[i] = lcm(lcms[i-1], f[i-1]);

	long long best = inf;
	for (int i = 0; i < n; i++)
	{
		if (lcms[i] == inf)
			break;
		if (lcms[i] <= gcds[i] && gcds[i] % lcms[i] == 0)
		{
			long long q = FindDiv(gcds[i], lcms[i], gcds[i]);
			if (q != inf)
				best = min(best, q);
		}		
	}
	if (lcms[n] != inf)
	{
		long long q = (l + lcms[n] - 1) / lcms[n];
		q = q*lcms[n];
		if (q <= h)
			best = min(best, q);
	}
	if (best == inf)
		printf("NO\n");
	else printf("%lld\n", best);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		Scan();
		printf("Case #%d: ", i+1);
		fprintf(stderr, "test %d\n", i);
		//Solve2();
		Solve();
	}
	return 0;
}