#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cassert>
#include <utility>
#include <climits>

using namespace std;

#define EPS 1E-8
#define INF int(1E+9)

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

void solve(int tst) {

	int n, v;    
	scanf("%d%d", &n, &v);

	vector<int> ops(n + 1);
	vector<int> can_change(n + 1);
	for (int i = 1; i <= (n - 1) / 2; ++i)
		scanf("%d%d", &ops[i], &can_change[i]);
	
	vector<int> value(n + 1);
	for (int i = (n - 1) / 2 + 1; i <= n; ++i) 
		scanf("%d", &value[i]);

	vector<int> t[2];
	t[0] = vector<int>(n + 1, INF);
	t[1] = vector<int>(n + 1, INF);

	for (int i = (n - 1) / 2 + 1; i <= n; ++i) 
		t[value[i]][i] = 0;
	
	for (int i = (n - 1) / 2; i >= 1; --i) {
		if (ops[i] == 1) {		//AND
			forn (x, 2)
				forn (y, 2) {
					int val = x & y;
					int cost = t[x][2 * i] + t[y][2 * i + 1];
					t[val][i] = min(t[val][i], cost);

					if (can_change[i]) {
						val = x | y;
						cost = t[x][2 * i] + t[y][2 * i + 1] + 1;
						t[val][i] = min(t[val][i], cost);
					}
				}
		} else {
			forn (x, 2)
				forn (y, 2) {
					int val = x | y;
					int cost = t[x][2 * i] + t[y][2 * i + 1];
					t[val][i] = min(t[val][i], cost);

					if (can_change[i]) {
						val = x & y;
						cost = t[x][2 * i] + t[y][2 * i + 1] + 1;
						t[val][i] = min(t[val][i], cost);
					}
				}
		}
	}

    printf("Case #%d: ", tst);    

	int ans = t[v][1];
	if (ans < INF / 2)
		printf("%d", ans);
	else
		printf("IMPOSSIBLE");

    printf("\n");
}

int main() {

    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tst;
    scanf("%d", &tst);
    forn (i, tst) solve(i + 1);

    return 0;
}

