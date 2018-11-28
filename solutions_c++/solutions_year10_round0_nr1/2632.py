#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	for (int c=0; c<t; c++) {
		unsigned long int n,k;
		fin >> n >> k;
		unsigned long int exp = 1;
		for (int i =0; i<n; i++)
			exp*=2;

		fout << "Case #" << (c+1) << ": ";
		if (k%exp == exp-1)
			fout << "ON" << endl;
		else
			fout << "OFF" << endl;
	}

	fin.close(); fout.close();
	return 0;
}