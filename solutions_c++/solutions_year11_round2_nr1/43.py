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

#define gout case_number++, printf("Case #%d:\n",case_number), cout

double frac (int a, int b)
{
 	if (!a) return 0.;
	return (double)a/b;
}

double owp[2000];
int n;
int wins[2000], tot[2000];
char s[200][200];

void main2 ()
{
	scanf ("%d", &n);

	for (int i = 0; i < n; i++)
		wins[i] = 0,
		tot[i] = 0,
		scanf ("%s", s[i]);

	double rpi, wp, oowp, vv;

	for (int i = 0, j; i < n; i++)
		for (int j = 0; j < n; j++)
			wins[i] += s[i][j] == '1',
			tot[i] += s[i][j] != '.';

	for (int i = 0; i < n; i++)
	{
	 	owp[i] = 0;
	 	for (int j = 0; j < n; j++)
	 		if (s[i][j]!='.')
	 			owp[i] += frac (wins[j]-(s[j][i]=='1'), tot[j]-(s[j][i]!='.'));
	 	owp[i] /= tot[i];
	}

	gout;

	for (int i = 0; i < n; i++)
	{
	 	rpi = 0.25 * frac (wins[i], tot[i]);
	 	vv = 0;

	 	for (int j = 0; j < n; j++)
	 		if (s[i][j]!='.')
	 			vv += owp[j];
	 	rpi += 0.25*vv/tot[i] + 0.5*owp[i];

	 	printf ("%.9lf\n", rpi);
	}
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
