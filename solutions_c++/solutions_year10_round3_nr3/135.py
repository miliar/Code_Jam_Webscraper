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

int a[1000][1000], sz[1000][1000], n, m;
int ans[1000];

int toInt(char c)
{
	if (isdigit(c))
		return (c - '0');
	return (10 + (c - 'A'));
}

int make(int i, int j)
{
	if (a[i][j] == -1)
		return (0);

	for(int x = 1; x < 1000; ++x)
	{
		if (i + x == n || j + x == m)
			return (x);
		for(int y = 0; y <= x; ++y)
		{
			if (a[i + x][j + y] == -1) return (x);
			if (a[i + x][j + y] == a[i + x - 1][j + y]) return (x);

			if (a[i + y][j + x] == -1) return (x);
			if (a[i + y][j + x] == a[i + y][j + x - 1]) return (x);
		}
	}
}

bool ok()
{	
	int ma = 0;
	fi(n)
		fj(m)
		{
			sz[i][j] = make(i, j);
			ma = max(ma, sz[i][j]);
		}
	if (ma == 0)
		return (false);

	ans[ma]++;
	fi(n)
		fj(m)
			if (sz[i][j] == ma)
			{
				for(int x = 0; x < sz[i][j]; ++x)
					for(int y = 0; y < sz[i][j]; ++y)
						a[i + x][j + y] = -1;
				return (true);
			}
}

void solve()
{
	cin >> n >> m;
	fi(n)
	{
		fj(m / 4)
		{
			char c;
			cin >> c;
			int x = toInt(c);
			fk(4)
				if (x & (1 << k))
					a[i][4 * j + 3 - k] = 1;
				else
					a[i][4 * j + 3 - k] = 0;
		}
	}

	clr(ans);
	while (1)
		if (!ok())
			break;

	int res = 0;
	for(int i = 999; i >= 1; --i)
		if (ans[i] != 0)
			res++;
	cout << res << endl;

	for(int i = 999; i >= 1; --i)
		if (ans[i] != 0)
			cout << i << ' ' << ans[i] << endl;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	fi(t)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
} 
