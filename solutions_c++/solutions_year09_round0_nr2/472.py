#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
using namespace std;

int basin[110][110], a[110][110], root[110][110], flow[110][110];
char ch[30];
int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int findroot(int i, int j) {
	if (basin[i][j] != 0)
		return (root[i][j] = basin[i][j]);
	return (root[i][j] = findroot(i+dir[flow[i][j]][0], j+dir[flow[i][j]][1]));
}

int main() {
	ifstream fin("B-large.in");
	ofstream fout("bout.txt");
	int T, w, h;
	fin >> T;
	for (int t = 0; t < T; t++) {
		fout << "Case #" << t+1 << ":\n";
		memset(a, 0, sizeof(a));
		fin >> h >> w;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				fin >> a[i][j];
			}
		}
		
		memset(basin, 0, sizeof(basin));
		int num = 0;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (i > 0 && a[i][j] > a[i-1][j]) continue;
				if (i < h-1 && a[i][j] > a[i+1][j]) continue;
				if (j > 0 && a[i][j] > a[i][j-1]) continue;
				if (j < w-1 && a[i][j] > a[i][j+1]) continue;
				basin[i][j] = ++num;
			}
		}

		memset(flow, 0, sizeof(flow));
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (basin[i][j] > 0) continue;
				int Min = a[i][j];
				for (int d = 0; d < 4; d++) {
					if (i+dir[d][0] < 0 || i+dir[d][0] >= h || j + dir[d][1] < 0 || j + dir[d][1] >= w)
						continue;
					if (Min > a[i+dir[d][0]][j+dir[d][1]]) {
						Min = a[i+dir[d][0]][j+dir[d][1]];
						flow[i][j] = d;
					}
				}
			}
		}
		memset(root, 0, sizeof(root));
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (root[i][j] == 0)
					findroot(i, j);
			}
		}
		memset(ch, 0, sizeof(ch));

		char nowch = 'a';
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (ch[root[i][j]] == 0)
					ch[root[i][j]] = nowch++;
				fout << ch[root[i][j]];
				if (j == w-1)
					fout << '\n';
				else
					fout << ' ';
			}
		}
	}
	return 0;
}
