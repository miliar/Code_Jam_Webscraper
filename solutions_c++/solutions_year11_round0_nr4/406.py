#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream fin("D-large.in");
	ofstream fout("D-large.out");
	int t;// test cases
	fin >> t;
	int n;
	int val[1000], pos[1000];
	for (int i = 0 ; i < t; i++) {
		fin >> n;
		for (int j = 0; j < n; j++) {
			fin >> val[j];
			val[j]--;
			pos[val[j]] = j;
		}
		int count = 0;
		for (int j = 0; j < n; j++) {
			if (val[j] != j) {
				int p = j;
				int circle = 1;
				while (val[p] != p) {
					int tmp = val[p];
					swap(val[p], val[pos[p]]);
					pos[tmp] = pos[p];
					pos[p] = p;
					p = pos[tmp];
					circle++;
				}
				count += circle;
			}
		}
		fout << "Case #" << i+1 << ": " <<count <<".000000" <<  endl;
	}
	fin.close();
	fout.close();
	return 0;
}

