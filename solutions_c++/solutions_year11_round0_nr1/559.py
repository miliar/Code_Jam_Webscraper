#include <fstream>
#include <string>

using namespace std;

#define FILENAME	"A-large-0"

int main() {
	ifstream in(FILENAME ".in");
	ofstream out(FILENAME ".out");

	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {
		int N;
		in >> N;
		int o_pos = 1, b_pos = 1, o_time = 0, b_time = 0, button;
		string robot;

		for (int i = 0; i < N; ++i) {
			in >> robot >> button;
			if (robot == "O") {
				o_time = max(b_time + 1, o_time + 1 + abs(button - o_pos));
				o_pos = button;
			} else {
				b_time = max(o_time + 1, b_time + 1 + abs(button - b_pos));
				b_pos = button;
			}
		}
		out << "Case #" << test << ": " << max(o_time, b_time) << endl;
	}

	return 0;
}