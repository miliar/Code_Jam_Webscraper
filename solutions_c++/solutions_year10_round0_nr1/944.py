#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("out.txt");
	int t, n, k;
	fin >> t;
	for (int i = 1; i <= t; ++i) {
		fin >> n >> k;
		fout << "Case #" << i << ": ";
		if ((k + 1) % (1 << n) == 0) fout << "ON" << endl;
		else fout << "OFF" << endl;
	}
	return 0;
}
