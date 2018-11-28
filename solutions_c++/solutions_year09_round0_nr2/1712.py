#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

const int MAXH = 100;
const int MAXW = 100;

int T;
int H, W;

const int dirs[5][2] = {{0, 0}, {-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int terr[MAXH][MAXW];
int dirf[MAXH][MAXW];
int belo[MAXH][MAXW];

int rr[MAXH * MAXW];
int cc[MAXH * MAXW];
int pp;

int GetDirf(int r, int c) {
	int v = terr[r][c];
	int min = 100000;
	int mind = 0;
	for (int i = 1; i <= 4; i++) {
		if (0 <= r + dirs[i][0] && r + dirs[i][0] < H && 0 <= c + dirs[i][1] && c + dirs[i][1] < W)
			if (terr[r + dirs[i][0]][c + dirs[i][1]] < min) {
				min = terr[r + dirs[i][0]][c + dirs[i][1]];
				mind = i;
			}
	}
	if (min >= v)
		return 0;
	else
		return mind;
}

void DoIt(int p) {
	memset(terr, 0, sizeof(terr));
	memset(dirf, 0, sizeof(dirf));
	memset(belo, 0, sizeof(belo));
	fin >> H >> W;
	for (int i = 0; i < H; i++)
		for (int j = 0; j < W; j++)
			fin >> terr[i][j];
	for (int i = 0; i < H; i++)
		for (int j = 0; j < W; j++)
			dirf[i][j] = GetDirf(i, j);

	int occ = 1;
	for (int i = 0; i < H; i++)
		for (int j = 0; j < W; j++)
			if (belo[i][j] == 0) {
				pp = 0;
				rr[pp] = i;
				cc[pp] = j;
				while (dirf[rr[pp]][cc[pp]] != 0 && belo[rr[pp]][cc[pp]] == 0) {					
					rr[pp + 1] = rr[pp] + dirs[dirf[rr[pp]][cc[pp]]][0];
					cc[pp + 1] = cc[pp] + dirs[dirf[rr[pp]][cc[pp]]][1];
					pp++;
				}
				if (belo[rr[pp]][cc[pp]] != 0) {
					for (int k = 0; k <= pp; k++) {
						belo[rr[k]][cc[k]] = belo[rr[pp]][cc[pp]];
					}
				}
				else {
					for (int k = 0; k <= pp; k++) {
						belo[rr[k]][cc[k]] = occ;
					}
					occ++;
				}
			}
	fout << "Case #" << p << ":" << endl;
	for (int i = 0; i < H; i++)
		for (int j = 0; j < W; j++) {
			fout << (char)('a' + belo[i][j] - 1);
			if (j == W - 1)
				fout << endl;
			else 
				fout << ' ';
		}
}

int main() {
	fin >> T;
	for (int i = 0; i < T; i++)
		DoIt(i + 1);
	return 0;
}