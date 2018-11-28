#include <iostream>
#include <string>
#include <sstream>
#include <list>
#include <map>

using namespace std;

int main() {
	string line;
	int queries;
	int current = 1;

	getline(cin, line);
	queries = line[0] = '0';

	while (current < queries && getline(cin, line)) {
		istringstream reader(line);
		list<int> orange;
		list<int> blue;
		list<list<int>* > order;

		// read the locations of buttons to press
		int events;
		reader >> events;
		for (int i = 0; i < events; i++) {
			char which;
			int location;
			reader >> which >> location;
			if (which == 'O') {
				orange.push_back(location);
				order.push_back(&orange);
			} else if (which == 'B') {
				blue.push_back(location);
				order.push_back(&blue);
			}
		}

		// move and push the buttons
		int orangePos = 1;
		int bluePos = 1;
		int time = 0;
		while (!order.empty()) {
			time++;
			bool currentlyPushing = false;
			if (!orange.empty() && orangePos > orange.front()) {
				orangePos--;
			} else if (orangePos < orange.front()) {
				orangePos++;
			} else if (order.front() == &orange) {
				order.pop_front();
				orange.pop_front();
				currentlyPushing = true;
			}

			if (!blue.empty() && bluePos > blue.front()) {
				bluePos--;
			} else if (bluePos < blue.front()) {
				bluePos++;
			} else if (!currentlyPushing && order.front() == &blue) {
				order.pop_front();
				blue.pop_front();
				currentlyPushing = true;
			}
		}

		cout << "Case #" << current++ << ": " << time << endl;

	}
	return 0;
}
