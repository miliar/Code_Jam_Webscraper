// Template for CodeJam by _ClearInbox_
#include <iostream>
#include <fstream>
#include <numeric>
#include <algorithm>
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

int Dummy(int num, int *x) {
	if (num == 1) {
		return x[0];
	} else if (num == 2) {
		return (x[0] ^ x[1]);
	} else {
		x[1] = x[0] ^ x[1];
		return Dummy(num - 1, x + 1);
	}
}

int DummyAdd(vector<int> &x) {
	int array[x.size()];
	for (int i = 0; i < x.size(); i++) {
		array[i] = x[i];
	}
	return Dummy(x.size(), array);
}

bool HasCombine(vector<int> &candy, int sum) {
	vector<int> sean = candy;
	vector<int> pat;
	if (find(sean.begin(), sean.end(), sum) != sean.end()) {
		// one candy
		return true;
	}
	return false;
}

int GetResult(vector<int> &candy) {
	int total = accumulate(candy.begin(), candy.end(), 0);
	if (DummyAdd(candy) != 0) {
		return -1;
	}
	for (int i = 0; i < total; i++) {
		if (HasCombine(candy, i)) {
			return total - i;
		}
	}
}

void HandleCases(ifstream &fin, ofstream &fout, int caseNum) {
	fout << "Case #" << caseNum << ": ";
	cout << "Case #" << caseNum << ": ";	// testing
	int num;
	fin >> num;
	vector<int> c;
	for (int i = 0; i < num; i++) {
		int temp;
		fin >> temp;
		c.push_back(temp);
	}
	sort(c.begin(), c.end());
	int result = GetResult(c);
	if (result == -1) {
		fout << "NO";
	} else {
		fout << result;
	}
	fout << endl;
	cout << endl;	// testing
}
