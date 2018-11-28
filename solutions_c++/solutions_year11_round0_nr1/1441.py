#include <string>
#include <vector>
#include <iterator>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <algorithm>
#include <fstream>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;


int main() {
	string fname = "C:\\A-large.in";
	string outname = "C:\\A.out";
	ifstream in;
	ofstream out;
	in.open(fname);
	out.open(outname);

	int N;
	in >> N;
	for (int i=0; i < N; ++i) {
		int k;
		vector<pair<bool, int>> o;
		in >> k;
		for (int j = 0; j < k; ++j) {
			char col; int pos;
			in >> col >> pos;
			o.push_back(make_pair(col == 'O' ? false : true, pos));
		}

		vector<int> pos(2,1);
		int res = 0;
		int hasTime = 0;
		bool lastR = false;
		for (int i = 0; i < o.size(); ++i) {
			int index = o[i].first;
			int extraTime = 0;
			if (index != lastR || i == 0) {
				extraTime = hasTime;
				hasTime = 0;
			}
			int timeLast = max(1, abs(pos[index] - o[i].second) + 1 - extraTime);
			hasTime += timeLast;
			res += timeLast;
			pos[index] = o[i].second;
			lastR = index;
		}
		out << "Case #" << i + 1 << ": " << res << endl;
	}
	in.close();
	out.close();
	return 0;
}