#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>

#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	scanf("%d", &T);
	forn(t, T) {
		int n;
		scanf("%d", &n);
		int where1 = 1, where2 = 1; 
		int time1 = 0, time2 = 0;

		forn(i, n) {
			char who;
			int pos;
			scanf(" %c %d", &who, &pos);

			if (who == 'O') {							
				time1 = max(time1 + abs(where1 - pos) + 1, time2 + 1);
				where1 = pos;
			} else if (who == 'B') {
				time2 = max(time2 + abs(where2 - pos) + 1, time1 + 1);
				where2 = pos;
			} else {
				fprintf(stderr, "BLYA!!!\n");
			}

		}
		printf("Case #%d: %d\n", t + 1, max(time1, time2));

	}

	return 0;
}
