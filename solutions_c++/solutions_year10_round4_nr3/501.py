//Solution by Ali-Amir Aldan
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <map>

#define forn(i, n) for (int (i); (i) < (n); (i)++ )
#define betw(a, b, c) ((a) <= (c) && (b) >= (c))
#define pb push_back
#define mp make_pair
#define ss second
#define ff first

typedef long long ll;
typedef long double ld;

int	fx[] = {-1, 0, +1, 0}, fy[] = {0, +1, 0, -1},
	ex[] = {-1, -1, 0, +1, +1, +1, 0, -1}, ey[] = {0, +1, +1, +1, 0, -1, -1, -1};

using namespace std;

int test_num, case_number;
int r, xx, yy, x2, y2, s;
bool a[102][102];

#define gout case_number++, printf("Case #%d: ",case_number), cout

void main2 ()
{
	scanf ( "%d", &r );

	memset (a, 0, sizeof (a));
	for ( int i = 0; i < r; i++ )
	{
		scanf ( "%d%d%d%d", &xx, &yy, &x2, &y2 );
		for ( int i1 = xx; i1 <= x2; i1++ )
			for ( int j1 = yy; j1 <= y2; j1++ )
				a[i1][j1] = 1;
	}

	for ( int it = 0; it < 100*100; it++ )
	{
		s = 0;

		for ( int i = 100; i > 0; i-- )
			for ( int j = 100; j > 0; j-- )
			{
				s += a[i][j];
				if (a[i][j] && !a[i - 1][j] && !a[i][j - 1]) a[i][j] = 0;
				else
				if (!a[i][j] && a[i - 1][j] && a[i][j - 1]) a[i][j] = 1;
			}

		if (!s)
		{
			gout << it << "\n";
			return;
		}
	}
}

int main ()
{
	freopen ( "c.in", "r", stdin );
	freopen ( "c.out", "w", stdout );

	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
