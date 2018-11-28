#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const int MAXN = 10010;
const int MAXM = 26;
const int MAXL = 11;

int n, m;
string word[MAXN];
map <vector <int>, int> maskMap[MAXL];
vector <int> maskLst[MAXN];
char buffer[65536];

string calc(string dict) {
	for (int i = 0; i < MAXL; i++) {
		maskMap[i].clear();
	}
	for (int i = 0; i < n; i++) {
		vector <int> v(26);
		for (int j = 0; j < (int)word[i].size(); j++) {
			int idx;
			for (idx = 0; idx < (int)dict.size(); idx++) {
				if (dict[idx] == word[i][j]) {
					break;
				}
			}
			v[idx] |= 1 << j;
		}
		maskMap[(int)word[i].size()][v] = i;
		maskLst[i] = v;
	}
	int mmax = -1, res = -1;
	for (int oo = 0; oo < n; oo++) {
		vector <int> & goal = maskLst[oo];
		vector <int> v(26);
		int cnt = 0;
		for (int o = 0; o < (int)dict.size(); o++) {
			if (o != 0) {
				v[o - 1] = goal[o - 1];
			}
			map <vector <int>, int>::iterator lowerIt;
			if (o != 0) {
				lowerIt = maskMap[(int)word[oo].size()].lower_bound(v);
			} else {
				lowerIt = maskMap[(int)word[oo].size()].begin();
			}
			map <vector <int>, int>::iterator upperIt;
			if (o != 0) {
				v[o - 1]++;
				upperIt = maskMap[(int)word[oo].size()].lower_bound(v);
				v[o - 1]--;
			} else {
				upperIt = maskMap[(int)word[oo].size()].end();
			}
			upperIt--;
			if (upperIt->first[o] && goal[o] == 0) {
				cnt++;
			}
//printf("%s (%s %s) cnt = %d (%d %d) %c\n", word[oo].c_str(), word[lowerIt->second].c_str(), word[upperIt->second].c_str(), cnt, upperIt->first[o], goal[o], dict[o]);
		}
		if (mmax < cnt) {
			mmax = cnt;
			res = oo;
		}
	}
	return word[res];
}

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", buffer);
			word[i] = buffer;
		}
		printf("Case #%d:", oo + 1);
		for (int i = 0; i < m; i++) {
			scanf("%s", buffer);
			printf(" %s", calc(buffer).c_str());
		}
		putchar('\n');
	}
}
