#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
using namespace std;

int H, W;
int m[101][101];

struct Node {
	int p;
	int rank;
};

vector<Node> disSet;

void makeset(int i)
{
	disSet[i].p = i;
	disSet[i].rank = 0;
}

void link(int x, int y)
{
	if (disSet[x].rank > disSet[y].rank) {
		disSet[y].p = x;
	} else {
		disSet[x].p = y;
		if (disSet[x].rank == disSet[y].rank) {
			disSet[y].rank++;
		}
	}
}

int findSet(int x)
{
	if (x != disSet[x].p) return disSet[x].p = findSet(disSet[x].p);
	return disSet[x].p;
}

void un(int x, int y)
{
	link(findSet(x), findSet(y));
}

void calc()
{
	int i, j, k;
	disSet.resize(H*W);
	for (i=0; i<H*W; ++i) {
		makeset(i);
	}

	int di[] = {-1, 0, 0, 1};
	int dj[] = {0, -1, 1, 0};
	for (i=0; i<H; ++i) for (j=0; j<W; ++j) {
		int mi = -1, mj = -1;
		int mv = 1000000000;
		for (k=0; k<4; ++k) {
			int ni = i+di[k];
			int nj = j+dj[k];
			if (ni<0||ni>=H || nj<0||nj>=W) continue;
			if (m[ni][nj] < m[i][j] && m[ni][nj]<mv) {
				mi = ni;
				mj = nj;
				mv = m[ni][nj];
			}
		}

		if (mi != -1) {
			//cout << "link: " << i*W+j << ' ' << mi*W+mj << endl;
			un(i*W+j, mi*W+mj);
		}
	}

	map<int, int> mm;
	int cur = 0;
	vector<string> ans(H);
	for (i=0; i<H*W; ++i) {
		int s = findSet(i);
		//cout << i << ' ' << s << endl;
		if (mm.find(s) == mm.end()) {
			mm[s] = cur++;
		}

		ans[i/W] += char('a'+mm[s]);
	}

	for (i=0; i<H; ++i) {
		for (j=0; j<W; ++j) {
			if (j) cout << ' ';
			cout << ans[i][j];
		}
		cout << endl;
	}
}

int main(void)
{
	int T;
	cin >> T;
	for (int ca=1; ca<=T; ++ca) {
		cin >> H >> W;
		for (int i=0; i<H; ++i) for (int j=0; j<W; ++j) {
			cin >> m[i][j];
		}
		cout << "Case #" << ca << ":" << endl;
		calc();
	}
	return 0;
}
