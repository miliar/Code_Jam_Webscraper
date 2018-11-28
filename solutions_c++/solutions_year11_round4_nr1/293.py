#pragma comment(linker, "/STACK:512000000")

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef long double ld;

typedef vector<int> VI;
typedef vector<bool> VB;
typedef pair<int, int> Edge;
typedef vector<vector<Edge> > Graph;

void init()
{
	freopen("input.txt", "rt", stdin);
}

struct Runway
{
	ll b, e, w;
};

bool operator<(const Runway& a, const Runway& b) {
	return a.b < b.b;
}

ll RR, SS;
bool cmp(const Runway& a, const Runway& b) {
	return (RR + a.w) * (SS + b.w) > (RR + b.w) * (SS + a.w);
}

int main()
{
	//init();

	int tc; cin >> tc;
	cout.precision(9);
	cout << fixed;
	forn(it, tc) {
		ll X, S, R, T, N;
		cin >> X >> S >> R >> T >> N;
		vector<ll> B(N), E(N), w(N);
		vector<Runway> rw;
		forn(i, N) {
			cin >> B[i] >> E[i] >> w[i];
			Runway r = {B[i], E[i], w[i]};
			rw.pb(r);
		}
		sort(all(rw));
		vector<Runway> tmp;
		forv(i, rw) {
			if (i == 0 && rw[i].b != 0) {
				Runway r = {0, rw[i].b, 0};
				tmp.pb(r);
			}
			tmp.pb(rw[i]);
			if (i + 1 < (int)rw.size() && rw[i].e < rw[i + 1].b) {
				Runway r = {rw[i].e, rw[i + 1].b, 0};
				tmp.pb(r);
			}
			if (i + 1 == (int)rw.size() && rw[i].e != X) {
				Runway r = {rw[i].e, X, 0};
				tmp.pb(r);
			}
		}
		rw = tmp;
		RR = R;
		SS = S;
		sort(all(rw), cmp);
		const ld EPS = 1e-9;
		ld ans = 0;
		ld restTime = T;
		forv(i, rw) {
			ld t1 = (ld)(rw[i].e - rw[i].b) / (ld)(rw[i].w + R);
			if (restTime > t1 - EPS) {
				ans += t1;
				restTime -= t1;
				if (restTime < EPS) restTime = 0;
			}
			else {
				ans += restTime;
				ld d = (rw[i].w + R) * restTime;
				ld xx = (rw[i].e - rw[i].b - d);
				restTime = 0;
				ans += xx / (rw[i].w + S);
			}
		}
		cout << "Case #" << it + 1 << ": " << ans << endl;
	}

	return 0;
}
