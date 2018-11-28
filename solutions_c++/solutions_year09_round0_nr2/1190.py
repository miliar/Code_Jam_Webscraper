#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define inf 0x3f3f3f3f

typedef long long int64;
typedef double real;

#define maxs (1 << 8)

const int dx[] = {-1, 0, 0, 1};
const int dy[] = { 0,-1, 1, 0};

int alt[maxs][maxs];
char f[maxs][maxs];
int w, h;
char next;

inline bool onb(int x, int y) {
	return x >= 0 && x < h && y >= 0 && y < w;
}

char go(int x, int y) {
	if(f[x][y]) return f[x][y];
	int bdir = -1, balt;
	for(int i = 0; i < 4; i++) {
		int nx = x + dx[i], ny = y + dy[i];
		if(!onb(nx, ny)) continue;
		if(alt[nx][ny] < alt[x][y] && (bdir == -1 || alt[nx][ny] < balt)) {
			bdir = i;
			balt = alt[nx][ny];
		}
	}
	if(bdir == -1) {
		assert(next <= 'z');
		return f[x][y] = next++;
	}
	return f[x][y] = go(x + dx[bdir], y + dy[bdir]);
}


int main() {
	int t = 1, tc, i, j;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d:\n", t);
		scanf("%d%d", &h, &w);
		for(i = 0; i < h; i++)
			for(j = 0; j < w; j++)
				scanf("%d", alt[i] + j);
		memset(f, 0, sizeof(f));
		next = 'a';
		for(i = 0; i < h; i++, printf("\n"))
			for(j = 0; j < w; j++)
				printf("%c ", go(i, j));
	}
	return 0;
}
