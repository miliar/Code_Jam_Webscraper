/*
 * main.cpp
 *
 *  Created on: 2009-9-3
 *      Author: megatang
 */

#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

struct node {
	int x, y;
};

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};
int map[101][101];
int mark[101][101];
node stack[10000];
int stack_size;
char translate[100];
int translated;
int num;
int W, H;

bool is_basin(int x, int y) {
	int current = map[x][y];
	for (int i = 0; i < 4; i++) {
		int tx = x + dx[i];
		int ty = y + dy[i];
		if (tx >= 0 && tx < W && ty >= 0 && ty < H && map[tx][ty] < current)
			return false;
	}
	return true;
}

int main() {
	int T;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> T;
	for (int cnt = 0; cnt < T; cnt++) {
		fin >> H >> W;
		memset(map, 0, sizeof(map));
		memset(mark, 0, sizeof(mark));
		memset(translate, 0, sizeof(translate));
		num = 0;
		translated = 0;
		for (int y = 0; y < H; y++)
			for (int x = 0; x < W; x++)
				fin >> map[x][y];
		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++) {
				if (mark[x][y] != 0)
					continue;
				stack_size = 0;
				int tx = x, ty = y;
				while (!is_basin(tx, ty) && mark[tx][ty] == 0) {
					int min = map[tx][ty];
					int j = -1;
					for (int i = 0; i < 4; i++) {
						int nx = tx + dx[i], ny = ty + dy[i];
						if (nx < 0 || nx >= W || ny < 0 || ny >= H)
							continue;
						if (map[nx][ny] < min) {
							min = map[nx][ny];
							j = i;
						}
					}
					if (j != -1) {
						stack[stack_size].x = tx;
						stack[stack_size].y = ty;
						tx = tx + dx[j];
						ty = ty + dy[j];
						stack_size++;
					}
				}
				if (mark[tx][ty] == 0)
					mark[tx][ty] = ++num;
				for (int i = 0; i < stack_size; i++)
					mark[stack[i].x][stack[i].y] = mark[tx][ty];
			}
		}
		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++) {
				if (translate[mark[x][y]] == 0)
					translate[mark[x][y]] = 'a' + translated++;
				else
					continue;
			}
		}
		cout << cnt + 1 << endl;
		fout << "Case #" << cnt + 1 << ":" << endl;
		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++) {
				cout << mark[x][y];
				fout << translate[mark[x][y]];
				if (x < W - 1) {
					fout << ' ';
				cout << ' ';
				}
			}
			cout << endl;
			fout << endl;
		}
	}
	fout.close();
	return 0;
}
