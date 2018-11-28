#include <mymacro.h>
using namespace std;

class Solver {
public:
	int solve() {
		int N, S, p;
		cin >> N >> S >> p;
		int ans = 0;
		rep(i, N) {
			int t; cin >> t;
			int sur = t / 3 + t % 3 + (t % 3 == 0 ? 1 : 0);
			int nor = t / 3 + t % 3 - (t % 3 == 2 ? 1 : 0);
			if (nor >= p) ans++;
			else if (sur >= p && S >= 1 && t != 0) ans++, S--;
		}
		return ans;
	}
};

int main() {
	int T; scanf("%d\n", &T);
	for(int t=1; t<=T; t++) {
		Solver sol;
		cout << "Case #" << t << ": " << sol.solve() << endl;
	}
	return 0;
}

