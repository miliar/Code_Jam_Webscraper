#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

#define sz(v)		((int)(v.size()))
#define fn(i, n)	for(int i = 0; i < (n); ++i)
#define set1(a)		memset(a, 0x3f, sizeof(a))
#define INF			0x3f3f3f3f

int n, T, m, r, v, ans;
int node[20000], type[20000], sol[20000][2];

int solve(int nod, int val) {
	if (sol[nod][val] != INF)
		return sol[nod][val];
	int &res = sol[nod][val];
	int tmp1, tmp2;
	if (nod >= r) {
		if (node[nod] == val) res = 0;
	} else {
		if (node[nod] == 1 || type[nod] == 1) {
			// AND
			if (val) {
				tmp1 = solve(nod*2 + 1, 1);
				tmp2 = solve(nod*2 + 2, 1);
				if (tmp1 >= 0 && tmp2 >= 0 && res > (tmp1 + tmp2 + (node[nod] == 1 ? 0 : 1)))
					res = tmp1 + tmp2 + (node[nod] == 1 ? 0 : 1);
			} else {
				tmp1 = solve(nod*2 + 1, 0);
				tmp2 = solve(nod*2 + 2, 0);
				if ((tmp2 >= 0 && tmp2 < tmp1) || tmp1 < 0)
					tmp1 = tmp2;
				if (tmp1 >= 0 && res > (tmp1 + (node[nod] == 1 ? 0 : 1)))
					res = tmp1 + (node[nod] == 1 ? 0 : 1);
			}
		}
		if (node[nod] == 0 || type[nod] == 1) {
			// OR
			if (!val) {
				tmp1 = solve(nod*2 + 1, 0);
				tmp2 = solve(nod*2 + 2, 0);
				if (tmp1 >= 0 && tmp2 >= 0 && res > (tmp1 + tmp2 + (node[nod] == 0 ? 0 : 1)))
					res = tmp1 + tmp2 + (node[nod] == 0 ? 0 : 1);
			} else {
				tmp1 = solve(nod*2 + 1, 1);
				tmp2 = solve(nod*2 + 2, 1);
				if ((tmp2 >= 0 && tmp2 < tmp1) || tmp1 < 0)
					tmp1 = tmp2;
				if (tmp1 >= 0 && res > (tmp1 + (node[nod] == 0 ? 0 : 1)))
					res = tmp1 + (node[nod] == 0 ? 0 : 1);
			}
		}
	}
	if (res == INF) res = -1;
	return res;
}

int main() {
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	cin >> T;
	fn(test, T) {
		cin >> m >> v;
		r = (m-1)/2;
		fn(i, r) cin >> node[i] >> type[i];
		fn(i, m-r) cin >> node[i+r];
		set1(sol);
		ans = solve(0, v);
		cout << "Case #" << test+1 << ": ";
		if (ans < 0) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << endl;
	}

	return 0;
}
