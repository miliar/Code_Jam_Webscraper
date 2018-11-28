#include <iostream>
#include <vector>
using namespace std;

class Hoge {
	int R, k, N;
	vector<int> g;
	vector< pair<int,int> > memo;
public:
	Hoge(int R, int k, const vector<int>& g) : R(R), k(k), g(g), N(g.size()), memo(N,make_pair(-1,-1)) {}
	int f(long long& ans, int pos) {
		if (memo[pos].first >= 0) {
			ans += memo[pos].first;
			return memo[pos].second;
		}
		int p = pos;
		int num = 0;
		for (;;) {
			if (num+g[p] > k) break;
			num += g[p];
			++ p;
			if (p == N) p = 0;
			if (p == pos) break;
		}
		ans += num;
		memo[pos] = make_pair(num, p);
		return p;
	}
	long long  func() {
		long long ans = 0;
		int pos = 0;
		for (int i = 0; i < R; ++ i) {
			pos = f(ans, pos);
		}
		return ans;
	}
};

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++ i) {
		int R, k, N;
		cin >> R >> k >> N;
		vector<int> g(N);
		for (int j = 0; j < N; ++ j) {
			cin >> g[j];
		}
		Hoge hoge(R, k, g);
		cout << "Case #" << i << ": " << hoge.func() << endl;
	}
}
