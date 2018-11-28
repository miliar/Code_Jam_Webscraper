#include <vector>
#include <list>

#include <deque>
#include <queue>
#include <stack>

#include <map>
#include <set>

#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <cstdio>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>

#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef pair<int, pair<int, int> > triple;

#define eps 1e-7
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define MP make_pair
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define tr(container, it) for(typeof((container).begin()) it = (container).begin(); it != (container).end(); it++)
#define MT(a,b,c) MP(a,MP(b,c))

char a[50][50];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int tests;
	scanf("%d\n", &tests);
	for (int test = 1; test <= tests; test++) {
		int r, c;
		scanf("%d %d\n", &r, &c);
		REP(i,r)
			REP(j,c)
				scanf("%c ", &a[i][j]);
		bool ok = true;
		for (int i = 0; i < r && ok; i++)
			for (int j = 0; j < c && ok; j++) {
				if (a[i][j] == '.')
					continue;
				if (a[i][j] == '#') {
					if (i + 1 >= r || j + 1 >= c) {
						ok = false;
						break;
					}
					if (a[i + 1][j] != '#' || a[i][j + 1] != '#' || a[i + 1][j
							+ 1] != '#') {
						ok = false;
						break;
					}
					a[i][j] = '/';
					a[i][j + 1] = '\\';
					a[i + 1][j] = '\\';
					a[i + 1][j + 1] = '/';
				}
			}
		REP(i,r)
			REP(j,c)
				if (a[i][j] == '#')
					ok = false;
		if (!ok) {
			printf("Case #%d:\nImpossible\n", test);
			continue;
		}
		printf("Case #%d:\n", test);

		REP(i,r) {
			REP(j,c) {
					printf("%c", a[i][j]);
			}
			printf("\n");
		}
	}

}
