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

class LessFunctor {
public:
	bool operator () (const pair< int, PII >& p1, const pair< int, PII >& p2) {
		return p1.second.first == p2.second.first ? p1.second.second < p2.second.second : p1.second.first < p2.second.first;
	}
};

class LessFunctor2 {
public:
	bool operator () (const PII& p1, const PII& p2) {
		return p1.second < p2.second;
	}
};

int main(int argc, char** argv) {
	freopen("CodeJam.in", "r", stdin);
	freopen("CodeJam.out", "w", stdout);

	int nT; scanf("%d", &nT);
	for (int t = 0 ; t < nT; ++t) {
		int turn, na, nb; scanf("%d %d %d", &turn, &na, &nb);
		vector< pair< int, PII > > v;
		for (int i = 0; i < na; ++i) {
			int h0, h1, m0, m1;
			scanf("%d:%d %d:%d", &h0, &m0, &h1, &m1);
			v.push_back(make_pair(0, PII(h0*60 + m0, h1*60 + m1)));
		}
		for (int i = 0; i < nb; ++i) {
			int h0, h1, m0, m1;
			scanf("%d:%d %d:%d", &h0, &m0, &h1, &m1);
			v.push_back(make_pair(1, PII(h0*60 + m0, h1*60 + m1)));
		}
		sort(ALL(v), LessFunctor());
		
		int total[2] = {0, 0};
		vector<PII> disp;
		for (int i = 0; i < v.size(); ++i) {
			bool isDisp = false;
			sort(ALL(disp), LessFunctor2());
			for (int j = 0; j < disp.size(); ++j) {
				if (disp[j].first == v[i].first) {
					if (disp[j].second <= v[i].second.first) {
						disp.erase(disp.begin() + j);
						isDisp = true;
						break;
					}
				}
			}
			if (!isDisp) total[v[i].first]++;
			disp.push_back(PII(1 - v[i].first, v[i].second.second + turn));
		}

		printf("Case #%d: %d %d\n", t + 1, total[0], total[1]);
	}

	return 0;
}
