#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define ALL(cont) cont.begin(), cont.end()

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vl;
typedef vector<double> vd;

int main()
{
	int T;
	cin >> T;
	REP(t, T)
	{
		int R, k, N;
		cin >> R >> k >> N;
		vi g(N + 1);
		g[0] = 0;
		REP(i, N) cin >> g[i + 1];
		partial_sum(ALL(g), g.begin());

		int euro = 0;
		vi prer(N + 1, -1), pree(N + 1);
		bool d = false;
		for(int i = 0, r = 0; r < R; )
		{
			if(prer[i] > -1 && !d)
			{
				int m = (R - r) / (r - prer[i]);
				euro += m * (euro - pree[i]);
				r += m * (r - prer[i]);
				d = true;
				continue;
			}
			prer[i] = r;
			pree[i] = euro;
			int j = upper_bound(ALL(g), g[i] + k) - g.begin() - 1;
			if(j == N)
			{
				euro += g.back();
				j = min(i, upper_bound(ALL(g), k - (g.back() - g[i])) - g.begin() - 1);
			}
			euro += g[j] - g[i];
			i = j % N;
			r++;
		}
		printf("Case #%d: %d\n", t + 1, euro);
	}
	
	return 0;
}
