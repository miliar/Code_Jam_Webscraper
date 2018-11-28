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

bool satisfies(int N, int D, int G, int pD, int pG) {
	if ((G * pG) % 100 == 0 && (D * pD) % 100 == 0) {
		int winG = (G * pG) / 100;
		int winD = (D * pD) / 100;
		int lossD = D - winD;
		int lossG = G - winG;
		return winG >= winD && lossD <= lossG;
	}
	return false;
}

int main()
{
	const bool contest = true;
	if (contest == true) {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	int nTest = rInt();
	for (int test = 1; test <= nTest; ++test) {
		int N = rInt(), pD = rInt(), pG = rInt();
		bool result = false;
		if (pD == 0) {
			if (pG == 100)
				result = false;
			else
				result = true;
		}
		else {
			if (pG == 0) result = false;
			else {
				//for (int n = N; n >= 0 && !result; --n)
					for (int d = N; d > 0 && !result; --d)
						for (int g = 1000 * d; g >= d && !result; --g)
							if (satisfies(N, d, g, pD, pG)) {
								result = true;
							}
			}
		}
		printf("Case #%d: %s\n", test, result == true? "Possible" : "Broken");
	}
	return 0;
}

// Powered by PhoenixAI
