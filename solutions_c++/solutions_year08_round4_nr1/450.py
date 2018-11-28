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

vector< int > tree, change, res[2];
int M, V;

void read_data () {
	cin >> M >> V;
	tree.resize (M);
	res[0].resize (M);
	res[1].resize (M);
	change.resize ((M-1)/2);

	fill (res[0].begin (), res[0].end (), -1);
	fill (res[1].begin (), res[1].end (), -1);

	for (int i = 0; i < M; ++i) {
		cin >> tree[i];
		if (i < (M-1)/2) cin >> change[i];
	}
}

int op (int a, int b, int c) {
	if (c == 0) return a || b; else return a && b;
}

void solve () {
	for (int i = (M-1)/2; i < M; ++i) res[tree[i]][i] = 0;

	for (int i = (M-1)/2-1; i >= 0; --i) {
		if (change[i] == 0) {
			for (int a = 0; a < 2; ++a)
				for (int b = 0; b < 2; ++b)
					if (res[a][i*2+1] != -1 && res[b][i*2+2] != -1 && (res[op (a, b, tree[i])][i] == -1 || res[op (a, b, tree[i])][i] > res[a][i*2+1] + res[b][i*2+2])) res[op (a, b, tree[i])][i] = res[a][i*2+1] + res[b][i*2+2];
		} else {
			for (int a = 0; a < 2; ++a)
				for (int b = 0; b < 2; ++b)
					for (int c = 0; c < 2; ++c)
						if (res[a][i*2+1] != -1 && res[b][i*2+2] != -1 && (res[op (a, b, tree[i] ^ c)][i] == -1 || res[op (a, b, tree[i] ^ c)][i] > res[a][i*2+1] + res[b][i*2+2] + c)) res[op (a, b, tree[i] ^ c)][i] = res[a][i*2+1] + res[b][i*2+2] + c;
		}
	}

	if (res[V][0] == -1)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << res[V][0] << endl;
}

int main () {
	freopen ("A-large.in", "r", stdin);

	int Ct;
	cin >> Ct;

	for (int t = 0; t < Ct; ++t) {
		printf ("Case #%d: ", t+1);

		read_data ();
		solve ();
	}

	return 0;
}
