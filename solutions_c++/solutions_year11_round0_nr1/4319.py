#include <algorithm>
#include <iostream>
#include <vector>
#include <cassert>
#include <climits>
#include <cmath>

using namespace std;


void doit() {
	int N;
	cin >> N;

	int posO = 1;
	int posB = 1;
	int timeO = 0;
	int timeB = 0;

	for (int i = 0; i < N; i++) {
		char c;
		cin.ignore();
		cin >> c;
		if (c == 'O') {
			int button;
			cin >> button;

			int dist = abs(posO - button);

			posO = button;
			timeO = max(timeB, timeO + dist) + 1;
		} else if (c == 'B') {
			int button;
			cin >> button;

			int dist = abs(posB - button);

			posB = button;
			timeB = max(timeO, timeB + dist) + 1;
		} else {
			cout << "Error in input\n";
			exit(1);
		}
	}

	cout << max(timeO, timeB) << '\n';
}

int main() {
	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cout << "Case #" << i + 1 << ": ";
		doit();
	}

	return 0;
}
