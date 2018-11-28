#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <algorithm>
#include <string>
#include <exception>
using namespace std;

int main(int argc, char** argv) {
	try {
		ifstream ifs;
		ifs.exceptions(ifstream::failbit | ifstream::badbit);
		ifs.open(argv[1]);

		size_t T;
		ifs >> T;
		cerr << "T=" << T << endl;

		for (size_t t = 0; t < T; ++t) {
			size_t R, C;

			ifs >> R >> C;

			bool impossible = false;
			vector<vector<int> > pict;

			size_t sum = 0;

			pict.resize(R);
			for (size_t r = 0; r < R; ++r) {
				sum = 0;
				pict[r].resize(C);
				for (size_t c = 0; c < C; ++c) {
					char ch;
					ifs >> ch;
					pict[r][c] = (ch == '#') ? -1 : 0;

					if (pict[r][c])
						++sum;
				}
				if ((sum & 1) != 0) {
					impossible = true;
				}
			}
			for (size_t c = 0; c < C; ++c) {
				sum = 0;
				for (size_t r = 0; r < R; ++r) {
					if (pict[r][c])
						++sum;

				}
				if ((sum & 1) != 0) {
					impossible = true;
					break;
				}
			}
			cout << "Case #" << (t+1) << ": " << endl;
			if (impossible) {
				cout << "Impossible" << endl;
			} else {
				for (size_t r = 0; r < R; ++r) {
					for (size_t c = 0; c < C; ++c) {
						if (pict[r][c]) {
							pict[r][c] = 0;
							if (r > 0) {
								if ((pict[r - 1][c] & 2) == 0)
									pict[r][c] |= 2;
							}
							else
								pict[r][c] |= 2;
							if (c > 0) {
								if ((pict[r][c - 1] & 1) == 0)
									pict[r][c] |= 1;
							}
							else
								pict[r][c] |= 1;
							switch (pict[r][c]) {
							case 3:
							case 0:
								cout << '/';
								break;
							case 1:
							case 2:
								cout << '\\';
								break;
							}
						} else {
							cout << '.';
						}
					}
					cout << endl;
				}
			}
		}

	} catch (exception& ex) {
		cerr << "Exception: " << ex.what() << endl;
	}
}
