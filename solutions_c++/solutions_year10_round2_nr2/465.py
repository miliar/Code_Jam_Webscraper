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


int C, case_number;
int n, k, b, t, cnt, v1;
int x[100], v[100];

#define gout case_number++, printf("Case #%d: ",case_number), cout

void main2 ()
{
	scanf ( "%d%d%d%d", &n, &k, &b, &t );
	cnt = 0;
	for ( int i = 0; i < n; i++ )
		scanf ( "%d", &x[i] );
	for ( int i = 0; i < n; i++ )
		scanf ( "%d", &v[i] );
	for ( int i = 0; i < k; i++ )
	{
		v1 = -1;
	 	for ( int j = n - i - 1; j >= 0; j-- )
	 		if (b - x[j] <= t*v[j])
	 		{
				for ( int k = j; k < n - i - 1; k++ )
					swap (v[k], v[k + 1]),
					swap (x[k], x[k + 1]),
					cnt++;
//				printf ( "here for %d %d\n", i, cnt );
				v1 = 1;
				break;
	 		}
		if (v1 == -1)
		{
			gout << "IMPOSSIBLE\n";
			return;
		}
	}
	gout << cnt << "\n";
}

int main ()
{
	freopen ( "b.in", "r", stdin );
	freopen ( "b.out", "w", stdout );

	scanf ( "%d", &C );

	for ( int i = 0; i < C; i++ )
		main2 ();

	return 0;
}
