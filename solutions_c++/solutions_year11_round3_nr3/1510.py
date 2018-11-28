#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main (int argc, char * const argv[]) {
	ifstream input(argv[1]);
	ofstream output("output.txt");
	int T, N, L, H;
	input >> T;
	for (int j = 0; j < T; j++) {
		input >> N >> L >> H;
		vector<int> harmonies;
		int a;
		for (int i = 0; i < N; i++) {
			input >> a;
			harmonies.push_back(a);
		}
		int big, small;
		vector<int> poss;
		for (int i = L; i <= H; i++) {
			bool done = false;
			for (int k = 0; k < harmonies.size(); k++) {
				if (i > harmonies[k]) {
					big = i, small = harmonies[k];
				} else {
					big = harmonies[k], small = i;
				}
				if (big%small!=0) {
					done = true;
					break;
				}
			}
			if (!done) {
				poss.push_back(i);
			}
		}
		output << "Case #" << j+1 << ": ";
		if (poss.empty()) {
			output << "NO" << endl;
		} else {
			output << poss[0] << endl;
		}
	}
	return 0;
}