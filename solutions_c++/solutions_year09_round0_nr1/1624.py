#include <iostream>
#include <vector>
using namespace std;

const int MAX = 512;

int count_match(string str, vector<string> vs) {
	bool hash[MAX][26];
	memset(hash, 0, sizeof(hash));
	bool inpare = false;
	int nth = 0;
	for (int i = 0; i < str.length(); ++i) {
		if (str[i] == '(') {
			inpare = true;
		} else if (str[i] == ')') {
			inpare = false;
			nth ++;
		} else {
			if (inpare) {
				hash[nth][str[i] - 'a'] = true;
			} else {
				hash[nth++][str[i] - 'a'] = true;
			}
		}
	}

	int ret = 0;
	for (int i = 0; i < vs.size(); ++i) {
		bool match = true;
		for (int j = 0; j < vs[i].length(); ++j) {
			if (!hash[j][vs[i][j] - 'a']) {
				match = false;
				break;
			}
		}
		if (match) {
			ret ++;
			//printf("%s\n", vs[i].c_str());
		}
	}
	return ret;
}

int main() {
	//freopen("alien_lang.in", "r", stdin);
	int L, D, N;
	char str[MAX];
	vector<string> db;
	scanf("%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; ++i) {
		scanf("%s", str);
		db.push_back(string(str));
	}
	for (int i = 0; i < N; ++i) {
		scanf("%s", str);
		printf("Case #%d: %d\n", i + 1, count_match(str, db));
	}
	return 0;
}

