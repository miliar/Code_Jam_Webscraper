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

struct Solver
{
	bool simulate(double distance, vector < pair <int, int> >& coordinates, double D) {
		int idx = 0, N = size(coordinates);
		bool unused = true;
		double target = 0.0;
		while (idx < N) {
			pair <int, int> current = coordinates[idx++];
			double P = current.first; int V = current.second;
			if (unused == true) {
				target = P - distance;
				V--;
				unused = false;
			}
			for (int i = 0; i < V; ++i) {
				double current = P;
				double newPosition = target + D;
				if (newPosition <= current) {
					if (current - newPosition <= distance)
						target = newPosition;
					else
						target = current - distance;
				}
				else if (newPosition >= current && newPosition - current <= distance)
					target = newPosition;
				else {
					return false;
				}
			}
		}
		return true;
	}
	double solve(vector < pair <int, int> >& coordinates, double D) {
		sort(coordinates.begin(), coordinates.end());
		if (simulate(0, coordinates, D))
			return 0.0;
		double low = 0, high = (1e20);
		for (int iter = 0; iter < 512; ++iter) {
			double mid = (low + high) / 2.0;
			if (simulate(mid, coordinates, D))
				high = mid;
			else
				low = mid;
		}
		return (low + high) / 2.0;
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
		int C = rInt(), D = rInt();
		vector < pair <int, int> > coordinates(C);
		for (int input = 0; input < C; ++input) {
			int P = rInt(), V = rInt();
			coordinates[input] = make_pair(P, V);
		}
		Solver solver;
		double timeTaken = solver.solve(coordinates, D);
		printf("Case #%d: %.12Lf\n", test, timeTaken);
		fprintf(stderr, "Test #%d\n", test);
	}
	return 0;
}

// Powered by PhoenixAI
