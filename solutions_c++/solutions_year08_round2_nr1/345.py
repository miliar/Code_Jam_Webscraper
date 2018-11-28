#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz size()
#define iss istringstream
#define oss ostringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vs vector<string>

using namespace std;

int rem[3][3];
int buvo[3][3][3][3][3][3];

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int tests;
	cin >> tests;
	for(int test = 1; test <= tests; test++) {
		memset(rem, 0, sizeof(rem));
		int n;
		cin >> n;
		LL A, B, C, D, x0, y0, M;
		cin >> A >> B >> C >> D >> x0 >> y0 >> M;
		LL X = x0, Y = y0;
		rem[X%3][Y%3]++;
		//cout << X << ' ' << Y << endl;
		for(int i = 1; i <= n - 1; i++) {
			X = (A*X + B)%M;
			Y = (C*Y + D)%M;
			//cout << X << ' ' << Y << endl;
			rem[X%3][Y%3]++;
		}
		
		LL ans = 0;
		memset(buvo, 0, sizeof(buvo));
		fr(x1, 3) fr(x2, 3) {
			fr(y1, 3) fr(y2, 3) {
				int x3 = (6 - x1 - x2)%3;
				int y3 = (6 - y1 - y2)%3;
				vector<pii> t;
				t.pb(mp(x1, y1));
				t.pb(mp(x2, y2));
				t.pb(mp(x3, y3));
				sort(t.begin(), t.end());
				if(buvo[t[0].st][t[0].nd][t[1].st][t[1].nd][t[2].st][t[2].nd]) continue;
				buvo[t[0].st][t[0].nd][t[1].st][t[1].nd][t[2].st][t[2].nd] = 1;
			//	cout << x1 << ' ' << y1 << "     " << x2 << ' ' << y2 << "      " << x3 << ' ' << y3 << endl;
				set<pii> s;
				s.insert(mp(x1, y1));
				s.insert(mp(x2, y2));
				s.insert(mp(x3, y3));
				LL a = rem[x1][y1];
				LL b = rem[x2][y2];
				LL c = rem[x3][y3];
			//	cout << a << ' ' << b << ' ' << c << endl;
			//	cout << ans << endl;
				if(s.size() == 1) ans += a*(b - 1)*(c - 2)/6;
			//	cout << ans << endl;
		/*		if(s.size() == 2) {
					if(x1 == x2 && y1 == y2) ans += c*a*(b - 1)/2;
					cout << ans << endl;
					if(x1 == x3 && y1 == y3) ans += b*a*(c - 1)/2;
					cout << ans << endl;
					if(x2 == x3 && y2 == y3) ans += a*b*(c - 1)/2;
					cout << ans << endl;
				} */
				if(s.size() == 3) ans += a*b*c;
			//	cout << ans << endl;
			//	cout << endl;
			}
		}
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}
