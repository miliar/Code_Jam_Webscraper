#include <cstdio>
#include <cstring>
#include <cassert>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;

#define inf 0x3f3f3f3f

#define maxs (1 << 13)

//int mark[maxs][maxs];
char isb[maxs][maxs][4];

int dx[4] = { 0,-1, 0, 1};
int dy[4] = { 1, 0,-1, 0};

int main() {
	int t, tc;
	std::cin >> tc;
	for(t = 1; t <= tc; t++) {
//		memset(mark, 0, sizeof(mark));
		memset(isb, 0, sizeof(isb));
		int l, i, j, k;
		std::string s, st;
		std::cin >> l;
		for(i = 0; i < l; i++) {
			std::cin >> st >> k;
			for(j = 0; j < k; j++) s += st;
		}
//		Eo(s);
		int x = maxs/2, y = maxs/2, dir = 0;
		for(i = 0; i < s.length(); i++)
			switch(s[i]) {
			case 'R': dir = (dir + 3) % 4; break;
			case 'L': dir = (dir + 1) % 4; break;
			case 'F': {
				switch(dir) {
				case 0: isb[x-1][y][3] = 1; isb[x][y][1] = 1; break;
				case 1: isb[x-1][y-1][0] = 1; isb[x-1][y][2] = 1; break;
				case 2: isb[x-1][y-1][3] = 1; isb[x][y-1][1] = 1; break;
				case 3: isb[x][y][2] = 1; isb[x][y-1][0] = 1; break;
				}
//				fprintf(stderr, "(%d, %d) : %d\n", x-maxs/2, y-maxs/2, dir);
				x += dx[dir]; y += dy[dir];
//				fprintf(stderr, "->(%d, %d)\n", x-maxs/2, y-maxs/2);
				break;
			}
			default: assert(0);
		}
		
		for(i = 1; i < maxs; i++)
			for(j = 1; j < maxs; j++) {
				isb[i][j][2] += isb[i][j-1][2];
				if(isb[i][j][2]  >= 100) isb[i][j][2] -= 50;
				isb[i][j][1] += isb[i-1][j][1];
				if(isb[i][j][1] >= 100) isb[i][j][1] -= 50;
			}
		for(i = maxs-2; i >= 0; i--)
			for(j = maxs-2; j >= 0; j--) {
				isb[i][j][0] += isb[i][j+1][0];
				if(isb[i][j][0] >= 100) isb[i][j][0] -= 50;
				isb[i][j][3] += isb[i+1][j][3];
				if(isb[i][j][3] >= 100) isb[i][j][3] -= 50;
			}
		int ans = 0;
		for(i = 0; i < maxs; i++)
			for(j = 0; j < maxs; j++) {
				bool f1 = isb[i][j][0] > 0 && isb[i][j][2] > 0 &&
					(isb[i][j][0] & 1) == 0 && (isb[i][j][2] & 1) == 0;
				bool f2 = isb[i][j][1] > 0 && isb[i][j][3] > 0 && 
					(isb[i][j][1] & 1) == 0 && (isb[i][j][3] & 1) == 0;
				if(f1 || f2) ans++;
			}
/*		Eo(char(isb[maxs/2-1][maxs/2][3]+'0'));
		for(j = maxs/2+5; j >= maxs/2-1; j--, fprintf(stderr, "\n"))
			for(i = maxs/2-1; i < maxs/2 + 6; i++) {
				fprintf(stderr, "%d", isb[i][j][2]);
//				fprintf(stderr, ((isb[i][j][0] && isb[i][j][2]) ||
//					(isb[i][j][1] && isb[i][j][3]) ? "x" : "."));
			}*/
		printf("Case #%d: %d\n", t, ans);
		fflush(stdout);
	}
	return 0;
}
