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

int testcase = 1;
void output(int x)
{
	cout<<"Case #" << testcase++ << ": " << x << endl;
}

int main()
{
	ios_base::sync_with_stdio(0);


	int T; cin >> T;
	while (T--) {
		int a, b; cin >> a >> b;
		int res = 0;
		REP(x, a, b+1) {
			ostringstream os; os << x;
			string s = os.str();
			string t = s;
			int n = atoi(s.c_str());
			map<int, int> used;
			rep(i, s.size()) {
				rotate(t.begin(), t.begin()+1, t.end());
				int m = atoi(t.c_str());
				if (a <= n && n < m && m <= b && !used[m]) {
					used[m] = 1;
					res++;
				}
			}
		}
		output(res);
	}

	return 0;
}
