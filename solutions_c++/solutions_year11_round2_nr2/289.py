//#pragma comment(linker, "/STACK:100000000")

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a) : (-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))
#define UNIQUE(p) sort(ALL(p)), p.resize( (int)(unique(ALL(p)) - p.begin()) )

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second

//#define INF 1000000000

//#define ll long long int
//#define INF ( ((ll)1) << 60 )

#define eps 1e-9

#define N 1000111

int n;
double d[N], d1[N];
double D;

bool f(double x)
{
	d1[0] = d[0] - x;
	for (int i = 1; i < n; ++i)
	{
		double mustBe = d1[i-1] + D;
		if (mustBe <= d[i])
		{
			d1[i] = max(mustBe, d[i] - x);
		}
		else
		{
			if (mustBe > d[i] + x)
			{
				return false;
			}
			d1[i] = mustBe;
		}
	}


	return true;
}


int main () {
	int i, j, CAS, c, x, y;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {
		mset(d,0), mset(d1,0);
		n = 0;

		scanf("%d%lf", &c, &D);

		for (i = 0; i < c; ++i)
		{
			scanf("%d%d", &x, &y);
			for (j = 0; j < y; ++j) d[n++] = x;
		}

		// algo
		double C = 1e16;
		double delta = C * 0.5;
		while (delta > 1e-15) // !!!
		{
			if (f(C)) C -= delta;
			else C += delta;

			delta *= 0.5;
		}
		
		printf("Case #%d: %.9lf\n", cas, C);
		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}


