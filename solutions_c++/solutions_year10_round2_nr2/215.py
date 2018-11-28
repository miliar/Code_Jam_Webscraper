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

#define ll long long int
#define INF ( ((ll)1) << 60 )


//////////////////////////////// GRAPHS ///////////////////////////////

//int di[] = {-1,0,1,0   ,   -1,1,1,-1};
//int dj[] = {0,1,0,-1   ,   1,1,-1,-1};

//#define inr(i,j)  ( 0 <= (i) && (i) < n && 0 <= (j) && (j) < n )   // square
//#define inr(i,j)  ( 0 <= (i) && (i) < n && 0 <= (j) && (j) < m )   // rectangular

#define N 60
ll n, K, B, T;

class Chick
{
public:
	ll x;
	ll v;
	bool bad;
	int howManyBadInfront;

	void isGood()
	{
		if (x + v*T >= B) bad = false;
		else bad = true;
	}
};

Chick a[N];

int main () {
	int i, j, CAS, x;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {
		scanf("%lld%lld%lld%lld", &n, &K, &B, &T);

		for (i = 0; i < n; ++i)
		{
			a[i].bad = true, a[i].howManyBadInfront = 0;
		}

		for (i = 0; i < n; ++i)
		{
			scanf("%d", &x);
			a[i].x = x;
		}
		for (i = 0; i < n; ++i)
		{
			scanf("%d", &x);
			a[i].v = x;
		}

		x = 0;
		for (i = n-1; i >= 0; --i)
		{
			a[i].isGood();
			a[i].howManyBadInfront = x;
			if (a[i].bad) ++x;
		}

		int have = 0;
		int swaps = 0;

		for (i = n-1; i >= 0 && have < K; --i)
		{
			if (!a[i].bad)
			{
				++have;
				swaps += a[i].howManyBadInfront;
			}
		}
		
		printf("Case #%d: ", cas);
		
		if (have < K) printf("IMPOSSIBLE");
		else printf("%d", swaps);
		
		printf("\n");

		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}


