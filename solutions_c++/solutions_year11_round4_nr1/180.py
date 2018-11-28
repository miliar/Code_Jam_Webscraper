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
#define N 20000

struct pass
{
	int l, r, v;
	bool operator < (const pass &a) const {return v<a.v;}
};
pass a[N];
int L, S, R, n;
double tme;

void main2 ()
{
	double res=0;
	cin >> L >> S >> R >> tme >> n;
	for (int i = 0; i < n; i++)
		scanf ("%d%d%d", &a[i].l, &a[i].r, &a[i].v);
	int t=n;
	for (int i = 1; i < n; i++)
		a[t].l = a[i-1].r,
		a[t].r = a[i].l,
		a[t++].v = 0;
	a[t].l = 0;
	a[t].r = a[0].l;
	a[t++].v = 0;
	a[t].l = a[n-1].r;
	a[t].r = L;
	a[t++].v = 0;        
	sort (a, a + t);

	for (int i = 0; i < t; i++)
	{
//		printf ("here l=%d r=%d\n", a[i].l, a[i].r);
		if ((double) (a[i].r-a[i].l)/(R+a[i].v) <= tme)
		{
			tme -= (double) (a[i].r-a[i].l)/(R+a[i].v);
			res += (double) (a[i].r-a[i].l)/(R+a[i].v);
		}
		else
		{
			res += tme + (double) ((a[i].r-a[i].l- tme*(R+a[i].v))/(S+a[i].v));
			tme = 0;
//			printf ("here tme=%.2lf len=%d\n", tme, a[i].r-a[i].l);
		}
	}

	gout;
	printf ("%.9lf\n", res);
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
