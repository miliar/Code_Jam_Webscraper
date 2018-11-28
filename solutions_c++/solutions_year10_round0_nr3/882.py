#include <iostream>
#include <algorithm>

using namespace std;

long long cnt[40][1000];
int nxt[40][1000];

int grp[1000];
int ngrps, k;


void dp() {
	fill(cnt[0], cnt[40], 0);
	fill(nxt[0], nxt[40], 0);
	int l = 0;
	int r = 0;
	int s = 0;
	for (int l = 0, r = 0; l < ngrps; s -= grp[l], l++) {
		while (s + grp[r] <= k && (s == 0 || r != l)) { s += grp[r]; r = (r + 1) % ngrps; }
		nxt[0][l] = r;
		cnt[0][l] = s;
	}
	for (int i = 1; i < 35; i++)
		for (int l = 0; l < ngrps; l++) {
			int mid = nxt[i - 1][l];
			cnt[i][l] = cnt[i - 1][l] + cnt[i - 1][mid];
			nxt[i][l] = nxt[i - 1][mid];
		}
}

int main() {
	int ncases;
	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++) {
		int nruns;
		cin >> nruns >> k >> ngrps;
		for (int i = 0; i < ngrps; i++)
			cin >> grp[i];
		dp();
		int j = 31;
		for (; !((nruns >> j) & 1); j--);
		int c = 0;
		long long p = 0;
		while (j >= 0) {
			if ((nruns >> j) & 1) { p += cnt[j][c]; c = nxt[j][c]; }
			j--;
		}
		cout << "Case #" << caseno << ": " << p << endl;
	}
	return 0;
}
