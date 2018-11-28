#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

char m[50][50];
int r, c;

int calc() {
	int res = 0;

	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			if (m[i][j] == '#') {
				if (j == c - 1 || i == r - 1)
					return 1;

				if (m[i+1][j] == '#' && m[i][j+1] == '#' && m[i+1][j+1] == '#') {
					m[i][j] = '/';
					m[i+1][j] = '\\';
					m[i][j+1] = '\\';
					m[i+1][j+1] = '/';
				} else {
					return 1;
				}
			}


		}
	}


	return res;
}

int main(int argc, char **argv) {
	string ifilename = "A-small.in";
	string ofilename = "A-small.out";
	ifstream ifs(ifilename.c_str());
	ofstream ofs(ofilename.c_str());

	int t;
	ifs >> t;


	for (int i = 0; i < t; ++i) {
		ifs >> r >> c;
		for (int j = 0; j < r; ++j) {
			for (int k = 0; k < c; ++k) {
				ifs >> m[j][k];
			}
		}
		ofs << "Case #" << (i+1) << ": " << endl;
		int res = calc();
		if (res > 0)
			ofs << "Impossible" << endl;
		else {
			for (int j = 0; j < r; ++j) {
				for (int k = 0; k < c; ++k) {
					ofs << m[j][k];
				}
				ofs << endl;
			}
		}

	}



	ifs.close();
	ofs.close();
	return 0;
}
