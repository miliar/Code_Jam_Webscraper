#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

vector<char> vec;
int cas, comN, oppN, n;
char s[256], com[256][256], opp[256][256];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &cas);
	for (int c = 1; c <= cas; ++c) {
		for (int i = 0; i < 256; ++i)
			for (int j = 0; j < 256; ++j)
				com[i][j] = opp[i][j] = '?';
		vec.clear();
		scanf("%d", &comN);
		for (int i = 0; i < comN; ++i) {
			scanf("%s", s);
			com[s[0]][s[1]] = com[s[1]][s[0]] = s[2];
		}
		scanf("%d", &oppN);
		for (int i = 0; i < oppN; ++i) {
			scanf("%s", s);
			opp[s[0]][s[1]] = opp[s[1]][s[0]] = '!';
		}
		scanf("%d%s", &n, s);
		for (int i = 0; i < n; ++i) {
			// check for combine
			if (vec.size() > 0 && com[vec.back()][s[i]] != '?') {
				char res = com[vec.back()][s[i]];
				vec.pop_back();
				vec.push_back(res);
				goto OVER;
			}
			// check for oppsite
			for (int j = 0; j < vec.size(); ++j) {
				if (opp[vec[j]][s[i]] == '!') {
					vec.clear();
					goto OVER;
				}
			}
			vec.push_back(s[i]);
OVER:;
		}
		printf("Case #%d: [", c);
		for (int i = 0; i < vec.size(); ++i) {
			if (i) printf(", ");
			printf("%c", vec[i]);
		}
		printf("]\n");
	}
	return 0;
}