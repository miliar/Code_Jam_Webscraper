#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cassert>
#include <algorithm>
#include <map>

using namespace std;


int main(int argc, char* argv[])
{
	if (argc != 2)
		return 1;

	ifstream ifs(argv[1]);
	string dummy;

	int T;
	ifs >> T;
	getline(ifs, dummy);

	for (int t = 0; t < T; ++t) {
		int H, W;
		ifs >> H >> W;
		getline(ifs, dummy);

		// create altitude map, idmap
		vector<int> altmap, idmap;
		altmap.reserve(H * W);
		idmap.reserve(H * W);
		for (int i = 0; i < (H * W); ++i) {
			int alt;
			ifs >> alt;
			altmap.push_back(alt);
			idmap.push_back(i);
		}
		getline(ifs, dummy);

		// connect
		for (int h = 0; h < H; ++h) {
			for (int w = 0; w < W; ++w) {
				const int curPos = h * W + w;
				int lowestPos = -1;
				int lowestAlt = altmap[curPos];

				// north
				if ((h - 1) >= 0) {
					int pos = (h - 1) * W + w;
					if (altmap[pos] < lowestAlt) {
						lowestPos = pos;
						lowestAlt = altmap[pos];
					}
				}

				// west
				if ((w - 1) >= 0) {
					int pos = h * W + (w - 1);
					if (altmap[pos] < lowestAlt) {
						lowestPos = pos;
						lowestAlt = altmap[pos];
					}
				}

				// east
				if ((w + 1) < W) {
					int pos = h * W + (w + 1);
					if (altmap[pos] < lowestAlt) {
						lowestPos = pos;
						lowestAlt = altmap[pos];
					}
				}

				// south
				if ((h + 1) < H) {
					int pos = (h + 1) * W + w;
					if (altmap[pos] < lowestAlt) {
						lowestPos = pos;
						lowestAlt = altmap[pos];
					}
				}

				// update idmap
				if (lowestPos >= 0) {
					const int from = idmap[lowestPos];
					const int to = idmap[curPos];
					std::replace(idmap.begin(), idmap.end(), from, to);
				}
			}
		}

		// id -> char
		map<int, char> id2char;
		char c = 'a';
		for (size_t i = 0; i < idmap.size(); ++i) {
			if (id2char.find(idmap[i]) == id2char.end()) {
				id2char.insert(make_pair(idmap[i], c++));
			}
		}

		// output
		cout << "Case #" << t + 1 << ":\n";
		for (size_t i = 0; i < idmap.size(); ++i) {
			cout << id2char[idmap[i]];
			if ((i + 1) % W)
				cout << ' ';
			else
				cout << endl;
		}
	}

	return 0;
}
