#include <iostream>
#include <vector>
#include <string>

using namespace std;

int Hash[15][26];
vector<string> dict;
int L,D,N;

void Input() {
	dict.resize(D);
	for (int i = 0; i < D; ++i) {
		cin >> dict[i];
	}
}

void Solve(int ncase, const string &query) {
	memset(Hash, 0, sizeof(Hash));
	int pos = 0;
	for (int i = 0; i < L; ++i) {
		char cur = query[pos];
		if (cur == '(') {
			++pos;
			for (cur = query[pos]; cur != ')'; ++pos, cur = query[pos]) {
				Hash[i][cur - 'a'] = 1;
			}
		} else {
			Hash[i][cur - 'a'] = 1;
		}
		++pos;
	}
	int count = 0;
	for (int i = 0; i < dict.size(); ++i) {
		string &token = dict[i];
		bool match = true;
		for (int j = 0;j < token.size(); ++j) {
			if (Hash[j][char(token[j]) - 'a'] == 0) {
				match = false;
				break;
			}
		}
		if (match)
			++count;
	}
	printf("Case #%d: %d\n", ncase, count);
}

int main() {
	// freopen("A-large.in", "r", stdin);
	// freopen("A-large.out", "w", stdout);
	cin >> L >> D >> N;
	Input();	
	for (int ncase = 1; ncase <= N; ++ncase) {
		string query;
		cin >> query;
		Solve(ncase, query);
	}
	return 0;
}