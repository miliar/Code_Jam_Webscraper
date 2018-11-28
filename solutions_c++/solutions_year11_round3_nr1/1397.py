#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <iomanip>
#include <algorithm>
#include <list>
#include <cmath>

using namespace std;

std::ostream& outCase(unsigned int tc) {
	std::cout << "Case #" << (tc + 1) << ": ";
	return std::cout;
}

bool testCase() {
	unsigned R; cin >> R;
	unsigned C; cin >> C;

	vector<string> img(R+1);

	for (unsigned i = 0; i < R; ++i) {
		cin >> img[i];
		img[i] += ".";
	}
	img[R] = "...........................................................";

	for (unsigned i = 0; i < R; ++i) {
		for (unsigned j = 0; j < C; ++j) {
			if (img[i][j] == '#') {
				img[i][j] = '/';

				if (img[i][j+1] == '#')
					img[i][j+1] = '\\';
				else
					return false;
				
				if (img[i+1][j] == '#')
					img[i+1][j] = '\\';
				else
					return false;

				if (img[i+1][j+1] == '#')
					img[i+1][j+1] = '/';
				else
					return false;
			}			
		}
	}

	for (unsigned i = 0; i < R; ++i) {
		for (unsigned j = 0; j < C; ++j) {
			cout << img[i][j];
		}
		cout << endl;
	}
}

int main() {
	unsigned int T; cin >> T;
	for (unsigned int t = 0; t < T; ++t) {		
		outCase(t) << endl;
		bool r = testCase();	
		if (!r)
			cout << "Impossible" << endl;
	}

	return 0;
}
