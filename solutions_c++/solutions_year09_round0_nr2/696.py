#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

size_t H,W;
size_t map[102][102];
int labels[102][102];

int dirs[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

bool Flow(size_t cif, size_t cjf, size_t cit, size_t cjt) {
	size_t mi = -1, mj = -1;
	if (map[cif][cjf] == 0)
		return false;
	for (size_t d=0;d<4;d++) {
		size_t i = cif + dirs[d][0];
		size_t j = cjf + dirs[d][1];
		if (i == 0 || i == H+1 || j == 0 || j == W+1)
			continue;
		if (map[i][j] < map[cif][cjf]) 
			if (mi == (size_t)-1 || map[i][j] < map[mi][mj]) {
				mi = i; mj = j;
			}
	}
	return mi == cit && mj == cjt;
}

void Fill(size_t ci, size_t cj, size_t id) {
	//cerr << "labels[" << ci << "][" << cj << "]=" << id << endl;
	labels[ci][cj] = id;
	for (int i=0;i<4;i++)
		if (Flow(ci+dirs[i][0], cj+dirs[i][1], ci, cj))
			Fill(ci+dirs[i][0], cj+dirs[i][1], id);
}

void Solve() {
	size_t ci,cj;
	size_t id = 0;
	do {
		ci = -1;
		for (size_t i=1;i<=H;i++)
			for (size_t j=1;j<=W;j++)
				if (labels[i][j] == -1) 
					if (ci == -1 || map[ci][cj] > map[i][j]) {
						ci = i; cj = j;
					}
		if (ci != -1) {
			//cerr << ci << ' ' << cj << endl;
			Fill(ci, cj, id);
			id++;
		}
	}while (ci != -1);
	int relabel[30];
	id = 0;
	memset(relabel,-1,sizeof(relabel));
	for (size_t i=1;i<=H;i++)
		for (size_t j=1;j<=W;j++)
			if (relabel[labels[i][j]] < 0)
				relabel[labels[i][j]] = id++;

	for (size_t i=1;i<=H;i++)
		for (size_t j=1;j<=W;j++)
			labels[i][j] = relabel[labels[i][j]];
}	

int main() {
	size_t N;
	cin >> N;
	for (int c=1;c<=N;c++) {
		cin >> H >> W;
		memset(map, 0, sizeof(map));
		memset(labels, -1, sizeof(labels));
		for (size_t i=1;i<=H;i++)
			for (size_t j=1;j<=W;j++)
				cin >> map[i][j];
		Solve();
		cout << "Case #" << c << ": " << endl;
		
		for (size_t i=1;i<=H;i++) {
			for (size_t j=1;j<=W;j++) {
				cout << (char)('a' + labels[i][j]);
				if (j!=W)
					cout << ' ';
			}
			cout << endl;
		}
	}

	return 0;
}
