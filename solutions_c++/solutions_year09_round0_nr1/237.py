#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

void parsequery(string query, bool character_map[][26], int L) {
	int n = 0;
	int i = 0;
	while (n < L) {
		memset(character_map[n], 0, sizeof(character_map[n]));

		char x = query[i];
		while ((x < 'a' || x > 'z') && x != '(') {
			x = query[++i];
		}
		if (x == '(') {
			do {
				x = query[++i];
				if (x >= 'a' && x <= 'z')
					character_map[n][x-'a'] = true;
			} while (x != ')');
			++i;
		}
		else {
			character_map[n][x-'a'] = true;
			++i;
		}
		++n;
	}
}

int main() {
	bool character_map[26][26];
	char buf[2000];

	gets(buf);
	int L, D, N;
	sscanf(buf, "%d %d  %d", &L, &D, &N);

	vector<string> dic;
	int i,j,k;
	for (i = 0; i < D; ++i) {
		gets(buf);
		dic.push_back(buf);
	}

	for (i = 0; i < N; ++i) {
		gets(buf);
		bool cand[5001];
		memset(cand,1,sizeof(cand));

		parsequery(buf, character_map, L);

		/*
		for (j = 0; j < L; ++j) {
			for (k = 0; k < 26; ++k) {
				cout << (int)character_map[j][k];
			}
			cout << endl;
		} */

		for (j = 0; j < L; ++j) {
			for (k = 0; k < D; ++k) {
				if (!character_map[j][dic[k][j] - 'a']) {
					cand[k] = false;
				}
			}
		}

		int res = 0;
		for (j = 0; j < D; ++j) {
			if (cand[j]) {
				++res;
			}
		}

		cout << "Case #" << i + 1 << ": " << res << endl;
	}
}