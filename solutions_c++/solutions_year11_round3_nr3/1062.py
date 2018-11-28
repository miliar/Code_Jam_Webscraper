// Template for CodeJam by _ClearInbox_
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <numeric>
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
int num, low, high;

bool Inham(int s, int note[]) {
	for (int i = 0; i < num; i++) {
		if (!(note[i] % s == 0 || s % note[i] == 0)) {
			return false;
		}
	}
	return true;
}

void HandleCases(ifstream &fin, ofstream &fout, int caseNum) {
	fout << "Case #" << caseNum << ": ";
	cout << "Case #" << caseNum << ": ";	// testing
	fin >> num >> low >> high;
	int notes[num];
	bool found = false;
	for (int i = 0; i < num; i++) {
		fin >> notes[i];
	}
	for (int i = low; i<= high; i++) {
		if (Inham(i, notes)) {
			fout << i;
			found = true;
			break;
		}
	}
	if (!found) {
		fout << "NO";
	}
	fout << endl;
	cout << endl;	// testing
}
