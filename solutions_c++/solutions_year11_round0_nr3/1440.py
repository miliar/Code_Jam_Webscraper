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
	string fname = "C:\\C-large.in";
	string outname = "C:\\C.out";
	ifstream in;
	ofstream out;
	in.open(fname);
	out.open(outname);

	int N;
	in >> N;
	for (int i=0; i < N; ++i) {
		int c;
		in >> c;
		
		vector<int> a(c);
		int res = 0;
		for (int j = 0; j < c; ++j) {
			in >> a[j];
			res ^= a[j];
		}
		if (res != 0)
			out << "Case #" << i + 1 << ": NO" << endl;
		else {
			sort(a.begin(), a.end());
			long long sum = 0;
			for (int h = 1; h < a.size(); ++h)
				sum += a[h];
			out << "Case #" << i + 1 << ": " << sum << endl;
		}
	}
	in.close();
	out.close();
	return 0;
}