// USTU Frogs
// Accepted
// I'm Feeling Lucky!

#include <iostream>

void initf()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <queue>
#include <memory.h>
#include <cassert>
#include <cmath>

using namespace std;

#define fr(i, a, b) for(int (i) = (a); (i) <= (b); ++(i))
#define fi(n) for(int i = 0; i < (n); ++i)
#define fj(n) for(int j = 0; j < (n); ++j)
#define fk(n) for(int k = 0; k < (n); ++k)
#define pb push_back
#define mp make_pair
#define clr(a) memset((a), 0, sizeof(a))
#define CLR(a,b) memset((a), (b), sizeof(a))
#define all(v) (v).begin(),(v).end()

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull; 
typedef vector < int > vi;
typedef pair < int, int > pii;

const int inf = (1 << 20);
const double eps = 1e-7;

struct A
{
	double x, vel;
};

bool operator<(A l, A r)
{
	return (l.x + eps < r.x);
}

char buf[1000];
A a[50];
int n, KK, res[100];
double b, t;

bool ok(int i, int k)
{
	if (a[i].vel - eps <= a[k].vel)
		return (false);

	double time = fabs((a[i].x - a[k].x) / (a[i].vel - a[k].vel));
	if (t - eps <= time) return (false);
	if (b - eps <= a[i].x + time * a[i].vel) return (false);
	return (true);
}

void solve()
{
	cin >> n >> KK >> b >> t;
	clr(res);
	fi(n)
		cin >> a[i].x;
	fi(n)
		cin >> a[i].vel;

	sort(a, a + n);

	for(int i = n - 1; i >= 0; --i)
	{
		res[i] = inf;
		if (t + eps < (b - a[i].x) / a[i].vel) continue;
		if (i == n - 1)
		{
			res[i] = 0;
			continue;
		}

		for(int j = i + 1; j <= n; ++j)
		{
			int cur = 0;

			for(int k = i + 1; k < j; ++k)
				if (ok(i, k))
					++cur;
			res[i] = min(res[i], cur + res[j]);
		}
	}

	sort(res, res + n);
	int ans = 0;
	fi(KK)
	{
		if (res[i] == inf)
		{
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		ans += res[i];
	}
	cout << ans << endl;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	gets(buf);
	sscanf(buf, "%d", &t);
	fi(t)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
} 
