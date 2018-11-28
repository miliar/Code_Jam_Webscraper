#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>

using namespace std;

#define BUG(x) if (DEBUG) cout << __LINE__ << ": " << #x << " = " << x << endl
#define LET(x, a) __typeof(a) x = a
#define FOREACH(it, v) for(LET(it, (v).begin()); it != (v).end(); ++it)

typedef long long LL;

template <class T> inline int size(const T& c) {return (int) c.size();}
int rInt() {int nT = -1; scanf("%d", &nT); return nT;}
string rStr() {char nStr[1 << 20] = ""; scanf("%s", nStr); return nStr;}
LL rLL() {LL nT = -1; scanf("%lld", &nT); return nT;}
inline LL two(int x) {return (1LL << (x));}
template <class T> ostream& operator << (ostream& o, const vector <T>& v)
{o << "{"; FOREACH(it, v) o << *it << ","; return o << "}";}
template <class A, class B> ostream& operator << (ostream& o, const pair <A, B>& p)
{o << "("; o << p.first << "," << p.second << ")"; return o;}

const bool DEBUG = true;
const double EPS = 1e-8;
const int INF  = 1000000000;
const LL INFLL = 1000000000000000000LL;

int main()
{
	const bool contest = true;
	if (contest == true) {
		freopen("input.txt", "r", stdin);
		freopen("outputLarge.txt", "w", stdout);
	}
	int nTest = rInt();
	for (int test = 1; test <= nTest; ++test) {
		int N = rInt();
		vector <int> cost(N);
		for (int i = 0; i < N; ++i)
			cost[i] = rInt();
		int result = 0;
		for (int i = 0; i < N; ++i)
			result ^= cost[i];
		if (result != 0)
			printf("Case #%d: NO\n", test);
		else
			printf("Case #%d: %d\n", test, accumulate(cost.begin(), cost.end(), 0) - *min_element(cost.begin(), cost.end()));
	}
	return 0;
}

// Powered by PhoenixAI
