// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int max(int a, int b) {
	return a >= b ? a : b;
}
int abs(int a) {
	return a >= 0 ? a : -a;
}

int main () {
	int n, m;
	ifstream fin ("in1.txt");
	ofstream fout ("out1.txt");
	fin >> m;
	for(int j = 0; j < m; j++) {
		fin >> n;
		char tc;
		int ti;
		int btime = 0, bloc = 1;
		int otime = 0, oloc = 1;
		for(int i = 0; i < n; i++) {
			fin >> tc >> ti;
			if(tc == 'B') {
				btime += abs(bloc - ti);
				bloc = ti;
				btime = max(btime+1, otime+1);
			} else {
				otime += abs(oloc - ti);
				oloc = ti;
				otime = max(btime+1, otime+1);
			}
		}
		fout << "Case #" << j+1 << ": " << max(otime, btime) << "\n";
	}
  return 0;
}
