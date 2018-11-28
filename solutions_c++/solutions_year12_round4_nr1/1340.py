#include <mymacro.h>
using namespace std;

class Solver {
public:
	string solve() {
		int D[10010], L[10010];
		int N;
		cin >> N;
		rep(i, N) cin >> D[i] >> L[i];
		cin >> D[N];
		priority_queue<PI> Q;
		Q.push(PI(0, 0));
		while(!Q.empty()) {
			PI pi = Q.top(); Q.pop();
			int n = pi.fi;
			if (n == N)
				return "YES";
			int bpos = pi.se;
			int md = min(bpos + 2*(D[n] - bpos), D[n] + L[n]);
			for(int i = lower_bound(D, D+N, bpos)-D; D[i] <= md && i <= N; i++)
				if (i > n) {
					Q.push(PI(i, D[n]));
				}
		}
		return "NO";
	}
};

int main() {
	int T; cin >> T;
	for(int t=1; t<=T; t++) {
		Solver sol;
		cout << "Case #" << t << ": " << sol.solve() << endl;
	}
	return 0;
}

