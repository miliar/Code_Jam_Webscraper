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

int test_num, case_number, p, n, s, t;
int m[3000];
int b[3000][3000];
ll a[3000];
ll d[3000][3000];
bool w[3000][3000];

#define gout case_number++, printf("Case #%d: ",case_number), cout

ll get (int u, int taken)
{
	if (u >= n)
	{
		if (taken >= m[u - n]) return 0;
		return (1 << 30);
	}

	if (w[u][taken]) return d[u][taken];

	w[u][taken] = 1;
	d[u][taken] = min (a[u] + get (u*2, taken + 1) + get (u*2 + 1, taken + 1), get (u*2, taken) + get (u*2 + 1, taken));

	return d[u][taken];
}

void main2 ()
{
	scanf ( "%d", &p );

	memset (w, 0, sizeof (w));

	n = (1 << p); s = t = 0;

	for ( int i = 0; i < n; i++ )
		scanf ( "%d", &m[i] ),
		m[i] = p - m[i],
		s += m[i];

	for ( int i = 0; i < p; i++ )
		for ( int j = 0; j < (1 << (p - i - 1)); j++ )
			scanf ( "%d", &b[i][j] );

	for ( int i = p - 1; i >= 0; i-- )
		for ( int j = 0; j < (1 << (p - i - 1)); j++ )
			a[++t] = b[i][j];

	gout << get (1, 0) << "\n";
}

int main ()
{
	freopen ( "b.in", "r", stdin );
	freopen ( "b.out", "w", stdout );
	
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
