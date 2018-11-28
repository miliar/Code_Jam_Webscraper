#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;

class swingingwild
{
	private:
		int n;
		vector<pii> vines;
		int d;

		bool sol;

	public:
		swingingwild() {}

		void input() {
			scanf("%d", &n);
			vines.resize(n);
			for (int f = 0; f < n; ++f) {
				scanf("%d%d", &(vines.at(f).first), &(vines.at(f).second));
			}
			scanf("%d", &d);
		}

		void solve() {
			vines.push_back(pii(d, 0));
			vector<int> bpd(n + 1, -1);
			bpd.at(0) = vines.at(0).first;
			for (int f = 0; f < n; ++f) {
				for (int g = f + 1; g <= n; ++g) {
					if (vines.at(g).first - vines.at(f).first <= bpd.at(f)) {
						bpd.at(g) = max(bpd.at(g), min(vines.at(g).first - vines.at(f).first, vines.at(g).second));
					}
				}
			}
			sol = (bpd.back() > -1);
		}

		void output(int caseno) {
			printf("Case #%d: %s\n", caseno, (sol? "YES" : "NO"));
		}
};

int main(void) {
	int nt;
	scanf("%d", &nt);
	for(int znj = 1; znj <= nt; ++znj) {
		swingingwild task;
		task.input();
		task.solve();
		task.output(znj);
	}
	return 0;
}
