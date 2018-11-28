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

void print(int i) {
	cout << i << " ";
}

void HandleCases(ifstream &fin, ofstream &fout, int caseNum) {
	fout << "Case #" << caseNum << ": ";
	cout << "Case #" << caseNum << ": ";	// testing
	int num;
	fin >> num;
	int array[num];
	vector<int> sorted;
	for (int i = 0; i < num; i++) {
		fin >> array[i];
		sorted.push_back(array[i]);
	}
	sort(sorted.begin(), sorted.end());
	// for_each(sorted.begin(), sorted.end(), print);
	int misplace = 0;
	for (int i = 0; i < num; i++) {
		if (array[i] != sorted[i]) {
			misplace++;
		}
	}
	fout << misplace << ".000000";
	fout << endl;
	cout << endl;	// testing
}
