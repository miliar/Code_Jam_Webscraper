#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cassert>

using namespace std;

void PickupWords(vector<string>* pOut, const vector<string>& dic, int pos, char c)
{
	for (size_t i = 0; i < dic.size(); ++i) {
		if (dic[i][pos] == c)
			pOut->push_back(dic[i]);
	}
}

int main(int argc, char* argv[])
{
	if (argc != 2)
		return 1;

	ifstream ifs(argv[1]);
	string dummy;

	int L, D, N;
	ifs >> L >> D >> N;
	getline(ifs, dummy);

	// dictionary
	vector<string> dic(D);
	for (int i = 0; i < D; ++i) {
		getline(ifs, dic[i]);
		assert(dic[i].length() == L);
	}

	vector<string> words, temp;
	for (int n = 0; n < N; ++n) {
		string word;
		getline(ifs, word);
		words = dic;

		int pos = 0;
		for (int i = 0; i < L; ++i, ++pos) {
			temp.clear();
			if (word[pos] == '(') {
				++pos;
				do {
					PickupWords(&temp, words, i, word[pos]);
				}
				while (word[++pos] != ')');
			}
			else {
				PickupWords(&temp, words, i, word[pos]);
			}
			words.swap(temp);
		}

		// output
		cout << "Case #" << n + 1 << ": " << words.size() << endl;
	}

	return 0;
}
