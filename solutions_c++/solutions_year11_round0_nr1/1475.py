#include <fstream>
#include <vector>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

ifstream in("D:/JAM/A-small-attempt0.in");
ofstream out("D:/JAM/out.txt");

int solve_case(vector<int> &orange_actions, vector<int> &blue_actions) 
{
	int time = 0;
	int o = 1;
	int b = 1;
	int bi = 1;
	int oi = 1;


	while (true) {
		if (orange_actions.size() != 0 && blue_actions.size() != 0 && orange_actions[oi - 1] < blue_actions[bi - 1]) {
			int time_spent = abs(o - orange_actions[oi]) + 1;
			time += time_spent;
			o = orange_actions[oi];
			if (blue_actions[bi] - b >= 0) {
				b = min(blue_actions[bi], b + time_spent);
			} else {
				b = max(blue_actions[bi], b - time_spent);
			}

			oi = oi + 2;
		} else if (orange_actions.size() != 0 && blue_actions.size()) {
			int time_spent = abs(b - blue_actions[bi]) + 1;
			time += time_spent;
			b = blue_actions[bi];
			if (orange_actions[oi] - o >= 0) {
				o = min(orange_actions[oi], o + time_spent);
			} else {
				o = max(orange_actions[oi], o - time_spent);
			}

			bi = bi + 2;
		}

		if (bi > blue_actions.size()) {
			while (oi < orange_actions.size()) {
				time += abs(orange_actions[oi] - o) + 1;
				o = orange_actions[oi];
				oi += 2;
			}

			return time;
		} else if (oi > orange_actions.size()) {
			while (bi < blue_actions.size()) {
				time += abs(blue_actions[bi] - b) + 1;
				b = blue_actions[bi];
				bi += 2;
			}

			return time;
		}
	}
}

int main() 
{
	int n_cases;
	in >> n_cases;
	for (int i = 1; i <= n_cases; i++) {
		int n_buttons;
		in >> n_buttons;
		vector<int> orange_actions;
		vector<int> blue_actions;
		for (int j = 1; j <= n_buttons; j++) {
			char robot;
			in >> robot;
			int pos;
			in >> pos;
			if (robot == 'O') {
				orange_actions.push_back(j);
				orange_actions.push_back(pos);
			} else {
				blue_actions.push_back(j);
				blue_actions.push_back(pos);
			}
		}
		int n = solve_case(orange_actions, blue_actions);
		out << "Case #" << i << ": " << n << endl;
	}
}



