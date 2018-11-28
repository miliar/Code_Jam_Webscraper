#if 1
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <functional>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <ctime>
#include <cassert>
#include <sstream>
#include <iostream>
#include <bitset>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"

namespace misc
{
	using std::ostringstream;
	using std::istringstream;
	using std::string;
	using std::max;

	// description: absolute value by max(a, -a)
	// tested: uva10367
	template<class T> T xabs(const T &a)
	{ return max(a, -a); }

	// description: anything to string (anything what ostream support)
	// tested: uva10367
	template<class T> string i2s(const T &num)
	{ ostringstream os; os << num; return os.str(); }

	// description: string to anything what istream support
	// tested: uva10367
	template<class T> T s2i(const string &s)
	{ T num; istringstream is(s); is >> num; return num; }
}


bool is_recycled(int n, int m)
{
	string s = misc::i2s(n);
	string t = misc::i2s(m);

	for(int i = 0; i + 1 < s.length(); ++i)
	{
		s += s[0];
		s.erase(0, 1);
		if(s == t)
			return true;
	}
	return false;
}
void solve(int test)
{
	int a, b;
	cin >> a >> b;
	int cnt = 0;
	for(int n = a; n <= b; ++n)
		for(int m = n + 1; m <= b; ++m)
			if(is_recycled(n, m))
				cnt++;
	cout << "Case #" << test << ": " << cnt << endl;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin);freopen(NAME ".out","w",stdout);

	int tests;
	cin >> tests;
	for(int test = 1; test <= tests; ++test)
		solve(test);

	return 0;
}
/*************************
*************************/
#endif
