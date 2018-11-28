#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>

using namespace std;

int getLength (int number) {
	int length = 0;
	while (number != 0) {
		number /= 10;
		length ++;
	}
	return length;
}

int rotate (int number, int length) {
	int powT = (int)pow((double)10, (double)(length - 1));
	int trail = number % powT;
	int start = number / powT;
	return trail * 10 + start;
}

int main () {
	ifstream fin;
	ofstream fout;
	vector<int> checked;
	int ok;

	fin.open("input.txt");
	fout.open("output.txt");

	int nCases, count, q;
	int A, B, length, n, m;
	fin >> nCases;
	
	for (int i = 1; i <= nCases; ++i) {
		fout << "Case #" << i << ": ";
		fin >> A >> B;
		count = 0;
		for (int n = A; n < B; ++n) {
			length = getLength(n);
			m = n;
			checked.clear();
			for (int k = 1; k < length; ++k) {
				m = rotate(m, length);
				if (length == getLength(m)) {
					if ( n < m && m <= B) {
						ok = 1;
						for (int j = 0; j < checked.size(); ++j) {
							if (checked.at(j) == m) {
								ok = 0;
								break;
							}
						}
						if (ok == 1) {
							checked.push_back(m);
							count ++;
						}
					} 
				}
			}
		}
		fout << count <<endl;
	}

	fin.close();
	fout.close();
	return 0;
}
