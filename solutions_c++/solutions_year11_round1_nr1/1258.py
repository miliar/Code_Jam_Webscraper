#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>

using namespace std;

/*string calculate (const string & sequence, const vector<string> & words) {
	vector<int> results(words.size());
	for (int i = 0; i < sequence.length(); ++i) {
		for (int word = 0; word < words.size(); ++word) {
			
		
		}
	}

}

string solveB(ifstream & input) {
	string res = "";
	int n, m;
	input >> n;
	input >> m;
	vector<string> words(n);
	vector<string> sequences(m);
	for (int i = 0; i < n; ++i) {
		input >> words[i];
	}
	for (int i = 0; i < m; ++i) {
		input >> sequences[i];
	}
	for (int i = 0; i < m; ++i) {
		res = res + ' ' + calculate(words, sequences[i]);
	}
	return res;
}*/

string solveA(ifstream & input) {
	int n, pd, pg;
	const string pos = "Possible";
	const string br = "Broken";
	input >> n;
	input >> pd;
	input >> pg;
	int d = -1, wd = -1;
	for(int i = 1; i <= min(100, n); ++i) {
		if ((i * pd) % 100 == 0) {
			d = i;
			wd = d * pd / 100;
			break;
		}
	}
	if (d == -1) {
		return br;
	}
	if (pg == 100 && wd < d || pg == 0 && wd > 0) {
		return br;
	}
	
	return pos;
}

int main() {
	ifstream input("input.txt");
	ofstream output("output.txt");
	int testCount;
	input >> testCount;
	for (int test = 0; test < testCount; ++test) {
		output << "Case #" << test + 1 << ": " << solveA(input) << endl;
		//cout << "Case #" << test + 1 << ": " << solveB(input) << endl;
	}
	return 0;
}