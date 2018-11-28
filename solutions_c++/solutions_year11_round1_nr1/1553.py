#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

bool f(int n, int pd, int pg) {
	if (pg == 0 || pg == 100)
		return pd == pg;
	int No = 100;
	for (int i = 2; i <= pd; i++) {
		if (pd % i == 0 && No % i == 0) {
			pd /= i;
			No /= i;
			i = 1;
		}
	}
	return No <= n;
}

int main() {
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.txt");
	int t, n, pd, pg;
	fin >> t;
	for (int x = 1; x <= t; x++) {
		fin >> n >> pd >> pg;
		fout << "Case #" << x << ": " << (f(n, pd, pg)? "Possible": "Broken") << endl;
	}
}
