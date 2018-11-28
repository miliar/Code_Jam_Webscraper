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

void solve()
{
	ll a, b, c, mul;
	cin >> a >> b >> c;
	mul = a;

	int x = 0;
	for(;;)
	{
		if (mul >= b) break;
		mul *= c;
		++x;
	}
	--x;

	int L = 1, R = x, ans = 0;
	while (L <= R)
	{
		++ans;
		if (L == R) break;
		L = (L + R) / 2 + 1;
	}

	cout << ans << endl;
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
