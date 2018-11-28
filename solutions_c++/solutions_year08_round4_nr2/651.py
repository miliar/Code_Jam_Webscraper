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

struct res {
	int x, y;
	int val;
};

void solve(int tst) {

	int n, m, a;
	scanf("%d%d%d", &n, &m, &a);	

	vector<res> t;
	forn (i, n + 1)
		forn (j, m + 1) {
			res r;
			r.x = i;
			r.y = j;
			r.val = i * j;
			t.pb(r);
		}

	forn (i, t.size())
		forn (j, t.size())
			if (t[i].val - t[j].val == a) {
			    printf("Case #%d: %d %d %d %d %d %d\n", tst, 0, 0, t[i].x, t[j].y, t[j].x, t[i].y);    
				return;
			}
    printf("Case #%d: ", tst);    
    printf("IMPOSSIBLE\n");
}

int main() {

    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tst;
    scanf("%d", &tst);
    forn (i, tst) solve(i + 1);

    return 0;
}

