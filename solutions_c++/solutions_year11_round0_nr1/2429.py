#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int NN = 128;

enum { ORANGE, BLUE };

int T, n;
int sb[NN], sr[NN];
int po, pb;
int ans;

int main(void) {
	scanf("%d", &T);
	for(int C = 1; C <= T; C++) {
		scanf("%d", &n);
		for(int i = 0; i < n; i++) {
			char ch[2];
			scanf("%s %d", ch, &sb[i]);
			sr[i] = ch[0] == 'O' ? ORANGE : BLUE;
		}

		ans = 0;
		po = pb = 1;
		for(int i = 0; i < n; i++) {
			int no = -1, nb = -1;
			for(int j = i; j < n && (no == -1 || nb == -1); j++) {
				if(sr[j] == ORANGE && no == -1) no = sb[j];
				if(sr[j] == BLUE && nb == -1) nb = sb[j];
			}

			if(sr[i] == ORANGE) {
				int delta = abs(sb[i] - po) + 1;
				ans += delta;
				po = sb[i];
				if(nb != -1) {
					int sgn = nb > pb ? 1 : -1;
					pb += sgn*min(delta, abs(nb - pb));
				}
			} else if(sr[i] == BLUE) {
				int delta = abs(sb[i] - pb) + 1;
				ans += delta;
				pb = sb[i];
				if(no != -1) {
					int sgn = no > po ? 1 : -1;
					po += sgn*min(delta, abs(no - po));
				}
			}
		}

		printf("Case #%d: %d\n", C, ans);
	}

	return 0;
}
