#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cmath>
using namespace std;

#define eps 1e-9
#define pb push_back
#define mp make_pair
#define RE(i, a, b) for(int (i) = a; (i) < (int)(b); (i)++)
#define REF(i, a, b) RE(i, a, b + 1)
#define REP(i, n) RE(i, 0, n) 
#define FOR(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define SZ(v) ((int)(v).size())
template<class T>string toString(T a) { stringstream t; t << a; return t.str(); }

FILE *fp = freopen("B-large-0.in", "r", stdin);
FILE *fout = freopen("B-large-0.out", "w", stdout);
typedef long long ll;

int main()
{
	int T;
	scanf("%d ", &T);
	for (int Ti = 1; Ti <= T; Ti++) {
	    fprintf(stderr, "Case #%d of %d...\n", Ti, T);
		int l, n, c;
		ll t;
		scanf("%d %lld %d %d", &l, &t, &n, &c);
		ll ans = 0;
		vector<ll> dis(n, 0);
		vector<ll> nd;
		for (int i = 0; i < c; i++) scanf("%lld", &dis[i]);
		for (int i = c; i < n; i++) dis[i] = dis[i % c];

		int z = -1;
		for (int i = 0; i < n; i++) {
			ans += dis[i] * 2;
			if (ans >= t) {
				if (ans > t) {
					nd.push_back((ans - t) / 2);
					ans = t;
				}
				z = i;
				break;
			}
		}

		if (z >= 0) {
			for (int i = z + 1; i < n; i++) nd.push_back(dis[i]);
		}

		sort(nd.begin(), nd.end());

		for (int i = nd.size() - 1; i >= 0; i--) {
			if (l > 0) {
				ans += nd[i];
				l--;
			}
			else {
				ans += nd[i] * 2;
			}
		}

		printf("Case #%d: %lld\n", Ti, ans);
	}
	return 0;
}
