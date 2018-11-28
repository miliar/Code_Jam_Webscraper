#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <deque>
#include <memory>
using namespace std;
typedef vector<int> vi;
typedef long long li;
typedef pair<int,int> pi;
#define all(c) c.begin(), c.end()
#define fr(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define mp make_pair
#define INT 2147483647
#define X first
#define Y second
#define sc(a) scanf("%d", &(a))


int main() {
	freopen("e:\\code\\a\\a-large.in", "r", stdin);
	freopen("e:\\code\\a\\a-large.out", "w", stdout);

	int p, l, i, j, k, t, T, n;
	sc(T);
	for (t = 1; t <= T; ++t) {
		cin >> p >> k >> l;
		vi em(l);
		fr(i, l) sc(em[i]);
		sort(all(em), greater <int> ());
		int col = 1, lim = k;
		li res = 0;
		fr(i, em.size()) {
			if (i == lim) {
				lim += k;
				col++;
			}
			res += (li) col * em[i];
		}
		printf("Case #%d: %lld\n", t, res);
	}
	fclose(stdout);
	return 0;
}
