#include <cstdio>/*{{{*/
#include <cassert>
#include <climits>
#include <iostream>
using namespace std;/*}}}*/

int N, D;
pair<int, int> vines[10000];

bool solve(int pos, int dx, int current_vine) {
	if (pos + dx >= D) {
		return true;
	}
	bool yes = false;
	for (int i = current_vine + 1; i < N; i++) {
		// grab one
		if (vines[i].first <= pos + dx) {
			if (solve(vines[i].first, min(vines[i].second, min(dx, vines[i].first - pos)), i)) {
					yes = true;
			}
		}
	}
	return yes;
}

int main(int argc, char const* argv[])
{
	int T;
	cin >> T;
	for (int ii = 0; ii < T; ii++) {
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> vines[i].first >> vines[i].second;
		}
		cin >> D;
		printf("Case #%d: %s\n", ii + 1, solve(vines[0].first, vines[0].first, 0)? "YES" : "NO");
	}
	return 0;
}

// vim: foldmethod=marker
