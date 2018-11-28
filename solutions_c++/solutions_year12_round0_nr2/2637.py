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
void output(int ans)
{
	cout << "Case #" << testcase++ << ": " << ans << endl;
}

bool maybe_surprising(int x)
{
	return 2<=x && x<=28;
}

bool mustbe_surprising(int x)
{
	if (!maybe_surprising(x)) return false;
	rep(i, 11) if (i+i+i==x || i+i+i+1==x || i+i+1+i+1==x) return false;
	return true;
}

int maximum(int x)
{
	if (x == 0) return 0;
	if (x == 1) return 1;
	rep(i, 9) if (i+i+i+2==x || i+i+1+i+2==x || i+i+2+i+2==x) return i+2;
	if (x >= 29) return 10;
}

int maximum2(int x)
{
	rep(i, 11) if (i+i+i==x) return i;
	rep(i, 10) if (i+i+i+1==x || i+i+1+i+1==x) return i+1;
}	

int main()
{
	ios_base::sync_with_stdio(0);

	/*
	rep(i, 31) {
		cout << i << ": " << maximum(i) << ", " << maximum2(i) << endl;
	}
	return 0;
	*/

	int T; cin >> T;
	while (T--) {
		int n, s, p;
		cin >> n >> s >> p;
		vector<int> v(n);
		rep(i, n) cin >> v[i];

		int res = 0;
		rep(i, 1<<n) {
			int cnt = 0;
			int scnt = 0;
			rep(j, n) {
				if (i&(1<<j)) {
					if (!maybe_surprising(v[j])) { cnt=0; break; }
					scnt++; 
					if (maximum(v[j]) >= p) cnt++;
				}
				else {
		//			if (mustbe_surprising(v[j])) { cnt=0; break; }
					if (maximum2(v[j]) >= p) cnt++;
				}
			}
			if (scnt == s) res = max(res, cnt);
		}
		output(res);
	}
	return 0;
}
