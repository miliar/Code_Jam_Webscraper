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

int n, t;
int a[2000];
pair <int, int> b[2000];

void main2 ()
{
	scanf ("%d", &n);

	if (!n)
	{
		gout << 0 << endl;
	 	return;
	}

	for (int i = 0; i < n; i++)
		scanf ("%d", &a[i]);
	sort (a, a + n);

	b[(t=1)-1] = make_pair (1, a[0]);

	for (int i = 1, fnd, j; i < n; i++)
	{
		fnd = 0;
		for (j = 0; j < t; j++)
			if (b[j].second+1 == a[i])
			{
			 	fnd = 1;
			 	b[j].second++;
			 	b[j].first++;
			 	break;
			}
		if (!fnd)
			b[t++] = make_pair (1, a[i]);
		sort (b, b + t);
//		for (j = 0; j < t; j++)
//			printf ("%d %d\n", b[j].first, b[j].second);
//		puts ("");
	}

	gout << b[0].first << endl;
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
