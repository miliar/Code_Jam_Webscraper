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

typedef long double data;

struct Solver
{
	void solve(vector <string>& vs) {
		int N = size(vs);
		vector <data> wp(N, 0), owp(N, 0), oowp(N, 0);
		for (int player = 0; player < N; ++player) {
			data ones = 0, zero = 0;
			for (int col = 0; col < N; ++col)
				if (vs[player][col] == '1') ++ones;
				else if (vs[player][col] == '0') ++zero;
			wp[player] = ones / (ones + zero);
			data total = 0;
			int howMany = 0;
			for (int opponent = 0; opponent < N; ++opponent) {
				ones = 0, zero = 0;
				if (vs[player][opponent] != '.') {
					++howMany;
					for (int r = 0; r < N; ++r)
						if (r != player)
							if (vs[opponent][r] == '1') ++ones;
							else if (vs[opponent][r] == '0') ++zero;
					total += (ones / (ones + zero));
				}
			}
			owp[player] = total / howMany;
		}
		for (int player = 0; player < N; ++player) {
			data sum = 0;
			int howMany = 0;
			for (int opponent = 0; opponent < N; ++opponent)
				if (vs[player][opponent] != '.')
					sum += owp[opponent], howMany++;
			oowp[player] = sum / howMany;
		}
		for (int player = 0; player < N; ++player) {
			double score = (wp[player] / 4.0) + (owp[player] / 2.0) + (oowp[player] / 4.0);
			printf("%.12Lf\n", (double) score);
		}
	}
};

int main()
{
	const bool contest = true;
	if (contest == true) {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	int nTest = rInt();
	for (int test = 1; test <= nTest; ++test) {
		int N = rInt();
		vector <string> vs(N);
		for (int i = 0; i < N; ++i)
			vs[i] = rStr();
		printf("Case #%d:\n", test);
		Solver solver;
		solver.solve(vs);
	}
	return 0;
}

// Powered by PhoenixAI
