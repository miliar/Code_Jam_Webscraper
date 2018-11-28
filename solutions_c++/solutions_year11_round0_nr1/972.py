#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

std::ostream& outCase(unsigned int tc) {
	std::cout << "Case #" << (tc + 1) << ": ";
	return std::cout;
}

void assert(bool test) {
	if (!test) {
		int a = 0;
	}
}

void testCase() {
	unsigned int N; cin >> N;
	vector<pair<int, unsigned int> > oran;
	vector<pair<int, unsigned int> > blue;
	for (unsigned int i = 0; i < N; ++i) {
		string rob; cin >> rob;
		int but; cin >> but;
		if (rob[0] == 'O') {
			oran.push_back(make_pair(but, i));
		} else {
			blue.push_back(make_pair(but, i));
		}
	}

	unsigned int seq = 0;
	int oran_pos = 1;
	int blue_pos = 1;
	vector<pair<int, unsigned int> >::const_iterator oran_task = oran.begin();
	vector<pair<int, unsigned int> >::const_iterator blue_task = blue.begin();
	unsigned int seconds = 0;
	while (oran_task != oran.end() || blue_task != blue.end()) {
		++seconds;
		bool pressed = false;

		if (oran_task != oran.end()) {
			if (oran_task->first == oran_pos) {
				if (oran_task->second == seq) {
					pressed = true;
					++oran_task;
				} // else wait
			} else if (oran_task->first > oran_pos) {
				++oran_pos;
			} else {
				--oran_pos;
			}
		}

		if (blue_task != blue.end()) {
			if (blue_task->first == blue_pos) {
				if (blue_task->second == seq) {
					pressed = true;
					++blue_task;
				} // else wait
			} else if (blue_task->first > blue_pos) {
				++blue_pos;
			} else {
				--blue_pos;
			}
		}

		if (pressed) {
			++seq;
		}
	}

	cout << seconds << endl;
}

int main() {
	unsigned int T; cin >> T;
	for (unsigned int t = 0; t < T; ++t) {		
		outCase(t);
		testCase();		
	}

	return 0;
}