#include <string>
#include <vector>
#include <fstream>
#include <iostream>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("output.txt");
int tt, h, w;
int weight[101][101];
int label[101][101];
int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

bool inbounds(int r, int c) { return r >= 0 && r < h && c >= 0 && c < w; }

int ffill(int r, int c) {
	if (label[r][c] != -1)
		return label[r][c];

	int dir = -1; int maxw = weight[r][c];
	for (int i = 0; i < 4; i++)
		if (inbounds(r + dr[i], c + dc[i]) && weight[r + dr[i]][c + dc[i]] < maxw)
			dir = i, maxw = weight[r + dr[i]][c + dc[i]];
	if (dir != -1)
		return ffill(r + dr[dir], c + dc[dir]);
	return -1;
}

void mark(int r, int c, int val) {
	if (label[r][c] != -1)
		return;

	label[r][c] = val;
	int dir = -1; int maxw = weight[r][c];
	for (int i = 0; i < 4; i++)
		if (inbounds(r + dr[i], c + dc[i]) && weight[r + dr[i]][c + dc[i]] < maxw)
			dir = i, maxw = weight[r + dr[i]][c + dc[i]];
	if (dir != -1)
		mark(r + dr[dir], c + dc[dir], val);
}

int main() {
	fin >> tt;
	for (int t = 0; t < tt; t++) {
		fin >> h >> w;
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				fin >> weight[i][j];

		memset(label, -1, sizeof(label));
		int index = 0;
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++) {
				int next = ffill(i, j);
				int label = next == -1 ? index++ : next;
				mark(i, j, label);
			}

		fout << "Case #" << t + 1 << ":" << endl;
		for (int i = 0; i < h; i++) {
			fout << (char) ('a' + label[i][0]);
			for (int j = 1; j < w; j++)
				fout << ' ' << (char) ('a' + label[i][j]);
			fout << endl;
		}
	}
	return 0;
}