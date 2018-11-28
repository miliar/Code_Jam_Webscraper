#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
const int MAXN = 1e9;
__int64 gcd(__int64 a, __int64 b)
{
	while (b)
	{
		a %= b;
		swap(a, b);
	}
	return a;
}

__int64 N, L, R;
__int64 notes[10146];
__int64 gcds[10146];
__int64 find(__int64 from, __int64 to, __int64 step, __int64 gc)
{
	if (to < from) return -1;
	for (__int64 i = from; i <= to && i < MAXN && i * i <= gc; i += step)
	{
		if (gc % i == 0)
		{
			return i;
		}
	}
	__int64 last = min(gc / from, (__int64) sqrt(1. * gc)) + 1;
	while (gc / last < from) 
	{
		--last;
		if (last < 1) return -1;
	}
	for (__int64 i = last; i > 0 && gc / i <= to; --i)
	{
		if (gc % i == 0 && (gc / i) % step == 0)
		{
			return gc / i;
		}
	}
	return -1;
}
__int64 INF = 1e18;
__int64 NOK(__int64 a, __int64 b)
{
	a /= (gcd(a, b));
	if (a >= R / b + 1)
	{
		return INF;
	}
	return a * b;
}
void solve()
{
	scanf ("%I64d%I64d%I64d", &N, &L, &R);
	__int64 ans = 0;
	for (int i = 0; i < N; ++i)
	{
		scanf ("%I64d", &notes[i]);		
	}
	sort(notes, notes + N);
	gcds[N] = 0;
	for (int i = N - 1; i >= 0; --i)
	{
		gcds[i] = gcd(notes[i], gcds[i + 1]);
	}
	__int64 no = 1;
	__int64 to = notes[0];
	__int64 from = 1;
	for (int i = 0; i < N; ++i)
	{
		__int64 nfrom = max (from, L);
		nfrom = (nfrom / from) * from;
		if (nfrom < L) nfrom += from;
		__int64 nto = min(to, R);
		nto = (nto / from) * from;
		ans = find(nfrom, nto, from, gcds[i]);
		if (ans != -1)
		{
			printf ("%I64d\n", ans);
			return;
		}
		from = NOK(from, notes[i]);
		to = notes[i + 1];
	}
	__int64 nfrom = max (from, L);
	nfrom = (nfrom / from) * from;
	if (nfrom < L) nfrom += from;
	if (nfrom <= R) 
	{
		printf ("%I64d\n", nfrom);
		return;
	}
	printf ("NO\n");
}
bool check(int n)
{
	for (int i = 0; i < N; ++i)
	{
		if (notes[i] % n != 0 && n % notes[i] != 0)
			return false;
	}
	return true;
}
void stupid()
{
	//scanf ("%I64d%I64d%I64d", &N, &L, &R);
	__int64 ans = 0;
	for (int i = 0; i < N; ++i)
	{
		//scanf ("%I64d", &notes[i]);		
	}
	sort(notes, notes + N);
	for (int i = L; i <= R; ++i)
	{
		if (check(i))
		{
			printf ("%d\n", i);
			return;
		}
	}
	printf ("NO\n");
}
int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf ("Case #%d: ", i + 1);
		solve();
		//stupid();
	}
	return 0;
}