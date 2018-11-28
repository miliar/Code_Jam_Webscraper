#include <iostream>

using namespace std;


int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		int at[2], tim[2];
		at[0] = 1;
		at[1] = 1;
		tim[0] = 0;
		tim[1] = 0;

		for (int i = 0; i < N; i++) {
			char ch;
			int b;
			cin >> ch >> b;
			int robot = (ch == 'O') ? 0 : 1;
			int dist = at[robot] - b;
			if (dist < 0) dist = -dist;

			int other = 1 - robot;
			if (tim[robot] >= tim[other] || tim[robot] + dist + 1 > tim[other]) {
				tim[robot] += dist + 1;
			} else {
				tim[robot] = tim[other] + 1;
			}
			at[robot] = b;
		}
		int ret = (tim[0] > tim[1]) ? tim[0] : tim[1];
		cout << "Case #" << t << ": " << ret << endl;
	}

	return 0;
}

