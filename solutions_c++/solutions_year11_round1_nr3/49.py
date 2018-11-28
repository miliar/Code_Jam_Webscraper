#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define PROBLEM "C"

struct Card {
	int c, s, t;
	Card(int C, int S, int T) : c(C), s(S), t(T) {}
};

vector <Card> cards;
bool used[100];
int n, m, w;
int q;

int rec(int turns) {
	if (turns == 0) return 0;
	turns--;

	int ans = 0;

	for (int i = 0; i < q; i++) {
		if (!used[i] && cards[i].t > 0) {
			used[i] = true;

			q = min(w, q + cards[i].c);
			ans += cards[i].s;
			turns += cards[i].t - 1;
		}
	}

	int bestCi = -1;
	int bestSi = -1;
	
	for (int i = 0; i < q; i++) {
		if (!used[i]) {
			assert(cards[i].t == 0);
			if (bestCi == -1 || cards[i].c > cards[bestCi].c || cards[i].c == cards[bestCi].c && cards[i].s > cards[bestCi].s) {
				bestCi = i;
			}
			if (bestSi == -1 || cards[i].s > cards[bestSi].s || cards[i].s == cards[bestSi].s && cards[i].c > cards[bestSi].c) {
				bestSi = i;
			}
		}
	}

	bool oldused[100];
	int oldq;
	int finalans = ans;

	//best cards      	
	if (bestCi != -1) {
    	memcpy(oldused, used, sizeof(used));
    	oldq = q;
    	
    	used[bestCi] = true;
    	q = min(w, q + cards[bestCi].c);

    	int bestCans = cards[bestCi].s + rec(turns);
    	finalans = max(finalans, ans + bestCans);

    	memcpy(used, oldused, sizeof(used));
    	q = oldq;
    }

	//best score
	if (bestSi != -1 && bestSi != bestCi) {
    	memcpy(oldused, used, sizeof(used));
    	oldq = q;
    	
    	used[bestSi] = true;
    	q = min(w, q + cards[bestSi].c);

    	int bestSans = cards[bestSi].s + rec(turns);
    	finalans = max(finalans, ans + bestSans);

    	/*memcpy(used, oldused, sizeof(used));
    	q = oldq;*/
    }

	return finalans;
}

int main() {
	freopen(PROBLEM ".in", "rt", stdin);
	freopen(PROBLEM ".out", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		fprintf(stderr, "Case #%d: ", t);

		memset(used, 0, sizeof(used));
		cards.clear();

		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			int c, s, t;
			scanf("%d %d %d", &c, &s, &t);
			cards.PB(Card(c, s, t));
		}
		scanf("%d", &m);
		for (int i = 0; i < m; i++) {
			int c, s, t;
			scanf("%d %d %d", &c, &s, &t);
			cards.PB(Card(c, s, t));
		}

		w = m + n;
		q = n;

		printf("%d", rec(1));

		printf("\n");
	}

	return 0;
}
