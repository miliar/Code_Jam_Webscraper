#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

typedef vector<int>	vi;
typedef vector<vi>	vvi;
typedef vector<string>	vs;
typedef stringstream	ss;
typedef long long	ll;
typedef pair<int, int>	ii;
typedef vector<ii>	vii;
typedef pair<double, double>	dd;
typedef pair<int, double>	id;
typedef pair<double, int>	di;
typedef	map<string, int>	dict;

#define sz(v)		((int)v.size())
#define	fn(n, i)	for (int i = 0; i < (n); ++i)
#define	fv(v, i)	for (int i = 0; i < sz(v); ++i)
#define pb(a)		push_back(a)
#define	mp(a, b)	make_pair(a, b)
#define	all(v)		v.begin(), v.end()

char buff[2048];
int used[200];

inline int mins(string& s) {
	return (s[0] - '0') * 600 + (s[1] - '0') * 60 + (s[3] - '0') * 10 + (s[4] - '0');
}

int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int N;
	string s1, s2;
	cin >> N;
	fn(N, test) {
		int ansa = 0, ansb = 0;
		int t, na, nb;
		cin >> t >> na >> nb;
		vii a, b;
		fn (na, i) {
			cin >> s1 >> s2;
			a.pb(mp(mins(s1), 1));
			b.pb(mp(mins(s2) + t, -1));
		}
		fn (nb, i) {
			cin >> s1 >> s2;
			b.pb(mp(mins(s1), 1));
			a.pb(mp(mins(s2) + t, -1));
		}
		sort(all(a));
		sort(all(b));
		int cur = 0;
		fv (a, i) {
			cur -= a[i].second;
			if (cur < 0) {
				++cur;
				++ansa;
			}
		}
		cur = 0;
		fv (b, i) {
			cur -= b[i].second;
			if (cur < 0) {
				++cur;
				++ansb;
			}
		}
		cout << "Case #" << test+1 << ": " << ansa << ' ' << ansb << endl;
	}

	return 0;
}
