#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

const int MAX = 1000000;
int T, D, K;
ll sequ[100];
bool prime[MAX+1];

ll pow_mod(ll a, ll e, ll m) {
	if (e == 0) return 1;
	ll v = pow_mod(a, e/2, m);
	v = (v * v) % m;
	if (e % 2) v = (v * a) % m;
	return v;
}

ll inv(ll v, ll m) {
	return pow_mod(v, m-2, m);
}

int main() {
	prime[0] = prime[1] = false;
	FOR(i, 2, MAX+1) prime[i] = true;
	for (int i = 2; i*i <= MAX; i++) {
		if (!prime[i]) continue;
		for (int j = i*i; j <= MAX; j += i) prime[j] = false;
	}
	cin >> T;
	FOR(cs, 1, T+1) {
		cin >> D >> K;
		FOR(i, 0, K) cin >> sequ[i];
		cout << "Case #" << cs << ": ";
		if (K == 1) {
			cout << "I don't know." << endl;
		} else {
			if (sequ[0] == sequ[1]) {
				cout << sequ[0] << endl;
			} else {
				if (K == 2) {
					cout << "I don't know." << endl;
				} else {
					ll x = sequ[0], y = sequ[1], z = sequ[2];
					ll Max = 0;
					FOR(i, 0, K) Max = max(Max, sequ[i]);
					ll lim = 1;
					FOR(i, 0, D) lim *= 10;
					ll res = -1;
					for (ll p = 2; p <= MAX; p++) {
						if (!prime[p] || Max >= p) continue;
						if (p > lim) break;
						ll a = (inv(((y-x)%p+p)%p, p) * (((z-y)%p+p)%p))%p;
						ll b = ((y - a*x)%p+p)%p;
						//ll s = x;
						bool poss = true;
						FOR(i, 1, K) {
							if ((a*sequ[i-1]+b) % p != sequ[i]) {
								poss = false;
								break;
							}
						}
						if (!poss) continue;
						ll v = (a*sequ[K-1]+b)%p;
						if (res != -1 && res != v) {
							res = -1;
							break;
						}
						res = v;
					}
					if (res == -1) {
						cout << "I don't know." << endl;
					} else {
						cout << res << endl;
					}
				}
			}
		}
	}
	return 0;
}

