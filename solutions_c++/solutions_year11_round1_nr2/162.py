#include <cstdio>
#include <cstring>
#include <string>
#include <list>

using namespace std;

int T, n, m;
string s[10000];
int m1[10000][26], m2[10000];
int c[10000][26];
char buf[27];

string gao() {
	int ret = -1;
	string word;
	for (int i = 0; i < n; ++i) {
		list <int> li;
		int tot[26];
		memset(tot, 0, sizeof(tot));
		for (int j = 0; j < n; ++j) {
			if (s[i].length() == s[j].length()) {
				li.push_back(j);
				for (int k = 0; k < 26; ++k) {
					tot[k] += c[j][k];
				}
			}
		}
		int cur = 0;
		for (int j = 0; j < 26; ++j) {
			int ch = buf[j] - 'a';
			if (tot[ch] == 0) {
				continue;
			}
			if (m1[i][ch] == 0) {
				++cur;
			}
			for (list <int>::iterator k = li.begin(); k != li.end(); ) {
				if (m1[i][ch] != m1[*k][ch]) {
					for (int l = 0; l < 26; ++l) {
						tot[l] -= c[*k][l];
					}
					k = li.erase(k);
				} else {
					++k;
				}
			}
		}
		if (cur > ret) {
			ret = cur;
			word = s[i];
		}
	}
	return word;
}

int main() {
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		scanf("%d%d", &n, &m);
		memset(m1, 0, sizeof(m1));
		memset(m2, 0, sizeof(m2));
		memset(c, 0, sizeof(c));
		for (int i = 0; i < n; ++i) {
			scanf("%s", buf);
			s[i] = buf;
			for (int j = 0; j < (int)s[i].length(); ++j) {
				m1[i][buf[j] - 'a'] |= 1 << j;
				m2[i] |= 1 << (buf[j] - 'a');
				++c[i][buf[j] - 'a'];
			}
		}
		printf("Case #%d:", caseNum);
		for (int i = 0; i < m; ++i) {
			scanf("%s", buf);
			string res = gao();
			printf(" %s", res.c_str());
		}
		printf("\n");
	}
	return 0;
}
