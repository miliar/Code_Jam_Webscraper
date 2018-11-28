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

long long fun (long long n, long long x, long long mult)
{
 	if (n<x) return 0;
 	return 1 + fun (n, x*mult, mult);
}

int a[1000002], f[1000002];
int npr;
long long n;

void main2 ()
{
	cin >> n;
	long long v = 0;
	for (int i = 0; i < npr; i++)
		if (a[i] <= n)
//			cerr << fun (n, a[i]) << endl,
			v += fun (n, a[i], a[i])-1;
	if (n==1) v = -1;
	gout << v+1 << endl;
}

int main ()
{
	scanf ( "%d", &test_num );

	npr = 1;
	a[0] = 2;
	for (int i = 3; i < 1000000; i+=2)
	{
		if (!f[i])
		{
		 	a[npr++] = i;
		 	f[i] = npr;
		}
		for (int j = 0; j < f[i]; j++)
			if (1LL*i*a[j]>=1000000)
				break;
			else
				f[i*a[j]] = j+1;
	}

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
