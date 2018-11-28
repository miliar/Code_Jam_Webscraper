#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

void main () {
	ifstream f ("input.txt");
	ofstream of ("output.txt");
	int T = 0;
	f >> T;
	for (int i = 0; i < T; ++i) {
		long long N = 0, pg = 0, pd = 0;
		f >> N >> pd >> pg;

		bool res;
		if (pg == 100) {
			if (pd == 100) res = true;
			else res = false;
		}
		else if (pg == 0) {
			if (pd == 0) res = true;
			else res = false;
		} else {
			int j = 1;
			for (; j <= 1000; ++j) {
				if (pd * j % 100 == 0) break;
			}
			if (j <= N) res = true;
			else res = false;
		}
		
		if (res) {
			cout << "Case #" << i+1 << ": " << "Possible" << endl;
			of << "Case #" << i+1 << ": " << "Possible" << endl;
		} else {
			cout << "Case #" << i+1 << ": " << "Broken" << endl;
			of << "Case #" << i+1 << ": " << "Broken" << endl;
		}
	}
	f.close();
	of.close();
	cin.get();
}