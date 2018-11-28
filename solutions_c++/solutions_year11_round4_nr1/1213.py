#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define FILENAME	"A-large-0"

#define rep(a, b, i)	for (int i = a; i < b; ++i)

int w[1024], b[1024], e[1024];
pair<double, double> walk[1024];

int main() {
	ifstream in(FILENAME ".in");
	ofstream out(FILENAME ".out");

	int T;
	in >> T;
	rep (1, T+1, test) {
		double ans = 0;
		int x, s, r, t, n;
		in >> x >> s >> r >> t >> n;
		rep(0, n, i)
			in >> b[i] >> e[i] >> w[i];

		int x1 = x;
		rep (0, n, i) {
			x1 -= e[i] - b[i];
			walk[i].first = w[i] + s;
			walk[i].second = e[i] - b[i];
		}
		walk[n].first = s;
		walk[n].second = x1;

		sort(walk, walk + n + 1);
		double t1 = t;
		rep(0, n+1, i) {
			double v = walk[i].first + r - s;
			double t2 = min(t1, walk[i].second / v);
			t1 -= t2;
			ans += t2;
			ans += (walk[i].second - t2 * v) / walk[i].first;
		}

		out << "Case #" << test << ": ";
		out.setf(ios::fixed);
		out.precision(7);
		out << ans;
		out << endl;
	}

	return 0;
}