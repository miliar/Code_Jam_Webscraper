#define LOCAL

#include <cstdio>
#include <cmath>
#include <cstring>

#include <memory>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

#include <cassert>

#define TASK "A"

using namespace std;

typedef long long int64;

const int MAXL = 20, MAXD = 5200, MAXNN = MAXD * MAXL + 10;

int nn, L, D, N;
int root;
int answer;

int bor[MAXNN][32];
int chr[MAXNN], dep[MAXNN], par[MAXNN];
bool can[MAXNN];

set <int> poss[MAXL];

string word, s; 

int main() {
	#ifdef LOCAL
		freopen(TASK ".in", "rt", stdin);
		freopen(TASK ".out", "wt", stdout);
	#endif

	scanf("%d %d %d\n", &L, &D, &N);

	nn = 1;
	root = 1;
	chr[1] = 0;
	dep[1] = 0;
	par[1] = 0;

	for (int i = 1; i <= D; i++) {
		cin >> word;

		int v = root;
		for (int j = 0; j < word.length(); j++) {
			if (bor[v][word[j]-'a'+1] == 0) {
				nn++;
				chr[nn] = word[j]-'a'+1;
				dep[nn] = dep[v] + 1;
				par[nn] = v;
                bor[v][word[j]-'a'+1] = nn;
			}
			v = bor[v][word[j]-'a'+1];
		}
	}

	for (int cs = 1; cs <= N; cs++) {
		printf("Case #%d: ", cs);

		cin >> s;
		int j = 0;
		int len = s.length();

		for (int i = 1; i <= L; i++) {
			poss[i].clear();

			if (s[j] == '(') {
				j++;
				while (s[j] != ')') {
					poss[i].insert(s[j]-'a'+1);
					j++;
				}
				j++;
			}
			else {
				poss[i].insert(s[j]-'a'+1);
				j++;
			}
		}

		assert(j == len);

		answer = 0;
		memset(can, 0, sizeof(can));

		can[1] = true;
		for (int k = 2; k <= nn; k++) {
			if (can[par[k]] && poss[dep[k]].find(chr[k]) != poss[dep[k]].end()) {
				can[k] = true;
				if (dep[k] == L) {
					answer++;
				}
			}
		}

		printf("%d\n", answer);
	}

	return 0;
}

