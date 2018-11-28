#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <ctime>
#include <map>
#include <set>

using namespace std;

const int INF = 1000000000;

string f[50];
int d[50][50][50][50];
int R, C, F;

void read_data()
{
	cin >> R >> C >> F;
	for (int i = 0; i < R; ++i)
		cin >> f[i];
}

int fall(int row, int column) {
	int rf = row;
	while (rf < R-1 && f[rf+1][column] == '.') ++rf;

	if (rf-row+1 > F) return -1;
	return rf;
}

void calc(int row, int column, int left, int right) {
	int go_l = column;
	while (go_l > 0 && f[row+1][go_l-1] == '#' && (f[row][go_l-1] == '.' || (left <= go_l-1 && right >= go_l-1))) --go_l;

	int go_r = column;
	while (go_r < C-1 && f[row+1][go_r+1] == '#' && (f[row][go_r+1] == '.' || (left <= go_r+1 && right >= go_r+1))) ++go_r;

	// налево, не сжигаем
	if (go_l > 0 && (f[row][go_l-1] == '.' || (left <= go_l-1 && right >= go_l-1))) {
		int to_row = fall(row+1, go_l-1);
		if (to_row != -1)
			if (d[to_row][go_l-1][1][0] > d[row][column][left][right]) d[to_row][go_l-1][1][0] = d[row][column][left][right];
	}

	// направо, не сжигаем
	if (go_r < C-1 && (f[row][go_r+1] == '.' || (left <= go_r+1 && right >= go_r+1))) {
		int to_row = fall(row+1, go_r+1);
		if (to_row != -1)
			if (d[to_row][go_r+1][1][0] > d[row][column][left][right]) d[to_row][go_r+1][1][0] = d[row][column][left][right];
	}

	// сжигаем, падаем налево
	for (int burn_right = go_l; burn_right < go_r; ++burn_right) {
		int to_row = fall(row+1, burn_right);
		if (to_row == -1) continue;

		if (to_row > row+1) {
			if (d[to_row][burn_right][1][0] > d[row][column][left][right]+1) d[to_row][burn_right][1][0] = d[row][column][left][right]+1;
			continue;
		}

		for (int burn_left = go_l; burn_left <= burn_right; ++burn_left)
			if (d[to_row][burn_right][burn_left][burn_right] > d[row][column][left][right]+burn_right-burn_left+1) d[to_row][burn_right][burn_left][burn_right] = d[row][column][left][right]+burn_right-burn_left+1;
	}

	// сжигаем, падаем направо
	for (int burn_left = go_l+1; burn_left <= go_r; ++burn_left) {
		int to_row = fall(row+1, burn_left);
		if (to_row == -1) continue;

		if (to_row > row+1) {
			if (d[to_row][burn_left][1][0] > d[row][column][left][right]+1) d[to_row][burn_left][1][0] = d[row][column][left][right]+1;
			continue;
		}

		for (int burn_right = burn_left; burn_right <= go_r; ++burn_right)
			if (d[to_row][burn_left][burn_left][burn_right] > d[row][column][left][right]+burn_right-burn_left+1) d[to_row][burn_left][burn_left][burn_right] = d[row][column][left][right]+burn_right-burn_left+1;
	}
}

void solve()
{
	for (int i = 0; i < R; ++i)
		for (int j = 0; j < C; ++j)
			for (int left = 0; left < C; ++left)
				for (int right = 0; right < C; ++right)
					d[i][j][left][right] = INF;

	d[0][0][1][0] = 0;

	for (int i = 0; i < R-1; ++i)
		for (int j = 0; j < C; ++j) {
			if (d[i][j][1][0] != INF) calc(i, j, 1, 0);

			for (int left = 0; left < C; ++left)
				for (int right = left; right < C; ++right)
					if (d[i][j][left][right] != INF) calc(i, j, left, right);
		}

	int mn = INF;

	for (int j = 0; j < C; ++j)
		for (int left = 0; left < C; ++left)
			for (int right = 0; right < C; ++right)
				if (mn > d[R-1][j][left][right]) mn = d[R-1][j][left][right];

	if (mn != INF)
		printf("Yes %d\n", mn);
	else
		printf("No\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		read_data();
		solve();
	}

	return 0;
}
