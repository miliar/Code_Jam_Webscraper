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

struct point
{
	double x, y;
	bool operator < (const point &a) const {return x<a.x;}
};
point a[2000], b[2000];
int n, m, G, W;

void proceed (point *a, point *b, int &n1, int &m1)
{
	int m = m1;
	double A, B, C, D, L;

	for (int i = 0, j, fnd; i < n1; i++)
	{
		for (j = 0; j<m1&&b[j].x<a[i].x; j++);

		if (j==m1 || b[j].x!=a[i].x)
		{
//			printf ("here found j =%d b[j]={%.1lf, %.1lf}\n", j, b[j].x, b[j].y);
//			printf ("b[j]={%.1lf, %.1lf}\n", b[j-1].x, b[j-1].y);
			A = b[j].x-b[j-1].x; B = b[j].y-b[j-1].y; L = a[i].x-b[j-1].x;
//			printf ("L = %.1lf A = %.1lf B = %.1lf\n", L, A, B);
			b[m].x = a[i].x;
			b[m++].y = b[j-1].y + B/A*L;
		}
	}
	m1 = m;
	sort (b, b + m);
}

double fnd (double xx)
{
	int j = 0;
	double ret = 0;

	for (; j<n-1 && a[j+1].x < xx; j++)
		ret += (b[j+1].y-a[j+1].y+b[j].y-a[j].y)*(b[j+1].x-b[j].x)/2.;
//		ret += fabs ((a[j+1].x-a[j].x)*(b[j].y-a[j].y)-(a[j+1].y-a[j].y)*(b[j].x-a[j].x));

	double A = a[j+1].x-a[j].x, B = a[j+1].y-a[j].y, yy, L, y2;
	L = xx - a[j].x; yy = a[j].y + B/A*L;
	A = b[j+1].x-b[j].x; B = b[j+1].y-b[j].y;
	y2 = b[j].y+B/A*L;

//	printf ("here ret = %.2lf xx=%.2lf yy=%.2lf\n", ret, xx, yy);
//	printf ("j = %d\n", j);

//	ret += fabs ((xx-a[j].x)*(b[j].y-a[j].y)-(yy-a[j].y)*(b[j].x-a[j].x));
	ret += (b[j].y-a[j].y+y2-yy)*(xx-a[j].x)/2.;

	return ret;
}

void main2 ()
{
	scanf ("%d%d%d%d", &W, &n, &m, &G);

	for (int i = 0; i < n; i++)
		scanf ("%lf%lf", &a[i].x, &a[i].y);
	for (int i = 0; i < m; i++)
		scanf ("%lf%lf", &b[i].x, &b[i].y);
	proceed (a, b, n, m);
	proceed (b, a, m, n);

//	for (int i = 0; i < n; i++)
//		printf ("{%.2lf %.2lf}\n", b[i].x, b[i].y);

	gout;
	double S = 0;

	for (int i = 1; i < n; i++)
		S += (b[i].y-a[i].y+b[i-1].y-a[i-1].y)*(a[i].x-a[i-1].x)/2.;
//		S += fabs ((a[i].x-a[i-1].x)*(b[i-1].y-a[i-1].y)-(a[i].y-a[i-1].y)*(b[i-1].x-a[i-1].x));

	for (int i = 1; i < G; i++)
	{
		double lo = 0, hi = W, mi;
		for (int it = 0; it < 100; it++)
		{
			mi = (lo+hi)*0.5;

			if (fnd (mi) > S/G*i)
				hi = mi;
			else
				lo = mi;
		}

//		printf ("val=%.2lf %.2lf\n", fnd (4.290588), S/G*i);
//		printf ("s = %.2lf\n", S);
		printf ("%.9lf\n", (lo+hi)*0.5);
	}
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
