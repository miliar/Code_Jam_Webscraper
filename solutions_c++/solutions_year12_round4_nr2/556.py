#include <cstdio>
#include <algorithm>
using namespace std;

typedef pair<int,int> pint;

int W, L;
bool swapped;
pint A[1000];
int N;

pint ans[1000];

void solve(int X0, int Y0, int deltaX, int x) {
	if (x == N) return;

	int R = A[x].first;

	int X1 = X0, Y1 = Y0;
	if (Y0) X1 += R, Y1 += R;

	if (Y1 > L) {
		solve (X0 + deltaX, 0, 0, x);
	} else {
		ans[A[x].second] = make_pair(X1, Y1);
		solve (X0, Y0 + R*2, max(deltaX, R*2), x+1);
	}
}

void init() {
	scanf("%d%d%d", &N, &W, &L);
	for (int i = 0; i < N; i++) {
		int r; scanf("%d", &r);
		A[i] = make_pair(r, i);
	}

	sort(A, A+N);
	reverse(A, A+N);

	if (W < L) {
		swap(W, L);
		swapped = true;
	} else swapped = false;
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		init();

		solve(0, 0, 0, 0);
		printf("Case #%d:", i+1);

		for (int j = 0; j < N; j++)
			if (!swapped) printf(" %d %d", ans[j].first, ans[j].second);
			else printf(" %d %d", ans[j].second, ans[j].first);
		printf("\n");
	}

	return 0;
}
