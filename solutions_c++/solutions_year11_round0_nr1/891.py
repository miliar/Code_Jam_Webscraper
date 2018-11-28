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

int t[200], p[200];

void main2 ()
{
	int n;
	scanf ("%d%*c", &n);

	for (int i = 0; i < n; i++)
	 	scanf ("%c%d%*c", &t[i], &p[i]);
	int p1 = 1, p2 = 1, t1 = 0, t2 = 0, tt = 0;

	for (int i = 0; i < n; i++)
		if (t[i] == 'O')
		{
			tt = max (abs (p1-p[i])-abs (tt-t1), 0)+tt+1;
			p1 = p[i];
			t1 = tt;
		}
		else
		{
			tt = max (abs (p2-p[i])-abs (tt-t2), 0)+tt+1;
			p2 = p[i];
			t2 = tt;
		}

	gout << tt << endl;
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
