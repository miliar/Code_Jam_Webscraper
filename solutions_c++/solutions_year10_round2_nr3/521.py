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
#define modulo 100003

typedef long long ll;
typedef long double ld;

int	fx[] = {-1, 0, +1, 0}, fy[] = {0, +1, 0, -1},
	ex[] = {-1, -1, 0, +1, +1, +1, 0, -1}, ey[] = {0, +1, +1, +1, 0, -1, -1, -1};

using namespace std;

int test_num, case_number;
int n, ret;
int d[505][505], dp[505][505], w[505][505];

#define gout case_number++, printf("Case #%d: ",case_number), cout

int C (int x, int y)
{
	if (x < y) return 0;
	if (!y) return 1;
	if (w[x][y]) return d[x][y];
	w[x][y] = 1;
	d[x][y] = (C (x - 1, y) + C (x - 1, y - 1)) % modulo;
	return d[x][y];
}

void main2 ()
{
	scanf ( "%d", &n );

	ret = 0;
	for ( int i = 0; i < n; i++ )
		ret = (ret + dp[i][n]) % modulo;

	gout << ret << "\n";
}

int main ()
{
	freopen ( "c.in", "r", stdin );
	freopen ( "c.out", "w", stdout );

	scanf ( "%d", &test_num );

	dp[0][1] = 1;
	for ( int i = 1; i < 500; i++ )
		for ( int k = i + 1; k <= 500; k++ )
			for ( int j = 0; j < i; j++ )
			{
//				if (i == 4 && k == 7)
//					printf ( "before %d\n", dp[i][k] );
				dp[i][k] = (dp[i][k] + dp[j][i]*C (k - i - 1, i - j - 1)) % modulo;
//				if (i == 4 && k == 7)
//					printf ( "after %d\n", dp[i][k] );
			}

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
