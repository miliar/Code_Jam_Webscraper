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

void toAlf(const string & sequence, vector<string> * words) {
	map<char, char> dict;
	for (int i = 0; i < sequence.length(); ++i) {
		dict[sequence[i]] = 'a' + i;
	}
	for (int i = 0; i < words->size(); ++i) {
		for (int j = 0; j < words->at(i).length(); ++j) {
			words->at(i)[j] = dict[words->at(i)[j]];
		}
	}
}

string calculate (const string & sequence, const vector<string> & words_old) {
	vector<string> words = words_old;
	toAlf(sequence, &words);
	map<string, int> res;
	
	for (int i = 0; i < sequence.length(); ++i) {
		map<string, int> new_res;
		for (int j = 0; j < words.size(); ++j) {
			string prev = "";
			string curr = "";
			for (int l = 0; l < words[j].length(); ++l) {
				if (words[j][l] <= 'a' + i) {
					curr = curr + words[j][l];
				} else {
					curr = curr + '.';
				}
				if (words[j][l] < 'a' + i) {
					prev = prev + words[j][l];
				} else {
					prev = prev + '.';
				}
				
			}
			if (prev == curr) {
				new_res[curr] = max(res[curr], new_res[curr]);
			} else {
				new_res[prev] = max(res[prev] + 1, new_res[prev]);
				new_res[curr] = max(res[prev], new_res[curr]);
			}
		}
		res = new_res;
	}
	int argmax = 0;
	for (int i = 0; i < words.size(); ++i) {
		if (res[words[i]] > res[words[argmax]]) {
			argmax = i;
		}
	}
	return words_old[argmax];
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
		res = res + ' ' + calculate(sequences[i], words);
	}
	return res;
}

int main() {
	ifstream input("input.txt");
	ofstream output("output.txt");
	int testCount;
	input >> testCount;
	for (int test = 0; test < testCount; ++test) {
		output << "Case #" << test + 1 << ":" << solveB(input) << endl;
	}
	return 0;
}