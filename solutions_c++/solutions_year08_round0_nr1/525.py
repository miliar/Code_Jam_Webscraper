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
#define UNIQUE(c) c.resize(unique(ALL(c), c.begin()) - c.begin())

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
VS split(string s, string delim) {
  VS res; int pos;
  while ((pos = s.find(delim)) != -1) {
    res.push_back(s.substr(0, pos));
    s.erase(0, pos + delim.size());
  } res.push_back(s);
  return res;
}
////////////////////////////////////////////////////////////////////////////////

int nQueries, nSearchs;
VI queries;

int memo[1001][101];

int best(int pos, int s) {
	if (pos == nQueries) return 0;
	if (memo[pos][s] != -1) return memo[pos][s];
	if (queries[pos] != s) return memo[pos][s] = best(pos + 1, s);
	memo[pos][s] = 0x3fffffff;
	for (int i = 0; i < nSearchs; ++i) {
		if (s == i) continue;
		memo[pos][s] = min(memo[pos][s], best(pos + 1, i) + 1);
	}
	return memo[pos][s];
}

int main(int argc, char** argv) {
	freopen("CodeJam.in", "r", stdin);
	freopen("CodeJam.out", "w", stdout);

	char buffer[10000];
	fgets(buffer, 10000, stdin);
	int nT; sscanf(buffer, "%d", &nT);
	for (int t = 0 ; t < nT; ++t) {
		fgets(buffer, 10000, stdin);
		sscanf(buffer, "%d", &nSearchs);
		map<string, int> search;
		for (int i = 0; i < nSearchs; ++i) {
			fgets(buffer, 10000, stdin);
			buffer[strlen(buffer) - 1] = 0;
			search[buffer] = i;
		}

		fgets(buffer, 10000, stdin);
		sscanf(buffer, "%d", &nQueries);
		queries.resize(nQueries);
		for (int i = 0; i < nQueries; ++i) {
			fgets(buffer, 10000, stdin);
			buffer[strlen(buffer) - 1] = 0;
			queries[i] = search[buffer];
		}

		memset(memo, -1, sizeof(memo));
		int min_ = 0x3fffffff;
		for (int i = 0; i < nSearchs; ++i) {
			min_ = min(min_, best(0, i));
		}
		printf("Case #%d: %d\n", t + 1, min_);
	}

	return 0;
}
