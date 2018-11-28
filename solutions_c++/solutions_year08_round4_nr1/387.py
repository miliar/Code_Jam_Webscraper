#include <iostream>
#include <string>
using namespace std;

const int INF = 10000000;

int N, M, V;
bool inter[12000];
bool change[12000];
int val[12000];
int tab[12000][2];

int rek(int n, int v) {
	if (tab[n][v] != -1) return tab[n][v];
	if (!inter[n]) {
		if (val[n] == v) return 0;
		return INF;
	}
	int num[2][2];
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			num[i][j] = rek(2*n+i, j);
		}
	}
	int num2[2];
	if (v == 0) {
		num2[0] = num[0][0] + num[1][0];
		if (num2[0] >= INF) num2[0] = INF;
		num2[1] = min(min(num[0][0] + num[1][0], num[0][0] + num[1][1]), num[0][1] + num[1][0]);
		if (num2[1] >= INF) num2[1] = INF;
	} else {
		num2[0] = min(min(num[0][0] + num[1][1], num[0][1] + num[1][0]), num[0][1] + num[1][1]);
		if (num2[0] >= INF) num2[0] = INF;
		num2[1] = num[0][1] + num[1][1];
		if (num2[1] >= INF) num2[1] = INF;
	}
	int res;
	if (change[n]) {
		res = min(num2[val[n]], num2[1-val[n]] + 1);
		if (res >= INF) res = INF;
	} else {
		res = num2[val[n]];
	}
	return tab[n][v] = res;
}

int main() {
	cin >> N;
	for (int tcs = 1; tcs <= N; tcs++) {
		cin >> M >> V;
		for (int i = 1; i <= (M-1)/2; i++) {
			inter[i] = true;
			cin >> val[i] >> change[i];
		}
		for (int i = (M-1)/2 + 1; i <= M; i++) {
			inter[i] = false;
			cin >> val[i];
		}
		memset(tab, -1, sizeof(tab));
		int res = rek(1, V);
		if (res == INF) {
			cout << "Case #" << tcs << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << tcs << ": " << res << endl;
		}
	}
	return 0;
}
