#include <cstdio>
#include <vector>
using namespace std;

int turnaround, na, nb;
int n[2];
int need[2];
int have[2];
int ready[2][30 * 60];
vector<pair<int, int> > trains[2];

void read(int x) {
	trains[x].resize(n[x]);
	for (int i = 0; i < n[x]; i++) {
		int h1, m1, h2, m2;
		scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
		trains[x][i] = make_pair(h1 * 60 + m1, h2 * 60 + m2);
	}
}

void process(int m, int x) {
	have[x] += ready[x][m];
	for (int i = 0; i < trains[x].size(); i++)
		if (trains[x][i].first == m) {
			if (have[x] == 0) {
				have[x] = 1;
				need[x]++;
			}
			have[x]--;
			ready[x ^ 1][trains[x][i].second + turnaround]++;
		}
}

void solve() {
	memset(need, 0, sizeof(need));
	memset(have, 0, sizeof(have));
	memset(ready, 0, sizeof(ready));

	scanf("%d%d%d", &turnaround, &n[0], &n[1]);
	read(0); //A
	read(1); //B

	for (int m = 0; m < 24 * 60; m++) {
		process(m, 0);
		process(m, 1);
	}
}

int main () {
	freopen("b.in", "r", stdin); freopen("b.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++) {
		solve();
		printf("Case #%d: %d %d\n", T, need[0], need[1]);
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
