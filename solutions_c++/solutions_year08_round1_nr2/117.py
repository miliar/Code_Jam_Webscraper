#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

const int MAXN = 2000;

int Ct, N, M, res[MAXN], im[MAXN];
vector< pair< int, int > > G[MAXN];

void read_data () {
	for (int i = 0; i < MAXN; ++i)
		G[i].clear ();

	memset (im, -1, sizeof (im));
	cin >> N >> M;

	for (int i = 0; i < M; ++i) {
		int T, X, Y;
		cin >> T;

		for (int j = 0; j < T; ++j) {
			cin >> X >> Y; --X;

			G[i].push_back (make_pair (X, Y));
			if (Y == 1) im[i] = X;
		}
	}
}

void solve () {
	memset (res, 0, sizeof (res));

	while (true) {
		bool ch = false;

		for (int i = 0; i < M; ++i) {
			bool good = false;

			for (int e = 0; e < G[i].size (); ++e)
				if (res[G[i][e].first] == G[i][e].second) { good = true; break; }

			if (!good) {
				if (im[i] == -1) { cout << "IMPOSSIBLE" << endl; return; }
				res[im[i]] = 1; ch = true;
			}
		}

		if (!ch) break;
	}

	for (int i = 0; i < N; ++i)
		cout << res[i] << " ";

	cout << endl;
}

int main () {
	cin >> Ct;

	for (int t = 0; t < Ct; ++t) {
		printf ("Case #%d: ", t+1);

		read_data ();
		solve ();
	}

	return 0;
}
