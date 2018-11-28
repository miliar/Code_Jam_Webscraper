#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <bitset>

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define sz(v) ((int)(v.size()))

using namespace std;

typedef long long int64;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<string> vs;

template<class T> T abs(T x){ return x > 0 ? x : (-x); }
template<class T> T sqr(T x){ return x * x; }

int X[100], Y[100], R[100];

double get(vi v)
{
	if (!sz(v)) return 0.0;
	if (sz(v) == 1) return R[v[0]];
	return 0.5 * (R[v[0]] + R[v[1]] + sqrt(0.0 + sqr(X[v[0]] - X[v[1]]) + sqr(Y[v[0]] - Y[v[1]])));
}

void solve(int testnum)
{
	printf("Case #%d: ", testnum + 1);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> X[i] >> Y[i] >> R[i];
	double res = 1E100;
	for (int mask = 0; mask < (1 << n); mask++)
	{
		vi v[2];
		for (int i = 0; i < n; i++)
		{
			if ((mask >> i) & 1)
				v[0].pb(i);
			else
				v[1].pb(i);
		}
		if (sz(v[0]) == 3 || sz(v[1]) == 3) continue;
		double r0 = get(v[0]);
		double r1 = get(v[1]);
		res = min(res, max(r0, r1));
	}
	printf("%.5lf", res);
	printf("\n");
}

int main()
{
//	freopen("", "r", stdin);
//	freopen("", "w", stdout);
	int nc;
	cin >> nc;
	for (int it = 0; it < nc; it++)
	{
		solve(it);
	}
	return 0;
}
