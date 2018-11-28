#include <cstdlib>
#include <iostream>
#include <fstream>
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
	
	//output << cx << " " << cy << " " << endl;
	//output << (double)sum_x/w << " " << (double)sum_y/w << endl;

	//return fabs(cx) <= 0.5 && fabs(cy) <= 0.5;
	//return fabs(cx) <= 0.0000001 && fabs(cy) <= 0.0000001;
	return false;
	
}

int main() {

	fstream input,output;
	input.open("1.txt",ios::in);
	output.open("2.txt",ios::out);
	int T;
	input >> T;

	for (int t = 1; t <= T; ++t) {
		int R, C, D;

		input >> R >> C >> D;

		for (int r = 0; r < R; ++r) {
			char tmp[1024];
			input >> tmp;
			for (int c = 0; c < C; ++c)
				MAP[r][c] = tmp[C-c-1] - '0';
		}

		int ans = -1;

		int start_size = min(R,C);

		//if (start_size % 2 == 0) start_size -= 1;

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
			output << "Case #" << t << ": " << ans << endl;
		else
			output << "Case #" << t << ": IMPOSSIBLE" << endl;
	}

}


