#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define contains(c, v) binary_search(all(c), v)

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef long double ld;

string solve(vi v)
{
	int s = 0;
	int ss = 0;
	forv(i, v) s ^= v[i], ss += v[i];
	if (s) {
		return "NO";
	}
	ss = ss - *min_element(all(v));
	string res;
	while (ss) res.pb(ss%10+'0'), ss/=10;
	reverse(all(res));
	return res;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int tn; cin >> tn;
	forn(it, tn) {
		int n; cin >> n;
		vi v(n);
		forn(i, n) cin >> v[i];
		cout << "Case #" << it+1 << ": " << solve(v) << endl;
	}

	return 0;
}
