#include <iostream>
#include <map>
#include <algorithm>
#include <fstream>
#include <cmath> 
#include <string>
#include <sstream>
#include <vector>

using namespace std;

vector<string> words;
vector<vector<string> > cases;


int main(int argc, char* argv[]) {
//	ifstream cin("C:\\test.txt");
	int L(0), D(0), N(0);
	cin >> L >> D >> N;

	for (int i = 0; i < D; ++i) {
		string word;
		cin >> word;
		words.push_back(word);
	}

	for (int i = 0; i < N; ++i) {
		vector<string> cs;

		string word;
		cin >> word;

		string cw;
		bool prt = false;

		for (int j = 0; j < word.size(); ++j) {
			if (word[j] == ')') {
				prt = false;
				if (cw != "") {
					cs.push_back(cw);
					cw = "";
				}
				continue;
			}
			if (word[j] == '(') {
				prt = true;
				continue;
			}

			if (prt) {
				cw += word[j];
			} else {
				cw = word[j];
				cs.push_back(cw);
				cw = "";
			}
		}
		if (cw != "") {
			cs.push_back(cw);
		}
		//cases.push_back(cs);
		int totals = 0;
		for (int x = 0; x < words.size(); ++x) {
			bool match = true;
			for (int j = 0; j < cs.size(); ++j) {
				bool flet = false;
				for (int k = 0; k < cs[j].size(); ++k) {
					if (words[x][j] == cs[j][k]) {
						flet = true;
						break;
					}
				}
				if (flet == false) {
					match = false;
					break;
				}
			}
			if (match == true) {
				++totals;
			}
		}
		cout << "Case #" << i + 1 << ": " << totals << "\n";
	}

	getchar();
	return 0;
}
