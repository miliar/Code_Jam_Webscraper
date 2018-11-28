#include <iostream>
#include <vector>

using namespace std;

typedef vector<bool> vb;
typedef vector<char> vc;
typedef vector<int> vi;

char combine[26][26];	// only {Q,W,E,R,A,S,D,F} are used
bool opposed[26][26];	// ditto

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		for (int i = 0; i < 26; ++i) {
			for (int j = 0; j < 26; j++) {
				combine[i][j] = 0;
				opposed[i][j] = false;
			}
		}
		int C;
		cin >> C;
		for (int c = 0; c < C; ++c) {
			char c1, c2, c3;
			cin >> c1 >> c2 >> c3;
			combine[c1-'A'][c2-'A'] = c3;
		}
		int D;
		cin >> D;
		for (int d = 0; d < D; ++d) {
			char d1, d2;
			cin >> d1 >> d2;
			opposed[d1-'A'][d2-'A'] = true;
		}
		int N;
		cin >> N;
		vc element_list;
		vi count(26, 0);
		for (int n = 0; n < N; n++) {
			char element1;
			cin >> element1;
			element_list.push_back(element1);
			char element2;
			// combine?
			if (element_list.size() >= 2) {
				element2 = element_list[element_list.size()-2];
				char element3 = combine[element1-'A'][element2-'A'] | combine[element2-'A'][element1-'A'];
				if (element3) {
					element_list.pop_back();
					element_list.pop_back();
					element_list.push_back(element3);
				}
			}
			// opposed?
			element1 = element_list.back();	// list can't be empty at this point
			for (int m = 0; m < (int) element_list.size()-1; ++m) {
				element2 = element_list[m];
				if (opposed[element1-'A'][element2-'A'] || opposed[element2-'A'][element1-'A']) {
					element_list.clear();
					break;
				}
			}
		}
		cout << "Case #" << t << ": [";
		for (unsigned i = 0; i < element_list.size(); ++i) {
			if (i > 0) {
				cout << ", ";
			}
			cout << element_list[i];
		}
		cout << "]" << endl;
	}
	return 0;
}
