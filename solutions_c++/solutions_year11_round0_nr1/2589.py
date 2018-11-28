#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>
using namespace std;

typedef vector < pair <int, int> > Buttons;

int solve(const Buttons* buttons[])
{
	Buttons::const_iterator front[2] =
		{buttons[0]->begin(), buttons[1]->begin()};
	Buttons::const_iterator end[2] =
		{buttons[0]->end(), buttons[1]->end()};
	int pos[2] = {1, 1};
	int n = buttons[0]->size() + buttons[1]->size();
	int res = 0;

	for (int cur_id = 0; cur_id < n; cur_id++) {
		int robot = (front[0] != end[0] && front[0]->first == cur_id) ? 0 : 1;
		int turns = abs(front[robot]->second - pos[robot]) + 1;
		pos[robot] = (front[robot]++)->second;
		res += turns;
		if (front[robot^1] != end[robot^1]) {
			int diff = front[robot^1]->second - pos[robot^1];
			if (abs(diff) > turns)
				diff = turns * ((diff > 0) ? 1 : -1);
			pos[robot^1] += diff;
		}
	}

	return res;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int N; cin >> N;
		Buttons blue, orange;
		for (int j = 0; j < N; j++) {
			char robot; cin >> robot;
			int button; cin >> button;
			switch (robot) {
			case 'O':
				orange.push_back(make_pair(j, button));
				break;
			case 'B':
				blue.push_back(make_pair(j, button));
				break;
			default:
				throw std::invalid_argument("Unknown robot id");
			}
		}

		const Buttons* arr[2] = {&blue, &orange};
		cout << "Case #" << i+1 << ": " << solve(arr) << endl;
	}
	return 0;
}
