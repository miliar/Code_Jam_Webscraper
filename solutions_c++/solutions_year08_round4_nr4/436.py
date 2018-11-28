#include <algorithm>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <cmath>
#include <set>
#include <map>

using namespace std;

int k, N, p[5], res;
string S, T;
bool u[5];

void read_data () {
	cin >> k >> S;
	N = S.length ();
	res = 1000000000;
}

void calc () {
	T = "";

	for (int i = 0; i < N/k; ++i)
		for (int j = 0; j < k; ++j)
			T += S[i*k + p[j]];

	int tres = 0;
	for (int i = 0; i < N; ++i)
		if (i == 0 || T[i] != T[i-1]) ++tres;

	if (tres < res) res = tres;
}

void gen (int d) {
	if (d == k) { calc (); return; }

	for (int i = 0; i < k; ++i)
		if (!u[i]) {
			u[i] = true; p[d] = i;
			gen (d+1);
			u[i] = false;
		}
}

void solve () {
	memset (u, 0, sizeof (u));
	gen (0);
	cout << res << endl;
}

int main () {
	freopen ("D-small-attempt0.in", "r", stdin);

	int Ct;
	cin >> Ct;

	for (int t = 0; t < Ct; ++t) {
		printf ("Case #%d: ", t+1);

		read_data ();
		solve ();
	}

	return 0;
}
