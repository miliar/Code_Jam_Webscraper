#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <algorithm>
#include <string>
#include <exception>
using namespace std;

int abs(int n)
{
	return (n < 0) ? -n : n;
}

int main(int argc, char** argv) {
	try {
		ifstream ifs;
		ifs.exceptions(ifstream::failbit | ifstream::badbit);
		ifs.open(argv[1]);

		size_t n;
		ifs >> n;
		cerr << "N=" << n << endl;

		for (size_t i = 0; i < n; ++i) {
			size_t m;
			ifs >> m;
			vector<char> robots;
			vector<int> buttons, O, B, tO, tB;
			for (size_t j = 0; j < m; ++j) {
				char robot;
				unsigned int button;
				ifs >> robot;
				ifs >> button;
				robots.push_back(robot);
				buttons.push_back(button);
				if (robot == 'B') B.push_back(button);
				else O.push_back(button);
			}
			tO.resize(O.size() + 1);
			tB.resize(B.size() + 1);

			int lO = 1, lB = 1;
			int curO = 1, curB = 1;
			tB[0] = 0;
			tO[0] = 0;
			for (size_t j = 0; j < buttons.size(); ++j) {
				if (robots[j] == 'B') {
					tB[curB] = tB[curB-1] + abs(buttons[j] - lB) + 1;
					lB = buttons[j];
					if ((curO != 1) && (tB[curB] <= tO[curO-1])) tB[curB] = tO[curO-1] + 1;
					++curB;
				}
				else {
					tO[curO] = tO[curO-1] + abs(buttons[j] - lO) + 1;
					lO = buttons[j];
					if ((curB != 1) && (tO[curO] <= tB[curB-1])) tO[curO] = tB[curB-1] + 1;
					++curO;
				}
			}
			int time;
			if (tO[tO.size()-1] > tB[tB.size()-1]) time = tO[tO.size()-1];
			else time = tB[tB.size()-1];
			cout << "Case #" << i + 1 << ": " << time << endl;
		}

	} catch (exception& ex) {
		cerr << "Exception: " << ex.what() << endl;
	}
}
