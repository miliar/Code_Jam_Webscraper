#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	long t, n, k;
	ofstream fout("D:\\out");
	ifstream fin("D:\\in");
	fin >> t;
	for (int i = 0; i < t; ++i) {
		fin >> n >> k;
		if ((k + 1) % (1 << n) == 0) {
			fout << "Case #" << i + 1 << ": ON" << endl;
		} else {
			fout << "Case #" << i + 1 << ": OFF" << endl;
		}
	}

	return 0;
}

