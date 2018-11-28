// Template for CodeJam by _ClearInbox_
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;
void HandleCases(ifstream &fin, ofstream &fout, int caseNum);

int main(int argc, char *argv[]) {
	ifstream fin(argv[1]);
	string out(argv[1]);
	out.replace(out.find(".in"), 3, ".out");
	ofstream fout(out.c_str()); // output
	string line;
	getline(fin, line);
	int cases = atoi(line.c_str());
	for (int i = 0; i < cases; i++) {
		HandleCases(fin, fout, i + 1);
	}
	fin.close();
	fout.close();
	return 0;
}

void HandleCases(ifstream &fin, ofstream &fout, int caseNum) {
	fout << "Case #" << caseNum << ": ";
	cout << "Case #" << caseNum << ": ";	// testing
	int o = 0;
	int ol = 1;
	int b = 0;
	int bl = 1;
	int butt;
	fin >> butt;
	for (int i = 0; i < butt; i++) {
		char color;
		int num;
		fin >> color >> num;
		if (color == 'O') {
			o += abs(num - ol) + 1;
			ol = num;
			if (o <= b) {
				o = b + 1;
			}
		}
		if (color == 'B') {
			b += abs(num - bl) + 1;
			bl = num;
			if (b <= o) {
				b = o + 1;
			}
		}
	}
	fout << max(b, o);
	fout << endl;
	cout << endl;	// testing
}
