#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <complex>

#define pb push_back
#define mp make_pair
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define tr(c, i) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define rtr(c, i) for (typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); --i)
#define contains(c, x) ((c).find(x) != (c).end())
#define Contains(c, x) (find(all(c), x) != (c).end())
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define rep(i, n) REP(i, 0, (n))
#define To_String to_string< char,std::char_traits<char>,std::allocator<char> >

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

int combine[256][256];
int opposed[256][256];
int main()
{
	ios_base::sync_with_stdio(0);
	int T; cin >> T;
	REP(t, 1, T+1) {
		memset(combine, 0, sizeof(combine));
		memset(opposed, 0, sizeof(opposed));
		int c; cin >> c;
		rep(i, c) {
			string s; cin >> s;
			combine[s[0]][s[1]] = combine[s[1]][s[0]] = s[2];
		}
		int d; cin >> d;
		rep(i, d) {
			string s; cin >> s;
			opposed[s[0]][s[1]] = opposed[s[1]][s[0]] = 1;
		}

		int n; cin >> n;
		string s; cin >> s;
		vector<char> res;
		rep(i, n) {
			if (res.empty()) { res.pb(s[i]); continue; }
			if (combine[res.back()][s[i]])
				res[res.size()-1] = combine[res.back()][s[i]];
			else
				res.pb(s[i]);
			rep(j, res.size()) REP(k, j+1, res.size()) {
				if (opposed[res[j]][res[k]]) {
					res.clear();
					break;
				}
			}
		}
		ostringstream os;
		rep(i, res.size()) os << ", " << res[i];
		string r = os.str();
		cout << "Case #" << t << ": ";
		cout << "[" << (r.size() > 2 ? r.substr(2) : "") << "]" << endl;
	}
	return 0;
}
