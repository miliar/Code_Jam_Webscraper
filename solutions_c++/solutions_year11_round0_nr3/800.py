#include <iostream>
#include <array>
#include <vector>
#include <cassert>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

string solve(const vector<int> vals) {

	int rs=0,xs=0;
	for (int i=0;i < vals.size();++i) {

		rs +=vals[i];
		xs ^=vals[i];
	}

	if (xs != 0) return "NO";

	int m = *std::min_element(vals.begin(),vals.end());

	stringstream str;
	str << (rs-m);
	return str.str();
}

int main(int argc, char **argv) {
	int T;

	cin >> T;

	for(int i=0;i < T;++i) {
		int N;
		cin >> N;

		vector<int> vals;

		for (int j=0;j < N;++j) {
			int C;
			cin >> C;
			vals.push_back(C);
		}

		cout << "Case #" << (i+1) << ": " << solve(vals) << endl;
	}
	
    return 0;
}
