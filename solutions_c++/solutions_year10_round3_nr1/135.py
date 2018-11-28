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

int n, a[1000], b[1000];

void solve()
{
	cin >> n;
	fi(n)
		cin >> a[i] >> b[i];

	int res = 0;
	fi(n)
		fj(i)
			if ((a[i] < a[j] && b[i] > b[j]) || (a[i] > a[j] && b[i] < b[j]))
				++res;
	cout << res << endl;
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
