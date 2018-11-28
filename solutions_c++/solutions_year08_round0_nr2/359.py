#include <stdio.h>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

#define CA 0
#define CB 1
#define SA 2
#define SB 3

vector<pair<int, int> > S;
int ta, tb;

int main() {
	int N;
	scanf("%d", &N);
	for (int _42 = 0; _42 < N; _42++) {
		printf("Case #%d: ", _42+1);
		S.clear();
		int T, na, nb;
		ta = tb = 0;
		int ra = 0, rb = 0;
		scanf("%d %d %d", &T, &na, &nb);
		for (int i = 0; i < na; i++) {
			int ha, ma, hb, mb;
			scanf(" %d:%d %d:%d", &ha, &ma, &hb, &mb);
			int tempa = ha*60 + ma;
			int tempb = hb*60 + mb;
			S.push_back(make_pair(tempa, SA));
			S.push_back(make_pair(tempb+T, CB));
		}
		for (int i = 0; i < nb; i++) {
			int ha, ma, hb, mb;
			scanf(" %d:%d %d:%d", &ha, &ma, &hb, &mb);
			int tempa = ha*60 + ma;
			int tempb = hb*60 + mb;
			S.push_back(make_pair(tempa, SB));
			S.push_back(make_pair(tempb+T, CA));
		}
		sort(S.begin(), S.end());
		for (int i = 0; i < S.size(); i++) {
			switch (S[i].second) {
				case CA: 
					ta++;
					break;
				case CB:
					tb++;
					break;
				case SA:
					if (ta == 0) {
						ra++;
						ta++;
					}
					ta--;
					break;
				case SB:
					if (tb == 0) {
						rb++;
						tb++;
					}
					tb--;
					break;
			}
		}
		printf("%d %d\n", ra, rb);
	}

	return 0;
}
