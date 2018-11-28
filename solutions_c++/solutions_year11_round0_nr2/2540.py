#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <cstring>
#include <vector>
using namespace std;

int C, D, N;
int countz[255];

char pos[255][255];

vector<char> neg[255];

int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		memset(countz, 0, sizeof(countz));
		memset(pos, 0, sizeof(pos));
		for (int i = 0; i < 255; ++i) {
			neg[i].clear();
		}
		cin >> C;
		for (int c = 0; c < C; ++c) {
			string p;
			cin >> p;
			pos[p[0]][p[1]] = p[2];
			pos[p[1]][p[0]] = p[2];
		}
		cin >> D;
		for (int d = 0; d < D; ++d) {
			string n;
			cin >> n;
			neg[n[0]].push_back(n[1]);
			neg[n[1]].push_back(n[0]);
		}
		cin >> N;

		string tmp;
		cin >> tmp;

		vector<char> word;
		for (int i = 0; i < tmp.size(); ++i) {

			bool done = false;

			// invoke
			word.push_back(tmp[i]);
			countz[tmp[i]]++;

			// combine
			while (word.size() >= 2) {
				char a = word[word.size() - 2];
				char b = word[word.size() - 1];
				char c = pos[a][b];
				if (c == 0) break;

				countz[a]--;
				countz[b]--;
				countz[c]++;
				
				word.pop_back();
				word.pop_back();
				word.push_back(c);

				done = true;
			}

			if (done) continue;

			char z = tmp[i];

			// oppose
			for (int j = 0; j < neg[z].size(); ++j) {
				char y = neg[z][j];
				if (countz[y] > 0) {

					while (word.size() > 0) {
						countz[word.back()]--;
						word.pop_back();
					}

					break;
				}
			}
		}
		
		cout << "Case #" << tt << ": ";

		cout << "[";

		for (int i = 0; i < word.size(); ++i) {
			if (i > 0) {
				cout << ", ";
			}
			cout << word[i];
		}

		cout << "]";

		cout << endl;
	}
	return 0;
}

