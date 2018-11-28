#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

int MAP[512][512];

bool calc(int x, int y, int size) {

	int sum_x = 0, sum_y = 0;
	int w = 0;
	for (int j = y; j < y+size; ++j) {
		for (int i = x; i < x+size; ++i) {

			if (j == y && (i == x || i+1 == x+size)) continue;
			if (j+1 == y+size && (i == x || i+1 == x+size)) continue;

			sum_x += MAP[j][i] * (i+1);
			sum_y += MAP[j][i] * (j+1);

			w += MAP[j][i];
		}
	}

	if((2*(sum_x - w - x*w)-(size-1)*w==0) && (2*(sum_y - w - y*w)-(size-1)*w==0)) return 1;
	return 0;

}

int main() {

	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		int R, C, D;

		cin >> R >> C >> D;

		for (int r = 0; r < R; ++r) {
			char tmp[1024];
			cin >> tmp;
			for (int c = 0; c < C; ++c)
				MAP[r][c] = tmp[C-c-1] - '0';
		}

		int ans = -1;

		int start_size = min(R,C);


		for (int s = start_size; s >= 3; s-=1) {
			for (int y = 0; y+s <= R; ++y) {
				for (int x = 0; x+s <= C; ++x) {
					if (calc(x,y,s)) {
						ans = s;
						break;
					}
				}
				if (ans > 0) break;
			}
			if (ans > 0) break;
		}

		if (ans > 0)
			cout << "Case #" << t << ": " << ans << endl;
		else
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
	}

}


