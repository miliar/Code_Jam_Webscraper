#include<iostream>
#include<vector>
#include<string>

#define ORANGE 0
#define BLUE 1

using namespace std;

int pos[2];
int turn;
int seconds;
vector<int> buttons[2]; // place of button each robot has to press
int currButton[2]; // current button which a robot has to look for
vector<int> order; // order of robots fot taking turns

int main() {
	int T;
	cin >> T;
	for (int i = 0; T--; i++) {
		order.clear();
		buttons[0].clear(), buttons[1].clear();
		currButton[0] = 0, currButton[1] = 0;
		pos[0] = 1, pos[1] = 1;
		seconds = 0;
		int N;
		cin >> N;
		while (N--) {
			char r;
			int b;
			cin >> r >> b;
			if (r == 'O') {
				buttons[ORANGE].push_back(b);
				order.push_back(ORANGE);
			} else {
				buttons[BLUE].push_back(b);
				order.push_back(BLUE);
			}
		}
		for (int j = 0; j < order.size(); j++) {
			turn = order[j];
			int delta = abs(buttons[turn][currButton[turn]] - pos[turn]) + 1;
			seconds += delta;
			pos[turn] = buttons[turn][currButton[turn]++];
			// looks how much other robot can advance
			int nextTurn = (turn + 1) % 2;
			if (buttons[nextTurn][currButton[nextTurn]] > pos[nextTurn]) 	
				pos[nextTurn] += min(delta, abs(buttons[nextTurn][currButton[nextTurn]] - pos[nextTurn]));
			else if (buttons[nextTurn][currButton[nextTurn]] < pos[nextTurn])
				pos[nextTurn] -= min(delta, abs(buttons[nextTurn][currButton[nextTurn]] - pos[nextTurn]));			
		}
		cout << "Case #" << (i + 1) << ": " << seconds << endl;
	}
	return 0;
}