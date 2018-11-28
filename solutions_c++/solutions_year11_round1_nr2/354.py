#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <cmath>

using namespace std;

struct Word {
	void set(string w)
	{
		word = w;

		for (size_t i=0; i<26; i++) hashes[i] = 0;
		sz = word.length();

		for (size_t i=0; i<sz; i++) {
			int letter = word[i]-'a';
			hashes[letter] |= (1 << i);
		}
	}

	size_t sz;
	int hashes[26];
	string word;
};

string solve(vector<Word>& dict, string list)
{
	for (size_t i=0; i<list.size(); i++) {
		char letter = list[i];
	}
	return dict[0].word;
}

int getScore(int baseScore, vector<Word*> dict, Word& picked, string alpha)
{
	if (dict.size() == 1) return baseScore;

	for (size_t i=0; i<alpha.length(); i++) {
		int letter = alpha[i]-'a';

		bool ok = false;
		for (size_t j=0; j<dict.size(); j++) {
			if (dict[j]->hashes[letter]) {
				ok = true;
				break;
			}
		}

		if (ok) {
			alpha = alpha.substr(i+1);
			vector<Word*> dict2;
			for (size_t j=0; j<dict.size(); j++) {
				if (dict[j]->hashes[letter] == picked.hashes[letter]) {
					dict2.push_back(dict[j]);
				}
			}
			if (picked.hashes[letter]) {
				return getScore(baseScore, dict2, picked, alpha);
			} else {
				return getScore(baseScore + 1, dict2, picked, alpha);
			}
		}
	}

	std::cout << "WTF!!";
	return -1;
}

string solveBrute(vector<Word>& dict, string alpha)
{
	string bestWord;
	int bestScore = -1;

	for (size_t i=0; i<dict.size(); i++) {
		Word& word = dict[i];
		string w = word.word;
		vector<Word*> remaining;
		for (size_t j=0; j<dict.size(); j++) {
			if (dict[j].sz == word.sz) remaining.push_back(&dict[j]);
		}
		int score = getScore(0, remaining, word, alpha);

		if (score > bestScore) {
			bestScore = score;
			bestWord = w;
		}
	}

	//std::cout << "Best score: " << bestScore << endl;
	return bestWord;
}

void processCase(istream& in, ostream& out)
{
	int N, M;
	in >> N;
	in >> M;

	vector<Word> dict;
	char buffer[128];
	for (int i=0; i<N; i++) {
		in >> buffer;
		dict.push_back(Word());
		dict.back().set(buffer);
	}

	vector<string> lists;
	for (int i=0; i<M; i++) {
		in >> buffer;
		lists.push_back(buffer);
	}

	for (int i=0; i<M; i++) {
		if (i != 0) out << " ";
		out << solveBrute(dict, lists[i]).c_str();
	}
}

int main()
{
	ifstream in("B-small-attempt1.in");
	//ostream& out = cout;
	ofstream out("B-small-attempt1.out", std::ios_base::out);

	int nCases;
	in >> nCases;
	for (int i=0; i<nCases; i++) {
		out << "Case #" << (i+1) << ": ";
		processCase(in, out);
		out << endl;
	}

	out.flush();
}
