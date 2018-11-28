#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <map>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

#define MAX 100

typedef pair<int,int> pii;

int geti() { int n; scanf("%d", &n); return n; }

#define i(n) for (int i = 0; i < (n); i++)
#define j(n) for (int j = 0; j < (n); j++)

int T, H, W;
int Height[MAX][MAX];
int B[MAX][MAX];
vector<pii> basins;

void setup() {
	memset(Height, 0, MAX*MAX * sizeof(int));
	memset(B, -1, MAX*MAX * sizeof(int));
	basins.clear();


	H = geti();
	W = geti();
	i(H) {
		j(W) {
			Height[i][j] = geti();
		}
	}
}

bool valid(int r, int c) {
	return !(r < 0 || r >= H || c < 0 || c >= W);
}


int h(int r, int c) {
	if (valid(r, c)) return Height[r][c];
	else return 1000000;
}

int NB = 0;

int dfs(int vr, int vc) {
	if (B[vr][vc] != -1) {
		return B[vr][vc];
	} else {
		int minr = vr;
		int minc = vc;

		int ur = vr-1;
		int uc = vc;
		if (h(ur, uc) < h(minr, minc)) {
			minr = ur;
			minc = uc;
		}

		ur = vr;
		uc = vc-1;
		if (h(ur, uc) < h(minr, minc)) {
			minr = ur;
			minc = uc;
		}

		ur = vr;
		uc = vc+1;
		if (h(ur, uc) < h(minr, minc)) {
			minr = ur;
			minc = uc;
		}

		ur = vr+1;
		uc = vc;
		if (h(ur, uc) < h(minr, minc)) {
			minr = ur;
			minc = uc;
		}

		if (minr == vr && minc == vc) {
			B[vr][vc] = ++NB;
		} else {
			B[vr][vc] = dfs(minr, minc);
		}
		return B[vr][vc];
	}
}

void doIt() {
	i(H) {
		j(W) {
			dfs(i, j);
		}
	}
}

int Case;
map<int,char> Bmap;

void print() {
	char tb = 'a';
	printf("Case #%d:\n", Case);

	i(H) {
		j(W) {
			int bi = B[i][j];
			if (Bmap.find(bi) == Bmap.end()) {
				Bmap[bi] = tb++;
			}
			printf("%c ", Bmap[bi]);
		}
		printf("\n");
	}
}

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	T = geti();

	for (Case = 1; Case <= T; Case++) {
		setup();
		doIt();
		print();
	}
}