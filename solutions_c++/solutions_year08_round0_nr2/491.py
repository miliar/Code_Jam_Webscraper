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
	//freopen("e:\\B-large.in", "r", stdin);
	//freopen("e:\\B-large.out", "w", stdout);
	int na, nb, h, m, h2, m2, i, j, k, cur, x1, x2, t, t_, x;
	sc(t_);
	for (t = 1; t <= t_; ++t) {
		vi a(2000), b(2000);
		scanf("%d", &x);
		scanf("%d%d", &na, &nb);
		fr(i, na) {
			scanf("%d:%d %d:%d", &h, &m, &h2, &m2);
			a[h * 60 + m]++;
			b[h2 * 60 + m2 + x]--;
		}
		fr(i, nb) {
			scanf("%d:%d %d:%d", &h, &m, &h2, &m2);
			b[h * 60 + m]++;
			a[h2 * 60 + m2 + x]--;
		}
		x1 = x2 = cur = 0;
		fr(i, 2000) {cur += a[i]; x1 = max(x1, cur);}
		cur = 0;
		fr(i, 2000) {cur += b[i]; x2 = max(x2, cur);}
		printf("Case #%d: %d %d\n", t, x1, x2);
	}
	fclose(stdout);
	return 0;
}