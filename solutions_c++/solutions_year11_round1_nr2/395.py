#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

string blanks(int n) {
	string ret = "";
	for (int i = 0; i < n; ++i)
		ret += "*";
	return ret;
}

string convert_non(const string& s, char c) {
	string ret = "";
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == c)
			ret = ret + "1";
		else
			ret = ret + "0";
	}
	return ret;
}

bool contains(const string& s, char c) {
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == c)
			return true;
	}
	return false;
}

int main() {
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		int n, m; cin >> n >> m;
		string words[n];
		for (int i = 0; i < n; ++i) {
			cin >> words[i];
		}
		vector<string> ret;
		for (int zzz = 0; zzz < m; ++zzz) {
			string list; cin >> list;
			assert(list.length() == 26);
			int best = -1;
			string ans = "???";
			for (int i = 0; i < n; ++i) {
				string cand = words[i];
				set<char> cand_chars;
				for (int j = 0; j < cand.length(); ++j)
					cand_chars.insert(cand[j]);
				set<string> possib_words;
				set<char> possib_chars;
				for (int j = 0; j < n; ++j) {
					if (cand.length() == words[j].length()) {
						possib_words.insert(words[j]);
						for (int x = 0; x < words[j].length(); ++x) {
							possib_chars.insert(words[j][x]);
						}
					}
				}
				assert(possib_words.find(cand) != possib_words.end());
				int score = 0;
				for (int ci = 0; ci < 26 && possib_words.size() > 1; ++ci) {
					char c = list[ci];
					set<string> new_possib_words;
					if (possib_chars.find(c) == possib_chars.end())
						continue;
					if (cand_chars.find(c) == cand_chars.end()) {
						++score;
						// only add things that don't have that letter
						for (set<string>::iterator it = possib_words.begin(); it != possib_words.end(); ++it) {
							if (!contains(*it, c)) {
								new_possib_words.insert(*it);	
							}
						}
					} else {
						// only add things that have that letter in the same spots
						string base = convert_non(cand, c);
						for (set<string>::iterator it = possib_words.begin(); it != possib_words.end(); ++it) {
							string curr = convert_non(*it, c);
							if (base == curr) {
								new_possib_words.insert(*it);
							}
						}
					}
					// update new possib chars
					possib_words = new_possib_words;
					possib_chars.clear();
					for (set<string>::iterator it = new_possib_words.begin(); it != new_possib_words.end(); ++it) {
						string s = *it;
						for (int xx = 0; xx < s.length(); ++xx)
							possib_chars.insert(s[xx]);
					}
				}
				assert(possib_words.size() == 1);
				if (best < score) {
					best = score;
					ans = cand;
				}
			}
			ret.push_back(ans);
		}
		cout << "Case #" << test << ": ";
		for (int i = 0; i + 1 < ret.size(); ++i) {
			cout << ret[i] << " ";
		}
		cout << ret.back() << endl;
	}
}

