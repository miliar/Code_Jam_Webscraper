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

int main()
{
	ios_base::sync_with_stdio(0);
	int T; cin >> T;
	REP(t, 1, T+1) {
		int n; cin >> n;
		queue<int> orange, blue;
		queue<pair<char, int> > a;
		rep(i, n) {
			char c;
			int x;
			cin >> c >> x;
			if (c == 'O') orange.push(x);
			else blue.push(x);
			a.push(mp(c, x));
		}
		int res = 0;
		int o = 1, b = 1;
		while (!a.empty()) {
			char c = a.front().first;
			int x = a.front().second;
			a.pop();

			if (c == 'O') {
				int od = orange.front() > o ? 1 : -1;
				orange.pop();
				while (o != x + od) {
					o += od;
					if (!blue.empty()) {
						int bd = blue.front() > b ? 1 : -1;
						if (b != blue.front()) b += bd;
					}
					res++;
				}
				o -= od;
			}
			else {
				int bd = blue.front() > b ? 1 : -1;
				blue.pop();
				while (b != x + bd) {
					b += bd;
					if (!orange.empty()) {
						int od = orange.front() > o ? 1 : -1;
						if (o != orange.front()) o += od;
					}
					res++;
				}
				b -= bd;
			}
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}
