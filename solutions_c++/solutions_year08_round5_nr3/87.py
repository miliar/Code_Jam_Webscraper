#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <set>

using namespace std;

int M, N;
char cl[100][100];
int F[100][100], nA, nB;
int G[10000][7], p[10000];
bool u[10000];

void read_data () {
	cin >> M >> N;

	for (int i = 0; i < M; ++i)
		scanf ("%s", cl[i]);

	memset (G, 0, sizeof (G));
	memset (p, -1, sizeof (p));
}

bool dfs_pair (int v) {
	u[v] = true;
	for (int e = 1; e <= G[v][0]; ++e)
		if (p[G[v][e]] == -1 || (!u[p[G[v][e]]] && dfs_pair (p[G[v][e]]))) { p[G[v][e]] = v; return true; }

	return false;
}

void solve () {
	nA = 0;
	for (int j = 0; j < N; j += 2)
		for (int i = 0; i < M; ++i)
			if (cl[i][j] == '.') F[i][j] = nA++;

	nB = 0;
	for (int j = 1; j < N; j += 2)
		for (int i = 0; i < M; ++i)
			if (cl[i][j] == '.') F[i][j] = nB++;

	for (int j = 0; j < N; j += 2)
		for (int i = 0; i < M; ++i)
			if (cl[i][j] == '.') {
				if (j > 0 && i > 0 && cl[i-1][j-1] == '.') { ++G[F[i][j]][0]; G[F[i][j]][G[F[i][j]][0]] = F[i-1][j-1]; }
				if (j > 0 && cl[i][j-1] == '.') { ++G[F[i][j]][0]; G[F[i][j]][G[F[i][j]][0]] = F[i][j-1]; }
				if (j > 0 && i < M-1 && cl[i+1][j-1] == '.') { ++G[F[i][j]][0]; G[F[i][j]][G[F[i][j]][0]] = F[i+1][j-1]; }

				if (j < N-1 && i > 0 && cl[i-1][j+1] == '.') { ++G[F[i][j]][0]; G[F[i][j]][G[F[i][j]][0]] = F[i-1][j+1]; }
				if (j < N-1 && cl[i][j+1] == '.') { ++G[F[i][j]][0]; G[F[i][j]][G[F[i][j]][0]] = F[i][j+1]; }
				if (j < N-1 && i < M-1 && cl[i+1][j+1] == '.') { ++G[F[i][j]][0]; G[F[i][j]][G[F[i][j]][0]] = F[i+1][j+1]; }
			}

	int ans = nA+nB;
	for (int i = 0; i < nA; ++i) {
		memset (u, 0, sizeof (u));
		if (dfs_pair (i)) --ans;
	}

	cout << ans << endl;
}

int main () {
	freopen ("C-large.in", "r", stdin);

	int T;
	cin >> T;

	for (int t = 0; t < T; ++t) {
		cout << "Case #" << t+1 << ": ";

		read_data ();
		solve ();
	}

	return 0;
}
