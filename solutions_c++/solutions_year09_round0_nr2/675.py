#include <stdio.h>
#include <string.h>
#include <vector>
#include <cassert>
#include <map>
#include <set>
#include <bitset>
#include <iostream>
#include <queue>
#define FOR(i,n) for(int i = 0; i < (int) (n); i++)
using namespace std;

int W, H;
int a[128][128];
int colors[128][128];
char classigns[64];

int dirs[4][2] = { { 0, -1 }, { -1, 0 }, { 1, 0 }, { 0, 1 } };

bool inrange(int x, int y) {
	return (x >= 0 && x < W && y >= 0 && y < H);
}

struct Pt {
	int x, y;
	Pt(){}
	Pt(int _x, int _y) { x = _x; y = _y; }
};

int main(void)
{
	//freopen("/home/vesko/gcj/b.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	
	FOR(tc, T) {
		printf("Case #%d:\n", tc + 1);
		scanf("%d%d", &H, &W);
		FOR(i, H) FOR(j, W) scanf("%d", &a[i][j]);
		memset(colors, 0xff, sizeof(colors));
		//
		queue<Pt> q;
		FOR(y, H) FOR(x, W) {
			bool sink = true;
			FOR(i, 4) {
				int nx = x + dirs[i][0];
				int ny = y + dirs[i][1];
				if (inrange(nx, ny) && a[ny][nx] < a[y][x]) sink = false;
			}
			if (sink) {
				q.push(Pt(x, y));
				colors[y][x] = q.size() - 1;
			}
		}
		//
		while (!q.empty()) {
			int x = q.front().x;
			int y = q.front().y;
			q.pop();
			int clr = colors[y][x];
			FOR(i, 4) {
				int nx = x + dirs[i][0];
				int ny = y + dirs[i][1];
				if (!inrange(nx, ny)) continue;
				if (colors[ny][nx] != -1) continue;
				int mdx = -1, mdy = -1, lalt = a[ny][nx];
				FOR(j, 4) {
					int tx = nx + dirs[j][0];
					int ty = ny + dirs[j][1];
					if (!inrange(tx, ty)) continue;
					if (a[ty][tx] < lalt) {
						lalt = a[ty][tx];
						mdx = tx;
						mdy = ty;
					}
				}
				if (mdx == x && mdy == y) {
					colors[ny][nx] = clr;
					q.push(Pt(nx, ny));
				}
			}
		}
		//
		memset(classigns, 0, sizeof(classigns));
		char letter = 'a';
		FOR(y, H) FOR(x, W) {
			assert(colors[y][x] != -1);
			if (classigns[colors[y][x]] == 0)
				classigns[colors[y][x]] = letter++;
		}
		assert(letter <= ('z'+1));
		FOR(y, H) {
			FOR(x, W) {
				if (x) printf(" ");
				printf("%c", classigns[colors[y][x]]);
			}
			printf("\n");
		}
	}
	return 0;
}
