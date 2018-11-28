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

	int nT; scanf("%d", &nT);
	for (int t = 0 ; t < nT; ++t) {
		int n; LL l, h; scanf("%d %lld %lld", &n, &l, &h);
		vector<LL> v(n);
		for (int i = 0; i < n; ++i) {
			scanf("%lld", &v[i]);
		}

		LL best = -1;
		sort(ALL(v));
		for (int i = l; i <= h; ++i) {
			bool valid = true;
			for (int j = 0; j < n; ++j) {
				if (i == 0 || v[j] == 0) continue;
				if ((i >= v[j] && i % v[j] != 0) || 
					(i < v[j] && v[j] % i != 0)) {
						valid = false;
						break;
				}
			}
			if (valid) {
				best = i;
				break;
			}
		}

		printf("Case #%d: ", t + 1);
		if (best == -1) printf("NO\n");
		else printf("%lld\n", best);
	}

	return 0;
}
