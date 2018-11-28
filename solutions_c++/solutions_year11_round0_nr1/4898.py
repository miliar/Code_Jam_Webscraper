#include <iostream>
#include <list>
#include <string>

using namespace std;

int solve(list<pair<int, int> > &sequence) {
	int loc[2];
	loc[0] = 1; loc[1] = 1;

	int next_time[2];
	next_time[0] = 0; next_time[1] = 0;

	while (sequence.size() > 0) {
		pair<int, int> next = sequence.front();
		sequence.pop_front();

		int time = max(abs(next.second - loc[next.first]) + next_time[next.first], next_time[1 - next.first]);

		next_time[next.first] = time + 1;
		loc[next.first] = next.second;

		//cout << (next.first == 0 ? "B" : "O") << " pushes button(" << next.second << ") at time " << next_time[next.first] << endl;
	}

	return max(next_time[0], next_time[1]);
}

int main() {
	int num_cases;
	cin >> num_cases;

	for (int i = 0; i < num_cases; i++) {

		int num_buttons;
		cin >> num_buttons;

		list<pair<int, int> > sequence;

		for (int j = 0; j < num_buttons; j++) {
			string a; cin >> a;
			int b; cin >> b;

			sequence.push_back(make_pair((a == "O" ? 1 : 0), b));
		}

		int time = solve(sequence);

		cout << "Case #" << (i +1) << ": " << time << endl;
	}

	return 0;
}