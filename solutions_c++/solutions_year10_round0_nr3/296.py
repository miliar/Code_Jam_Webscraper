#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
using namespace std;

#define CLR(a, x) memset(a, x, sizeof(a)) // x = 0|-1, true|false.
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<=(b); i++)
#define FORD(i, b, a) for(int i=(b); i>=(a); i--)
#define FORE(ty, it, data) for(ty::iterator it=data.begin(); it!=data.end(); it++)
#define ALL(x) (x).begin(),(x).end()
#define TWO(X) (1<<(X))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define EPS 1e-10
const double PI = acos(-1.0);

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<ll, ll> PII;
typedef map<string, int> MSI;

template<typename T> string toString(const T &n) { ostringstream O; O<<n; return O.str(); }

////////////////////////////////////////////////////////////////////////////////////////////////////////

ll table[1111], check[1111], pe[1111];
ll R, K, N;

int next(int idx)
{
	return (idx+1)%N;
}

PII go(int idx)
{
	ll people(0);
	int start(idx);
	while(true) {
		if(people+table[idx] > K)	break;
		people += table[idx];
		idx = next(idx);
		if(idx == start)	break;
	}
	return mp(idx, people);
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	scanf("%d\n", &T);
	FOR(tc, 1, T) {
		printf("Case #%d: ", tc);

		scanf("%lld %lld %lld", &R, &K, &N);
		REP(i, N) {
			scanf("%lld", &table[i]);
		}

		CLR(check, -1);
		int idx(0);
		check[idx] = 0;
		pe[idx] = 0;

		ll sol(0), r(0);
		bool first(true);
		while(r<R) {
			PII ret = go(idx);
			r++;
			ll fidx = ret.X;
			ll people = ret.Y;

			sol += people;
			if(first) {
				if(check[fidx]==-1) {
					check[fidx] = sol;
					pe[fidx] = r;
				}
				else {
					ll added = sol - check[fidx];
					ll p = r - pe[fidx];

					ll rep = (R-r)/p;
					sol += added*rep;
					r += rep*p;

					first = false;
				}
			}

			idx = fidx;
		}

		printf("%lld\n", sol);



		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}