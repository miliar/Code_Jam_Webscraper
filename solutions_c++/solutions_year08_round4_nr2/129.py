#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz size()
#define iss istringstream
#define oss ostringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vs vector<string>

using namespace std;

pair<LL, LL> factor(LL A, LL N, LL M) {
	pair<LL, LL> ans = mp(-1, -1);
	for(int i = 1; i <= N; i++) {
		if(A%i == 0 && A/i <= M) {
			ans = mp(i, A/i);
			return ans;
		}
	}
	return ans;
}

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int tests;
	cin >> tests;
	fr(test, tests) {
		LL N, M, A;
		cin >> N >> M >> A;
		pair<LL, LL> F = mp(-1, -1);
		pair<LL, LL> S = mp(-1, -1);
		int k = 0;
		if(A > M*N) {
			cout << "Case #" << test + 1 << ": IMPOSSIBLE" << endl;
			continue;
		}
		for(; k <= min(10000, (int)(N*M)); k++) {
			pair<LL, LL> f = factor(A + k, N, M);
			if(!(f.st == -1 && f.nd == -1)) {
				F = mp(f.st, 1);
				S = mp(k, f.nd);
				break;
			}
		}
		if(k == 10000 + 1 && k != N*M + 1) cout << "FAILURE" << endl;
		if(F.st == -1 && F.nd == -1) cout << "Case #" << test + 1 << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << test + 1 << ": " << 0 << ' ' << 0 << ' ' << F.st << ' ' << F.nd << ' ' << S.st << ' ' << S.nd << endl;
	}
	return 0;
}
