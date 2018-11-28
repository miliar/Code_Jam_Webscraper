#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

double X, S, R, t;
int n;
const double eps = 1e-8;

struct way {
		double length;
		double s;
		bool operator < (const way& rhs) const {
				return s < rhs.s;
		}
};

vector<way> ways;

int main() {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
		int r;
		int case_no = 0;
		scanf("%d", &r);
		while (r--) {
				scanf("%lf %lf %lf %lf %d", &X, &S, &R, &t, &n);
				ways.clear();
				way tmp;
				double total = 0;
				for (int i = 0; i < n; ++i) {
						double b, e;
						scanf("%lf %lf %lf", &b, &e, &tmp.s);
						tmp.length = e - b;
						ways.push_back(tmp);
						total += tmp.length;
				}
				tmp.length = X - total;
				tmp.s = 0;
				ways.push_back(tmp);
				sort(ways.begin(), ways.end());
				double sol = 0.0;
				for (int i = 0; i < (int)ways.size(); ++i) {
						double d = ways[i].length;
						double ss = ways[i].s;
						double tt = ways[i].length / (double)(ways[i].s + R);
						tt = min(t, tt);
						t -= tt;
						sol += tt;
						ways[i].length -= tt * (ways[i].s + R);
						d -= tt * (ways[i].s + R);
						sol += ways[i].length / (double)(ways[i].s + S);
				}
				printf("Case #%d: %.7lf\n", ++case_no, sol);
		}
		return 0;
}
