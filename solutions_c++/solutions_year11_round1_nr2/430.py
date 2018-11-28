#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

typedef pair<bool, bool> bb;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<bb> vbb;
typedef vector<ii> vii;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;


bool has_letter(string word, char letter)
{
	for (int i = 0; i < word.size(); ++i) {
		if (word[i] == letter) return true;
	}
	return false;
}


bool is_consistent(string word, string pattern, string letters, int pos)
{
	if (word.size() != pattern.size()) return false;
	for (int i = 0; i < word.size(); ++i) {
		if (pattern[i] != '_' && pattern[i] != word[i]) return false;
		if (pattern[i] == '_') {
			for (int j = 0; j < pos; ++j) {
				if (letters[j] == word[i]) return false;
			}
		}
	}
	return true;
}


bool choose_letter(vs& dict, string pattern, string letters, int pos)
{
	char letter = letters[pos];
	for (vs::iterator it = dict.begin(); it != dict.end(); ++it) {
		if (has_letter(*it, letter) && is_consistent(*it, pattern, letters, pos)) return true;
	}
	return false;
}


string update_pattern(string pattern, string word, char letter)
{
	for (int i = 0; i < word.size(); ++i) {
		if (word[i] == letter) {
			pattern[i] = letter;
		}
	}
	return pattern;
}

int update_score(string pattern, char letter)
{
	return (has_letter(pattern, letter) ? 0 : 1);
}


int calc_score(vs& dict, char *letters, string word)
{
	string pattern;
	for (int i = 0; i < word.size(); ++i) {
		pattern = pattern + "_";
	}

	int score = 0;	
	for (int i = 0; i < 26; ++i) {
		char letter = letters[i];
		//cout << "letter: " << letter;		
		if (choose_letter(dict, pattern, letters, i)) {
			//cout << " (chosen)";
			pattern = update_pattern(pattern, word, letter);
			score += update_score(pattern, letter);
		}
		//cout << " score: " << score << endl;
	}
	
	return score;
}	



string solve(vs& dict, char *letters)
{
	//cout << "letters: " << letters << endl;
	int max_score = -1;
	string max_score_word;
	for (vs::iterator it = dict.begin(); it != dict.end(); ++it) {
		int new_score = calc_score(dict, letters, *it);
		//cout << "word: " << *it << " score: " << new_score << endl;
		if (new_score > max_score) {
			max_score = new_score;
			max_score_word = *it;
		}
	}
	return max_score_word;
}


int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N, M;
		cin >> N >> M;
		vs dict;
		for (int n = 0; n < N; ++n) {
			string word;
			cin >> word;
			dict.push_back(word);
		}
		char letters[27];
		letters[26] = '\0';
		cout << "Case #" << t << ":";
		for (int m = 0; m < M; ++m) {
			for (int i = 0; i < 26; ++i) {
				cin >> letters[i];
			}
			cout << ' ' << solve(dict, letters);
		}
		cout << endl;
	}
	
	return 0;
}
