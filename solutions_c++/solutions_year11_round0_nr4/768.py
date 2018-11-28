#include <algorithm>
#include <vector>

using namespace std;

const int MAX_N = 20;

double fact(int N) {
	double res = 1;
	for (int i = 2; i <= N; i ++) {
		res *= i;
	}
	return res;
}

bool ready[MAX_N];
double dp[MAX_N];
double rec(int N) {
	if (N == 1) {
		return 0;
	}
	double &res = dp[N];
	if (ready[N]) {
		return res;
	}
	double coef = 1 / fact(N);
	vector<int> v;
	for (int i = 0; i < N; i ++) {
		v.push_back(i);
	}
	res = 0;
	double k = 0;
	vector<int> count(N + 1, 0);
	do {
		vector<bool> used(N, false);
		vector<int> curCount(N + 1, 0);
		for (int i = 0; i < v.size(); i ++) {
			if (!used[i]) {
				int size = 0;
				int pos = i;
				while (!used[pos]) {
					used[pos] = true;
					size ++;
					pos = v[pos];
				}
				count[size] ++;
				curCount[size] ++;
				if (size == N) {
					k += coef;
				} else {
					res += coef * rec(size);
				}
			}
		}
		void;
	} while (next_permutation(v.begin(), v.end()));
	res = (1 + res) / (1 - k);
	ready[N] = true;
	return res;
}

int T;
int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++) {
		int N;
		scanf("%d", &N);
		int res = N;
		for (int i = 0; i < N; i ++) {
			int tmp;
			scanf("%d", &tmp);
			if (tmp == i + 1) {
				res --;
			}
		}
		printf("Case #%d: %d\n", t, res);
	}
}