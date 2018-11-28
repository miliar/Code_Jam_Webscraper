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

int n, m, D;
char a[1000][1000];
double s[1000][1000], f1[1000][1000], f2[1000][1000];

double val1 (int i, int j, int K)
{
 	return f1[i+K][j+K]+f1[i][j]-f1[i][j+K]-f1[i+K][j];
}
double val2 (int i, int j, int K)
{
 	return f2[i+K][j+K]+f2[i][j]-f2[i][j+K]-f2[i+K][j];
}
double val (int i, int j, int K)
{
 	return s[i+K][j+K]+s[i][j]-s[i][j+K]-s[i+K][j];
}


bool ok (int K)
{
	double v1,v2, x=0, y=0;
 	for (int i = 0; i <= n-K; i++)
 		for (int j = 0, q, w; j <= m-K; j++)
 		{
			x=i+K/2.-0.5; y = j+K/2.-0.5; v1 = v2 = 0;

			v1 = val1 (i, j, K) - val (i, j, K)*x;
			v2 = val2 (i, j, K) - val (i, j, K)*y;
			v1 -= (i-x)*(a[i][j]-'0'+D);
			v1 -= (i-x)*(a[i][j+K-1]-'0'+D);
			v1 -= (i+K-1-x)*(a[i+K-1][j]-'0'+D);
			v1 -= (i+K-1-x)*(a[i+K-1][j+K-1]-'0'+D);
			v2 -= (j-y)*(a[i][j]-'0'+D);
			v2 -= (j-y)*(a[i+K-1][j]-'0'+D);
			v2 -= (j+K-1-y)*(a[i][j+K-1]-'0'+D);
			v2 -= (j+K-1-y)*(a[i+K-1][j+K-1]-'0'+D);
			if (!v1 && !v2) return 1;
 		}
 	return 0;
}

void main2 ()
{
	scanf ("%d%d%d", &n, &m, &D);

	for (int i = 0; i < n; i++)
		scanf ("%s", &a[i]);

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
		{
		 	f1[i][j] = f1[i-1][j] + f1[i][j-1]-f1[i-1][j-1];
		 	f1[i][j] += (a[i-1][j-1]-'0'+D)*(i-1);
		 	f2[i][j] = f2[i-1][j] + f2[i][j-1]-f2[i-1][j-1];
		 	f2[i][j] += (a[i-1][j-1]-'0'+D)*(j-1);
		 	s[i][j] = s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i-1][j-1]-'0'+D;
		}

	for (int K = min (n, m); K >= 2; K--)
	{
	 	if (K == 2)
	 	{
	 	 	gout << "IMPOSSIBLE\n";
	 	 	break;
	 	}
	 	if (ok (K))
	 	{
	 	 	gout << K << endl;
	 	 	break;
	 	}
	}
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
