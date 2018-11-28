#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
using namespace std;

int main()
{
	vector<string> names;
	set<string> used;
	int N, S, Q, i, j, numSwitches;
	char line[256];
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin >> N;
	for (i = 0; i < N; ++i) {
		fin >> S;
		fin.ignore();
		names.clear();
		for (j = 0; j < S; ++j) {
			fin.getline(line, 256);
			names.push_back(string(line));
		}
		fin >> Q;
		fin.ignore();
		used.clear();
		numSwitches = 0;
		for (j = 0; j < Q; ++j) {
			fin.getline(line, 256);
			used.insert(string(line));
			if (used.size() == S) {
				++numSwitches;
				used.clear();
				used.insert(string(line));
			}
		}
		fout << "Case #" << i+1 << ": " << numSwitches;
		if (i != N-1)
			fout << endl;
	}
	return 0;
}