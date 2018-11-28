#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

struct Str {
	char arr[16];
	inline char &operator[] (int i) { return arr[i]; }

	inline bool operator == (const Str &oth) const {
		return strcmp(arr, oth.arr) == 0;
	}
	inline bool operator != (const Str &oth) const {
		return strcmp(arr, oth.arr) != 0;
	}
	inline bool operator < (const Str &oth) const {
		return strcmp(arr, oth.arr) < 0;
	}
};

const int SIZE = 10100;

int n, m;
Str words[SIZE];
char lst[128][32];

bool used[32];
Str pattern[SIZE];
vector<vector<int> > groups[32];
vector<int> score[32];

typedef map<Str, int> siMap;
siMap pind;

Str GetPattern(Str &s) {
	Str res;
	int i;
	for (i = 0; s[i]; i++) {
		if (used[s[i] - 'a'])
			res[i] = s[i];
		else
			res[i] = '*';
	}
	res[i] = 0;
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {

		scanf("%d%d", &n, &m);
		for (int i = 0; i<n; i++)
			scanf("%s", words[i].arr);
		for (int i = 0; i<m; i++)
			scanf("%s", lst[i]);

		printf("Case #%d:", tt);
		for (int i = 0; i<m; i++) {
			memset(used, 0, sizeof(used));

			groups[0].clear();
			pind.clear();
			for (int j = 0; j<n; j++)
				pind[GetPattern(words[j])] = 0;
			int k = 0;
			for (siMap::iterator it = pind.begin(); it != pind.end(); it++) it->second = k++;
			groups[0].clear();
			groups[0].resize(k);
			score[0].clear();
			score[0].resize(k, 0);
			for (int j = 0; j<n; j++)
				groups[0][pind[GetPattern(words[j])]].push_back(j);

			const char CHARS = 26;
			for (int c = 0; c < CHARS; c++) {
				int cc = lst[i][c] - 'a';

/*				printf("Before %c\n", cc + 'a');
				for (int g = 0; g<groups[c].size(); g++) {
					printf("Group %d (%d)\n", g, score[c][g]);
					for (int q = 0; q<groups[c][g].size(); q++)
						printf("%s %s\n", GetPattern(words[groups[c][g][q]]).arr, words[groups[c][g][q]].arr);
				}
				printf("\n");*/

				groups[c+1].clear();
				score[c+1].clear();
				for (int g = 0; g<groups[c].size(); g++) {
					vector<int> &vg = groups[c][g];
					pind.clear();
					used[cc] = true;

					for (int u = 0; u<vg.size(); u++)
						pind[GetPattern(words[vg[u]])] = 0;
					int k = groups[c+1].size();
					for (siMap::iterator it = pind.begin(); it != pind.end(); it++) it->second = k++;
					groups[c+1].resize(k);
					score[c+1].resize(k);
					for (int u = 0; u<vg.size(); u++) {
						used[cc] = false;
						Str oldp = GetPattern(words[vg[u]]);
						used[cc] = true;
						Str newp = GetPattern(words[vg[u]]);

						int tsc = score[c][g];
						if (oldp == newp && pind.size() > 1)
							tsc++;

						int ii = pind[newp];
						groups[c+1][ii].push_back(vg[u]);
						score[c+1][ii] = tsc;
					}
				}
				groups[c].clear();
			}

			int minsc = -1000000000;
			for (int t = 0; t<score[CHARS].size(); t++)
				if (minsc < score[CHARS][t])
					minsc = score[CHARS][t];

			int ans = 1000000000;
			for (int t = 0; t<score[CHARS].size(); t++)
				if (score[CHARS][t] == minsc) {
					for (int q = 0; q<groups[CHARS][t].size(); q++) {
						int ii = groups[CHARS][t][q];
						if (ans > ii) ans = ii;
					}
				}

			printf(" %s", words[ans].arr);
		}
		printf("\n");
		fflush(stdout);
	}
	return 0;
}
