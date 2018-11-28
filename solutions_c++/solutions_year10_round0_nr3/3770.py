#include <iostream>
#include <string>
#include <queue>

using namespace std;

int main() {
	int R; //Number of times roller coaster will run in a day.
	int T; //Number of test cases.
	int k; //Number of people the roller coaster can hold.
	int N; //Number of groups.
	int revenue;
	string whitespace; //dummy variable to get rid of endline

	cin >> T;
	getline(cin, whitespace);
	for (int i = 0; i < T; i++) {
		revenue = 0;
		queue<int> waiting_line;
		cin >> R >> k >> N;
		getline(cin, whitespace);
		for (int j = 0; j < N; j++) {
			int group_size;
			cin >> group_size;
			waiting_line.push(group_size);
		}
		getline(cin, whitespace);
		for (int j = 0; j < R; j++) {
			int tempk = k;
			int tempN = N;
			while (((tempk - waiting_line.front()) >= 0) && (tempN > 0)) {
				revenue = revenue + waiting_line.front();
				tempk = tempk - waiting_line.front();
				int temp = waiting_line.front();
				waiting_line.push(temp);
				waiting_line.pop();
				tempN--;
			}
		}
		cout << "Case #" << i+1 << ": " << revenue << endl;
	}
	return 0;
}