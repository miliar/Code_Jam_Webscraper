
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <set>

using namespace std;

int toBaseAnd2(int dec, int base) {
	int res = 0;
	while (dec > 0) {
		res += (dec%base)*(dec%base);
		dec /= base;
	}
	return res;
}

int main() {

	int T;
	cin >> T;
	string line;
	vector<int> bases;
	set<int> seen; 
	getline(cin,line);
	for (int i = 0; i < T; i++) {
		getline(cin, line);
		istringstream in(line);
		int inn;
		bases.clear();
		while (in >> inn) bases.push_back(inn);
		bool was_there_bad_base = true;
		int j;
		for (j = 2; was_there_bad_base; j++) {
			was_there_bad_base = false;
			for (int k = 0; (k < bases.size()) && (!was_there_bad_base); k++) {
				seen.clear();
				int m = j;
				while (seen.count(m) == 0 && m!=1) {
					seen.insert(m);
					m = toBaseAnd2(m, bases[k]);
				}
				if (m!=1) {
					was_there_bad_base = true;
				}
			}
		}
		cout << "Case #" << (i+1) << ": " << j-1 << endl;
	}


	return 0;
}

