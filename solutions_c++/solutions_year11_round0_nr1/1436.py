#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main() {
	ifstream in("A.in");
	ofstream out("A.out");

	int tests;
	in >> tests;
	for (int test = 1; test <= tests; ++test) {
		out << "Case #" << test << ": ";

		int pos[2]  = {1, 1};
		int time[2] = {0, 0};

		int presses;
		in >> presses;
		while (presses--) {
			char bot;
			int  loc;

			in >> bot >> loc;
			int turn = bot == 'O' ? 0 : 1;

			time[turn] = max(time[1 - turn], time[turn] + abs(loc - pos[turn])) + 1;
			pos[turn]  = loc;
		}

		out << max(time[0], time[1]) << endl;
	}
}