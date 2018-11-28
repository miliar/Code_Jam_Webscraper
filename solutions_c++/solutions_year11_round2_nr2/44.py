//Solution by Ali-Amir Aldan
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <map>
#include <set>

#define forn(i, n) for (int (i); (i) < (n); (i)++ )
#define betw(a, b, c) ((a) <= (c) && (b) >= (c))
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define pint pair <int, int> 

typedef long long ll;
typedef double ld;

int	fx[] = {-1, 0, +1, 0}, fy[] = {0, +1, 0, -1},
	ex[] = {-1, -1, 0, +1, +1, +1, 0, -1}, ey[] = {0, +1, +1, +1, 0, -1, -1, -1};

using namespace std;

int test_num, case_number;

#define gout case_number++, printf("Case #%d: ",case_number), cout

int c, d, n, pos, x;
int a[10000000];

bool ok (double t)
{
	double last = -1e18;

	for (int i = 0; i < n; i++)
	{
		if (a[i]-last>d)
			last = max (last+d, a[i]-t);
		else
		{
			if (a[i]+t-last < d) return 0;
			last = min (a[i]+t, last+d);
		}
	}

	return 1;
}

void main2 ()
{
	scanf ("%d%d", &c, &d);

	n = 0;
	for (int i = 0; i < c; i++)
	{
	 	scanf ("%d%d", &pos, &x);

	 	for (; x--;)
	 		a[n++] = pos;
	}
	sort (a, a + n);

	double lo = 0, hi = 1e13, mi;

	for (int it = 0; it < 100; it++)
	{
		mi = (lo+hi)*0.5;

		if (ok (mi)) hi = mi;
		else lo = mi;
	}
	gout;
	printf ("%.7lf\n", mi);
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
