#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int n;
		cin >> n;
		int time_buf[2] = {0, 0};
		int pos[2] = {1, 1};
		int time = 0;
		while (n--) {
			char c;
			int bpos;
			cin >> c >> bpos;
			int color = (c == 'O');
			int add_time = max(1, abs(pos[color] - bpos) + 1 - time_buf[color]);
			time_buf[color] = 0;
			time_buf[1 - color] += add_time;
			pos[color] = bpos;
			time += add_time;
		}
		cout << "Case #" << t << ": " << time << endl;
	}
}
