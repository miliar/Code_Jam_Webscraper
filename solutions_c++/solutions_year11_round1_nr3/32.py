#include <iostream>
#include <cstdio>
#include <vector>
#include <cassert>

using namespace std;

struct card {
	int c, s, t, id;
	card(int c, int s, int t, int id): c(c), s(s), t(t), id(id) {}
};

int main()
{
	int T;
	
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		int n;
		vector <card> cards, _have;

		scanf("%d", &n);

		int id = 0;
		for (int i = 0; i < n; i++) {
			int c, s, t;
			scanf("%d %d %d", &c, &s, &t);
			cards.push_back(card(c,s,t,id));
			_have.push_back(card(c,s,t,id));
			id++;
		}
		int m;
		scanf("%d",&m);
		for (int i = 0; i < m; i++) {
			int c, s, t;
			scanf("%d %d %d", &c, &s, &t);
			cards.push_back(card(c,s,t,id));
			id++;
		}

		int final = 0;

		for (int wc1 = 0; wc1 <= 81; wc1++) {
			vector <card> have = _have;
			int rc1 = wc1;
			int next = n;
			
			int score = 0, turn = 1;

			while (turn) {
//				printf("Turn = %d\n", turn);
				int done = 0;
				for (int i = 0; i < have.size(); i++)
					if (have[i].t > 0) {
						score += have[i].s;
						turn += have[i].t;

//						printf("Get card (%d,%d,%d)\n", have[i].c, have[i].s, have[i].t);

						if (have[i].c)
							if (next < cards.size()) {
								have.push_back(cards[next]);
								next ++;
							}
						have.erase(have.begin()+i);
						done = 1;
						goto bla;
					}
			bla:
				if (!done) {
					int havec1 = 0;
					for (int i = 0; i < have.size(); i++)
						if (have[i].c)
							havec1 = 1;
					if (havec1 && rc1 > 0) {
						int best = -1;
						for (int i = 0; i < have.size(); i++)
							if (have[i].c && (best == -1 || have[i].s > have[best].s))
								best = i;
						if (best != -1) {
							int i = best;
//						printf("Get card (%d,%d,%d)\n", have[i].c, have[i].s, have[i].t);
							score += have[i].s;
							turn += have[i].t;
							
							assert (have[i].c);
								if (next < cards.size()) {
									have.push_back(cards[next]);
									next ++;
								}
						have.erase(have.begin()+i);
							rc1--;
						}
					} else {
						int best = -1;
						for (int i = 0; i < have.size(); i++)
							if ((best == -1 || have[i].s > have[best].s))
								best = i;
						if (best != -1) {
							int i = best;
//						printf("Get card (%d,%d,%d)\n", have[i].c, have[i].s, have[i].t);
							score += have[i].s;
							turn += have[i].t;
							
							if (have[i].c)
								if (next < cards.size()) {
									have.push_back(cards[next]);
									next ++;
								}
						have.erase(have.begin()+i);
						}
					}
				}
				turn--;
			}

//			printf("Again: got score %d.\n", score);

			final = max(final, score);
		}

		printf("Case #%d: %d\n", t+1, final);
	}

	return 0;
}
