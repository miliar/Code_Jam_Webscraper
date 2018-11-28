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

int n, col, sz, res;
int a[2000], w[2000];

void dfs (int u)
{
	if (w[u] == col) return;

 	w[u] = col;
 	sz++;

	dfs (a[u]);
}

void main2 ()
{
	scanf ("%d", &n);

	for (int i = 0; i < n; i++)
		scanf ("%d", &a[i]),
		a[i]--;

	col++;
	res = 0;
	for (int i = 0; i < n; i++)
	{
		sz = 0;
		dfs (i);
		if (sz>1) res += sz;
	}

	gout << res << endl;
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
