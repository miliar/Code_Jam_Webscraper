#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isIn(char letter, vector<string> words) {
	bool found = false;
	for (int i = 0; i < words.size(); ++i) {
		if (words[i].find(letter) != string::npos) {
			return true;

		}
	}
	return found;
}

void removeBad(int pos, char letter, vector<string> &words) {
	for (int i = 0; i < words.size(); ++i) {

		if (words[i][pos] != letter) {
			words.erase(words.begin()+i);
			--i;
		} else {
			words[i][pos] = ' ';
		}
	}
}

void remove(char letter, vector<string> &words) {
	for (int i = 0; i < words.size(); ++i) {
		for (int x = 0; x < words[i].size(); ++x) {
			if (words[i][x] == letter) {
				words.erase(words.begin()+i);
				remove(letter, words);
				return;
			}
		}
	}
}


int getScore(string word, string alpha, vector<string> words) {
	int num = 0;
	int len = word.size();
	bool found = false;
	int numKnown = 0;
	for (int i = 0; i < words.size(); ++i) {
		if (words[i].size() != len) {
			words.erase(words.begin()+i);
			--i;
		}
	}
	for (int i = 0; i < 26; ++i) {
		if (!isIn(alpha[i], words))
			continue;
		for (int x = 0; x < word.size(); ++x) {
			if (word[x] == alpha[i]) {
				found = true;
				++numKnown;
				removeBad(x, alpha[i], words);
			}
		}
		remove(alpha[i], words);
		if (!found) {
			++num;

		}
		if (word.size() == numKnown || words.size() == 1)
			return num;
		found = false;
	}
	return num;
}

int main() {
	int cases = 0;
	cin >> cases;

	for (int i = 0; i < cases; ++i) {
		int numWords = 0, numAlphas = 0;
		vector<string> words, alphas;
		cin >> numWords >> numAlphas;
		for (int x = 0; x < numWords; ++x) {
			string a;
			cin >> a;
			words.push_back(a);
		}
		for (int x = 0; x < numAlphas; ++x) {
			string a;
			cin >> a;
			alphas.push_back(a);
		}

		cout << "Case #" << i+1 <<":";
		for (int x = 0; x < numAlphas; ++x) {
			string bestWord = "";
			int bestNum = -1;
			for (int y = 0; y < numWords; ++y) {
				int score = getScore(words[y], alphas[x], words);
				if (score > bestNum) {
					bestNum = score;
					bestWord = words[y];
				}
			}
			cout << " " << bestWord;
		}
		cout << endl;
	}
}