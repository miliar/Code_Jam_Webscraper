#include <iostream>
#include <deque>
#include <map>
using namespace std;

struct element {
	char R;
	int P;
};

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		deque<element> queue;
		map<char, deque<element> > qs;
		for (int i = 0; i < N; i++) {
			element el;
			cin >> el.R;
			cin >> el.P;
			queue.push_back(el);
			qs[el.R].push_back(el);
		}

		map<char, int> positions;
		positions['O'] = 1;
		positions['B'] = 1;
		int time = 0;
		while (!queue.empty()) {
			element curMove = queue.front();
			char curRobot = curMove.R;
			char secondRobot = (curMove.R == 'O') ? 'B' : 'O';

			//first robot moves
			if (curMove.P == positions[curRobot]) {
				queue.pop_front();
				qs[curRobot].pop_front();
			} else {
				if (curMove.P > positions[curRobot]) {
					positions[curRobot]++;
				} else {
					positions[curRobot]--;
				}
			}

			//second robot moves
			element nextMove = qs[secondRobot].front();
			if (nextMove.P > positions[secondRobot]) {
				positions[secondRobot]++;
			} else if (nextMove.P < positions[secondRobot]) {
				positions[secondRobot]--;
			} else {
				//waiting...
			}

			time++;
			/*cout << "Time: " << time << endl;
			cout << "O: " << positions['O'] << endl;
			cout << "B: " << positions['B'] << endl;
			cout << endl;*/
		}
		cout << "Case #" << t << ": " << time << endl;


	}
	return 0;
}
