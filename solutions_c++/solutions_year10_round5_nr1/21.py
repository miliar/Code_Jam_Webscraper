#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

bool u[1000000];
int n, d, a[100];
int res = -1;

int64 power (int64 x, int64 pw, int64 P)
{
	if (x == 0)
		return 0;
	int64 res = 1;
	while (pw > 0)
	{
		if (pw & 1)
			res = (res * x) % P;
		x = (x * x) % P;
		pw >>= 1;
	}
	return res;
}

int calc1 (int64 P)
{
	if (n <= 1)
		return -2;
	if (n == 2 && a[0] == a[1])
		return a[0];
	if (n <= 2)
		return -2;
	forn (i, n)
		if (a[i] % P != a[i])
			return -1;
	int64 S0 = a[0];
	int64 S1 = a[1];
	int64 S2 = a[2];
	int64 A = (S2 - S1 + P) % P * power ((S1 - S0 + P) % P, P-2, P);
	int64 B = (((S1 - A * S0) % P) + P) % P;
	forn (i, n-1)
		if ((A*a[i] + B) % P != a[i+1])
			return -1;
	return (A * a[n-1] + B) % P;
}

void calc ()
{
	scanf ("%d%d", &d, &n);
	forn (i, n)
		scanf ("%d", &a[i]);
	res = -1;
	int y = 1;
	forn (i, d)
		y *= 10;
	for (int i = 2; i < y; i ++)
	if (!u[i])
	{
		int x = calc1 (i);
		if (x == -1)
			continue;
		if (x == -2)
		{
			printf ("I don't know.\n");
			return;
		}
		else
		if (res != -1 && res != x)
		{
			printf ("I don't know.\n");
			return;
		}
		else
			res = x;
	}
	if (res == -1)
	{
//		printf ("I don't know.\n");
//		return;
	}
	printf ("%d\n", res);
}

int main ()
{
	seta (u, 0);
	u[0] = u[1] = 1;
	for (int i = 2; i < 1000000; i ++)
		if (!u[i])
		{
			int x = i * 2;
			while (x < 1000000)
			{
				u[x] = 1;
				x += i;
			}
		}
	int tt;
	scanf ("%d", &tt);
	forn (ii, tt)
	{
		printf ("Case #%d: ", ii+1);
		calc ();
	}
	
	return 0;
}
