#include <iostream>
#include <queue>
#include <cmath>
using namespace std;

queue< pair<char,int> > buttons;
queue<int> buttons_o;
queue<int> buttons_b;
int T, N;

int main() {
	int steps, position, distance_o, distance_b;
	char color;
	pair<char, int> next;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		steps = 0;
		cin >> N;
		for (int j = 0; j < N; j++)
		{
			cin >> color >> position;
			buttons.push(make_pair(color,position));
			if (color == 'O') buttons_o.push(position);
			else buttons_b.push(position);
		}
		distance_o = buttons_o.empty() ? 0 : buttons_o.front() - 1;
		distance_b = buttons_b.empty() ? 0 : buttons_b.front() - 1;
		while (!buttons.empty()) {
			next = buttons.front();
			if (next.first == 'O') {
				steps += distance_o+1;
				buttons_o.pop();
				distance_b = max(0, distance_b - (distance_o+1));
				if (!buttons_o.empty()) distance_o = abs(buttons_o.front() - next.second);
			}
			else {
				steps += distance_b+1;
				buttons_b.pop();
				distance_o = max(0, distance_o - (distance_b+1));
				if (!buttons_b.empty()) distance_b = abs(buttons_b.front() - next.second);
			}
			buttons.pop();
		}
		cout << "Case #" << i << ": " << steps << endl;
	}
	return 0;
}
