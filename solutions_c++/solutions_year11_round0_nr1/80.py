#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>

using namespace std;

const int maxn = 10000;

int N;
char R[maxn];
int P[maxn];

void solve() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf(" %c %d", &R[i], &P[i]);
		R[i] = toupper(R[i]);
	}
	int idx1 = 0, idx2 = 0;
	for (; idx2 < N && R[idx2] == R[idx1]; idx2++);
	int p1 = 1, p2 = 1, ans = 0, waitTime = abs(P[0] - p1);
	while (idx1 < N) {
		if (idx2 >= N) {
			ans += waitTime;
			p1 = P[idx1];
			for (int i = idx1; i < N; i++) {
				ans += abs(P[i] - p1) + 1;
				p1 = P[i];
			}
			break;
		}
		int player2Need = abs(P[idx2] - p2);
		int player1Need = waitTime;
		p1 = P[idx1];
		for (int i = idx1; i < idx2; i++) {
			player1Need += abs(P[i] - p1) + 1;
			p1 = P[i];
		}
		ans += player1Need;
		if (player1Need >= player2Need) waitTime = 0;
		else waitTime = player2Need - player1Need;
		swap(p1, p2);
		idx1 = idx2;
		for (; idx2 < N && R[idx2] == R[idx1]; idx2++);
	}
	printf("%d\n", ans);
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}