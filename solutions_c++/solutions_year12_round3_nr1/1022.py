using namespace std;

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <limits>
#include <stack>
#include <string>
#include <vector>

#define EPS 1e-11
#define INF 1000000000
#define LL long long

#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )
#define rrep( i, a, b ) for( __typeof(b) i = ( a ); i >= ( b ); --i )
#define xrep( i, a, b ) _rep( i, a, b, 1 )

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()

typedef vector <int> vi;
vi T[1024];
int cur;
LL memo[1024];
LL solve(int u)
{
	if (u == cur) return 1;
	LL &ret = memo[u];
	if (ret != -1) return ret;
	ret = 0;
	rep(i,sz(T[u]))
	{
		int v = T[u][i];
		ret += solve(v);
	}
	if (ret >= 2) ret = 3;
	return ret;
}

int main()
{
	freopen("/home/user/input.txt", "r", stdin);
	freopen("/home/user/output.txt", "w", stdout);

	int tcase, n;

	cin >> tcase;

	xrep(caseno,1,tcase)
	{
		cin >> n;

		rep(i,n) T[i].clear();
		int d, x;
		rep(i,n)
		{
			cin >> d;
			rep(j,d)
			{
				cin >> x;
				x--;
				T[x].pb(i);
			}
		}
		bool ok = false;
		rep(i,n)
		{
			ms(memo, -1);
			cur = i;
			rep(j,n)
			{
				LL ret = solve(j);
				//cout << i << " " << j << " " << ret << endl;
				if (ret >= 2)
				{
					ok = true;
					break;
				}
			}
		}
		cout << "Case #" << caseno << ": ";
		if (ok) cout << "Yes" << endl;
		else cout << "No" << endl;
	}
}
