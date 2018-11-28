#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
using namespace std;

int H, W;
int m[110][110];
char res[110][110];
int cnt;
int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

char color(int r, int c) {
	if (res[r][c] != 0) return res[r][c];
	int nextr, nextc = -1;
	int lowest = m[r][c];
	for (int i = 0; i < 4; i++) {
		int nr = r+dr[i], nc = c+dc[i];
		if (0 <= nr && nr < H && 0 <= nc && nc < W && m[nr][nc] < lowest) {
			lowest = m[nr][nc];
			nextr = nr, nextc = nc;
		}
	}
	if (nextc == -1) return res[r][c] = 'a'+(cnt++);
	return res[r][c] = color(nextr, nextc);
}

int main() {
	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("B-large.out", "w");
	
	int numtests;
	fscanf(fin, "%d", &numtests);

	for (int i = 0; i < numtests; i++) {
		fscanf(fin, "%d %d", &H, &W);
		for (int j = 0; j < H; j++) for (int k = 0; k < W; k++) fscanf(fin, "%d", &m[j][k]);
			
		cnt = 0;
		memset(res, 0, sizeof(res));
		for (int j = 0; j < H; j++) for (int k = 0; k < W; k++)
			if (res[j][k] == 0) color(j, k);

		fprintf(fout, "Case #%d:\n", i+1);
		for (int j = 0; j < H; j++) {
			for (int k = 0; k < W; k++) fprintf(fout, "%c ", res[j][k]);
			fprintf(fout, "\n");
		}
	}

	fclose(fin);
	fclose(fout);
	return 0;
}


