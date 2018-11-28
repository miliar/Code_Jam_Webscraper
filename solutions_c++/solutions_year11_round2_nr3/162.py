#include <stdio.h>
#include <math.h>
#include <string.h>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
using namespace std;

int n, m;
int a[2048][2], b[2048];

struct Room {
	set<int> points;
	
	inline bool inside(int x, int y)
	{
		return points.find(x) != points.end() && points.find(y) != points.end();
	}
};

vector<vector<int> > p;
int C;
int colors[2048];
bool found;

void check(void)
{
	bitset<16> bs[16];
	for (int i = 0; i < (int) p.size(); i++)
		for (int j = 0; j < (int) p[i].size(); j++)
			bs[i].set(colors[p[i][j]]);
	for (int i = 0; i < (int) p.size(); i++)
		if (bs[i].count() < C) return;
	printf("%d\n", C);
	for (int i = 1; i <= n; i++) {
		if (i > 1) printf(" ");
		printf("%d", colors[i]);
	}
	printf("\n");
	found = true;
}

void bt(int idx)
{
	if (found) return;
	if (idx > n) { check(); return; }
	for (int i = 1; i <= C; i++) {
		colors[idx] = i;
		bt(idx + 1);
	}
}

void solve(void)
{
	scanf("%d%d", &n, &m);
	vector<Room> vr;
	Room r;
	for (int i = 1; i <= n; i++) r.points.insert(i);
	vr.push_back(r);
	for (int j = 0; j < 2; j++)
		for (int i = 0; i < m; i++) scanf("%d", &a[i][j]);
	for (int i = 0; i < m; i++) {
		sort(a[i], a[i] + 2);
		int k = 0;
		while (!vr[k].inside(a[i][0], a[i][1])) k++;
		Room newRoom;
		for (int j = a[i][0]; j <= a[i][1]; j++) {
			if (vr[k].points.find(j) != vr[k].points.end()) {
				newRoom.points.insert(j);
				if (j != a[i][0] && j != a[i][1])
					vr[k].points.erase(j);
			}
		}
		vr.push_back(newRoom);
	}
	C = 9999;
	p.clear();
	for (int i = 0; i < (int) vr.size(); i++) {
		vector<int> xx;
		for (set<int>::iterator it = vr[i].points.begin(); it != vr[i].points.end(); ++it)
			xx.push_back(*it);
		p.push_back(xx);
		C = min(C, (int) xx.size());
	}
	/*
	printf("Groups: ");
	for (int i = 0; i < (int) vr.size(); i++) {
		printf("[");
		for (set<int>::iterator it = vr[i].points.begin(); it != vr[i].points.end(); ++it)
			printf(" %d", *it);
		printf(" ]  ");
	}
	printf("\n");
	*/
	if (C > 5) {
		printf("%d\n", C);
		for (int i = 1; i <= n; i++) {
			if (i > 1) printf(" ");
			printf("%d", i);
		}
		printf("\n");
		return;
	}
	
	found = false;
	bt(1);
	
	
}

int main(void)
{
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}
