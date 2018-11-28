#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;

int a[1000];

char spell[256];
map<pair<char, char>, char> combo;
set<pair<char, char> > oposed;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	scanf("%d", &T);
	forn(t, T) {
		combo.clear();
		oposed.clear();

		int c, d, n;
		scanf("%d", &c);
		forn(i, c) {
			char x1, x2, x3;
			scanf(" %c%c%c", &x1, &x2, &x3);
			combo[mp(x1, x2)] = x3;
			combo[mp(x2, x1)] = x3;
		}
		scanf("%d", &d);
		forn(i, d) {
			char x1, x2;
			scanf(" %c%c", &x1, &x2);
			oposed.insert(mp(x1, x2));
			oposed.insert(mp(x2, x1));
		}

		scanf("%d ", &n);
		int m = 0;
		forn(i, n) {
			scanf("%c", &spell[m]);
			m++;
			if (m >= 2 && combo.count(mp(spell[m - 2], spell[m - 1])) > 0) {
				spell[m - 2] = combo[mp(spell[m - 2], spell[m - 1])];
				m--;
			}

			forn(j, m) forn(k, m)
				if (j != k) {
					if (oposed.count(mp(spell[j], spell[k])) > 0) {
						m = 0;
					}
				}
		}
		spell[m] = 0;
		printf("Case #%d: [", t + 1);
		forn(i, m) {
			if (i != 0) printf(", ");
			printf("%c", spell[i]); 
		}
		printf("]\n");

	}
	return 0;
}

