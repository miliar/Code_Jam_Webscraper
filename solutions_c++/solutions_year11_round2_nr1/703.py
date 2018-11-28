#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int n;
char map[100][110];
int game[100][2];
double wp[100][3];

void process() {
	scanf("%d", &n);
	memset(game, 0, sizeof(game));
	for (int i = 0; i < n; ++i) {
		scanf("%s", map[i]);
		for (int j = 0; j < n; ++j) {
			if (map[i][j] != '.') game[i][0]++;
			if (map[i][j] == '1') game[i][1]++;
		}
		wp[i][0] = game[i][1] / (double) game[i][0];
	}
	for (int i = 0; i < n; ++i) {
		wp[i][1] = 0;
		for (int j = 0; j < n; ++j) {
			if (map[j][i] == '0') {
				wp[i][1] += game[j][1] / (double) (game[j][0] - 1);
			} else if (map[j][i] == '1') {
				wp[i][1] += (game[j][1] - 1) / (double) (game[j][0] - 1);
			}
		}
		wp[i][1] /= (double)game[i][0];
	}
	for (int i = 0; i < n; ++i) {
		wp[i][2] = 0;
		for (int j = 0; j < n; ++j) {
			if (map[i][j] != '.') {
				wp[i][2] += wp[j][1];
			}
		}
		wp[i][2] /= (double)game[i][0];
	}
	for (int i = 0; i < n; ++i) {
		printf("%.12lf\n", wp[i][0] / 4 + wp[i][1] / 2 + wp[i][2] / 4);
	}
}

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int t = 1; t <= cas; ++t) {
		printf("Case #%d:\n", t);
		process();
	}
	return 0;
}
