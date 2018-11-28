#pragma warning (disable:4996)

#include "map"
#include "set"
#include "cmath"
#include "ctime"
#include "queue"
#include "bitset"
#include "cctype"
#include "cstdio"
#include "string"
#include "vector"
#include "climits"
#include "numeric"
#include "sstream"
#include "iostream"
#include "algorithm"
#include "functional"
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<string> VS;
typedef pair<int, int> PII;
#define ALL(c) c.begin(), c.end()
#define INDEX(c, e) lower_bound(ALL(c), e) - c.begin()
#define UNIQUE(c) c.resize(unique(ALL(c)) - c.begin())

////////////////////////////////////////////////////////////////////////////////
const double eps = 5e-9;
int DoubleComp(double a, double b) {
  if (fabs(a - b) < eps) return 0;
  if (b * (1.0 - eps) < a && a < b * (1.0 + eps)) return 0;
  if (b * (1.0 + eps) < a && a < b * (1.0 - eps)) return 0;
  return a < b ? -1 : +1;
}

int sign(int x) {return x < 0 ? -1 : +1;}
int DoubleSign(double x) {return DoubleComp(x, 0.0) < 0 ? -1 : +1;}
int DoubleCast(double x) {return (int)(x + (x < 0.0 ? -eps : +eps));}
int DoubleFloor(double x) {return DoubleCast(floor(x + eps));}
int DoubleCeil(double x) {return DoubleCast(ceil(x - eps));}

double DoubleMin(double a, double b) { return DoubleComp(a, b) < 0 ? a : b; }
double DoubleMax(double a, double b) { return DoubleComp(a, b) > 0 ? a : b; }
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
char buffer[100000];

VS split(string s, string delim) {
  VS res; int pos;
  while ((pos = s.find(delim)) != -1) {
    if (pos) res.push_back(s.substr(0, pos));
    s.erase(0, pos + delim.size());
  } if (!s.empty()) res.push_back(s);
  return res;
}

string getLine() {
  fgets(buffer, sizeof(buffer), stdin); string res(buffer);
  return res.substr(0, res.find_last_not_of("\r\n") + 1);
}
////////////////////////////////////////////////////////////////////////////////

struct point_t {
  int x, y; point_t() {}
  point_t(int x_, int y_) : x(x_), y(y_) {}
};

typedef vector<point_t> polygon_t;
double GetPolygonArea(const polygon_t& polygon) {
  int area = 0;
  for (int k = 0; k < polygon.size(); ++k) {
    const point_t& p0 = polygon[k];
    const point_t& p1 = polygon[(k + 1) % polygon.size()];
    area += p0.x * p1.y - p1.x * p0.y;
  }
  return area;
}

int countGroups(string s) {
	int nGroups = 1;
	for (int i = 1; i < s.size(); ++i) {
		if (s[i] != s[i - 1]) nGroups++;
	}
	return nGroups;
}

string getP(string s, VI v) {
	string res = s;	
	for (int i = 0; i < s.size() / v.size(); ++i) {
		for (int j = 0; j < v.size(); ++j) {
			res[i*v.size() + j] = s[i*v.size() + v[j]];
		}
	}
	return res;
}

int main(int argc, char** argv) {
	freopen("CodeJam.in", "r", stdin);
	freopen("CodeJam.out", "w", stdout);

	int nT = atoi(getLine().c_str());
	for (int t = 0 ; t < nT; ++t) {
		int k = atoi(getLine().c_str());
		string s = getLine();
	
		VI v;
		for (int i = 0; i < k; ++i) v.push_back(i);
		int min_ = INT_MAX;

		do {
			min_ = min(min_, countGroups(getP(s, v)));
		} while (next_permutation(ALL(v))) ;

		printf("Case #%d: %d\n", t + 1, min_);
	}

	return 0;
}
