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
char buffer[10000];

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

int main(int argc, char** argv) {
	freopen("CodeJam.in", "r", stdin);
	freopen("CodeJam.out", "w", stdout);

	char bufferN[100];
	char bufferM[100];

	int nT; scanf("%d", &nT);
	for (int _t = 0 ; _t < nT; ++_t) {
		int a, b; scanf("%d %d", &a, &b);
		int total = 0;
		for (int i = a; i <= b; ++i) {
			sprintf(bufferN, "%d", i);
			sprintf(bufferM, "%d", i);
			string n = bufferN, m = bufferM;
			set<int> used;

			for (int j = 0; j < n.size(); ++j) {
				m.insert(m.begin(), m[m.size() - 1]);
				m.resize(m.size() - 1);

				const int intN = atoi(n.c_str());
				const int intM = atoi(m.c_str());

				if (m[0] == '0') continue;
				if (intN >= intM) continue;
				if (intM > b) continue;
				if (used.count(intM)) continue;
				used.insert(intM);

				total++;
			}
		}

		printf("Case #%d: %d\n", _t + 1, total);
	}

	return 0;
}
