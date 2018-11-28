#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int T, N, NA, NB;
int TA[100][2], TB[100][2], p[200];
bool G[200][200], mark[200];

void read_data () {
	cin >> T >> NA >> NB;

	string s;

	for (int i = 0; i < NA; ++i) {
		cin >> s;
		TA[i][0] = ((s[0]-48)*10 + (s[1]-48))*60 + (s[3]-48)*10 + (s[4]-48);

		cin >> s;
		TA[i][1] = ((s[0]-48)*10 + (s[1]-48))*60 + (s[3]-48)*10 + (s[4]-48);
	}

	for (int i = 0; i < NB; ++i) {
		cin >> s;
		TB[i][0] = ((s[0]-48)*10 + (s[1]-48))*60 + (s[3]-48)*10 + (s[4]-48);

		cin >> s;
		TB[i][1] = ((s[0]-48)*10 + (s[1]-48))*60 + (s[3]-48)*10 + (s[4]-48);
	}
}

bool DFS_pair (int u) {
	mark[u] = true;

	for (int v = 0; v < NA+NB; ++v)
		if (G[u][v] && (p[v] == -1 || (!mark[p[v]] && DFS_pair (p[v])))) { p[v] = u; return true; }

	return false;
}

void solve () {
	memset (G, 0, sizeof (G));
	memset (p, -1, sizeof (p));

	for (int i = 0; i < NA; ++i)
		for (int j = 0; j < NB; ++j) {
			if (TA[i][1] + T <= TB[j][0]) G[i][NA+j] = true;
			if (TB[j][1] + T <= TA[i][0]) G[NA+j][i] = true;
		}

	for (int i = 0; i < NA+NB; ++i) {
		memset (mark, 0, sizeof (mark));
		DFS_pair (i);
	}

	int PA = 0, PB = 0;
	for (int i = 0; i < NA+NB; ++i)
		if (p[i] == -1)
			if (i < NA) ++PA; else ++PB;

	cout << PA << " " << PB << endl;
}

int main () {
	cin >> N;

	for (int t = 0; t < N; ++t) {
		cout << "Case #" << t+1 << ": ";

		read_data ();
		solve ();
	}

	return 0;
}
