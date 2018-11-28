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


int em[10000], em2[10000];
int main() {
	freopen("e:\\code\\a\\a-small.in", "r", stdin);
	freopen("e:\\code\\a\\a-small.out", "w", stdout);
	int t, T, n, i, j, k;
	sc(T);
	for (t = 1; t <= T; ++t) {
		li res = 0;
		sc(n);
		fr(i, n) sc(em[i]);
		fr(i, n) sc(em2[i]);
		sort(em, em + n);
		sort(em2, em2 + n);
		reverse(em2, em2+ n);
		i = 0; j = n - 1;
		fr(i, n) res += (li) em[i] * em2[i];
		printf("Case #%d: %lld\n", t, res);
	}
	fclose(stdout);
	return 0;
}