#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

#define pii pair<int, pair<int, int> >
#define mp make_pair

int fun (priority_queue<int> &A, priority_queue<int> &B, pii q) {
	int dep = q.first;
	int arr = q.second.first;
	B.push(-arr);
	if (!A.empty() && -A.top() <= dep) {
		A.pop();
		return 0;
	}
	return 1;
}

int main () {
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	int test;
	scanf("%d", &test);
	for (int testn = 1; testn <= test; testn++) {
		int T, N, M, res1 = 0, res2 = 0, h1, m1, h2, m2;
		priority_queue<int> A, B;
		vector<pii> Q;
		scanf("%d\n%d %d", &T, &N, &M);
		for (int i = 0; i < N+M; i++) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			Q.push_back(mp(h1*60+m1, mp(h2*60+m2+T, i<N?0:1)));
		}
		sort(Q.begin(), Q.end());
		for (int i = 0; i < Q.size(); i++) {
			if (Q[i].second.second == 0) res1 += fun(A, B, Q[i]);
			else res2 += fun(B, A, Q[i]);
		}
		printf("Case #%d: %d %d\n", testn, res1, res2);
	}
	return 0;
}