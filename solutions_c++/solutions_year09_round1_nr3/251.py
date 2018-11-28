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

#define TASK "C"
#define PB(a) push_back(a)

using namespace std;

typedef long long int64;

const int MAXM = 1030, MAXB = 250;

int T, C, N;
vector <int> decks;
long double prob[MAXM][MAXB+5];
long double answer;
int fact[16];

void Generate(int mask, int left, int last) {
	if (left == 0) {
		decks.PB(mask);
		//cerr << mask << " ";
		return;
	}

	for (int k = last+1; k < C; k++) {
		if (C-k < left) break;

		if ((mask & (1 << k)) == 0) {
			Generate(mask | (1 << k), left-1, k);
		}
	}
}
     
int main() {
	#ifdef LOCAL
		freopen(TASK ".in", "rt", stdin);
		freopen(TASK ".out", "wt", stdout);
	#endif

	scanf("%d", &T);

	fact[0] = 1;
	for (int i = 1; i <= 12; i++) fact[i] = fact[i-1] * i;

	for (int cs = 1; cs <= T; cs++) {
		cerr << cs << endl;
		printf("Case #%d: ", cs);

		scanf("%d %d", &C, &N);

		if (C <= N) {
			printf("1.000000\n");
			continue;
		}

		decks.clear();
		memset(prob, 0, sizeof(prob));

		Generate(0, N, -1);

		prob[0][0] = 1.0;

		for (int m = 0; m < (1 << C)-1; m++) {
			for (int k = 0; k < MAXB; k++) {
				for (int i = 0; i < decks.size(); i++) {
					prob[m | decks[i]][k+1] += (prob[m][k] * fact[N] * fact[C-N]) / fact[C];
				}
			}
		}

		answer = 0;

		for (int k = 0; k <= MAXB; k++) {
			//cout << k << " " << prob[(1 << C) - 1][k] << endl;
			answer += prob[(1 << C) - 1][k] * k;
		}

		cout << answer << endl;
	}

	return 0;
}

