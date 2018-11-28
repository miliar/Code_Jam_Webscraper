#include <ios>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <cassert>

using namespace std;

ostream& operator<<(ostream &os, vector<int>& v) {
	for (size_t i = 0; i < v.size(); ++i)
		 cerr << (v[i] ? '1' : '.');
	return os;
}

int main() {
	int L, D, N;

	std::ifstream is("data.txt");

	is >> L >> D >> N;

	vector<string> dict;
	for (int i = 0; i < D; ++i) {
		string word;
		is >> word;
		dict.push_back(word);
	}
	assert(dict.size() == D);

	vector<string> patterns;
	vector< vector<int> > maps;

	for (int i = 0; i < N; ++i) {
		string word;
		is >> word;
		patterns.push_back(word);

		cerr << word << endl;
		for (size_t j = 0; j < word.length();) {
			vector<int> local(26, 0);

			if (word[j] == '(') {
				++j;
				while (word[j] != ')') {
					local[word[j] - 'a'] = 1;
					++j;
				}
				++j;
			} else {
				local[word[j] - 'a'] = 1;
				++j;
			}
			cerr << local << endl;
			maps.push_back(local);
		}
	}
	assert(patterns.size() == N);

	vector<int> counters(N, 0);
	for (int i = 0; i < D; ++i) {
		for (int j = 0; j < N; ++j) {
			bool failed = false;
			for (int k = 0; k < L; ++k) {
				int x = j * L + k;
				if (maps[x][ dict[i][k] - 'a' ] == 0) {
					failed = true;
					break;
				}
			}
			if (!failed)
				counters[j] += 1;
		}
	}

	for (int j = 0; j < N; ++j) {
		cout << "Case #" << j + 1 << ": " << counters[j] << endl;
	}
	return 0;
}
