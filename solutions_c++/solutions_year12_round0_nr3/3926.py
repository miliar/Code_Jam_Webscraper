#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>

using namespace std;

#define forab(i, a, b) for (int i = a; i < int(b); ++i)
#define fordab(i, a, b) for (int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab (i, 0, n)
#define ford(i, n) fordab (i, 0, n)
#define forv(i, a) forn (i, a.size())

int strtoint(string s) {
	int res = 0;
	ford (i, s.size()) {
		res *= 10;
		res += s[i];
	}
	return res;
}

string inttostr(int a) {
	string res = "";
	while (a) {
		res += a % 10;
		a /= 10;
	}
	return res;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	forn (q, t) {
		int a, b;
		cin >> a >> b;
		++b;
		int ans = 0;
		forab (i, a, b) {
			string s, t;
			s = inttostr(i);
			t = s;
			set<int> st;
			forv (j, s) {
				t = t.substr(1, t.size() - 1) + t[0];
				int x = strtoint(t);
				if (t[t.size() - 1] && a <= x && x < i) {
					st.insert(x);
				}
			}
			ans += st.size();
			st.clear();
		}
		cerr << q << endl;
		cout << "Case #" << q + 1 << ": " << ans << "\n";
	}
}
