#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
#define SIZE 100

int H, W;
int alt[SIZE][SIZE];
char basin[SIZE][SIZE];
char next;

typedef struct point {
	int x, y;
	int alt;
} point;

vector<point> points;
vector<point> mark[26];

point make_point(int x, int y) {
	point t = {x, y, 0};
	return t;
}

char find(int x, int y) {
	if(basin[x][y]) {
		return basin[x][y];
	}
	int minx = x, miny = y, minv = alt[x][y];
	if(x > 0 && alt[x - 1][y] < minv) {
		minx = x - 1; miny = y; minv = alt[x - 1][y];
	}
	if(y > 0 && alt[x][y - 1] < minv) {
		minx = x; miny = y - 1; minv = alt[x][y - 1];
	}
	if(y < W - 1 && alt[x][y + 1] < minv) {
		minx = x; miny = y + 1; minv = alt[x][y + 1];
	}
	if(x < H - 1 && alt[x + 1][y] < minv) {
		minx = x + 1; miny = y; minv = alt[x + 1][y];
	}
	char thisMark;
	if(x == minx && y == miny) {
		thisMark = next;
		next ++;
	} else {
		thisMark = find(minx, miny);
	}
	mark[thisMark - 'a'].push_back(make_point(x, y));
	return basin[x][y] = thisMark;
}

bool less_than(const point &l, const point &r) {
	return l.alt > r.alt || (l.alt == r.alt && l.x > l.x) ||
		(l.alt == r.alt && l.x == l.x & l.y > r.y);
}

int main() {
	int casa;
	scanf("%d", &casa);
	point t;
	for(int ncasa = 1; ncasa <= casa; ncasa ++) {
		scanf("%d %d", &H, &W);
		points.clear();
		for(int i = 0; i < 26; i++) {
			mark[i].clear();
		}
		for(t.x = 0; t.x < H; t.x++) {
			for(t.y = 0; t.y < W; t.y++) {
				scanf("%d", &t.alt);
				alt[t.x][t.y] = t.alt;
				basin[t.x][t.y] = 0;
				points.push_back(t);
			}
		}
		next = 'a';
		make_heap(points.begin(), points.end(), less_than);
		while(!points.empty()) {
			pop_heap(points.begin(), points.end(), less_than);
			t = points.back();
			points.pop_back();
			find(t.x, t.y);
		}
		
		next = 'a';
		for(int i = 0; i < H; i++) {
			for(int j = 0; j < W; j++) {
				char thisMark = basin[i][j];
				if(basin[i][j] < next) {
					continue;
				}
				
				if(basin[i][j] > next) {
					for(vector<point>::iterator it = mark[thisMark - 'a'].begin();
						it != mark[thisMark - 'a'].end(); ++it) {
						basin[it->x][it->y] = next;
					}
					for(vector<point>::iterator it = mark[next - 'a'].begin();
						it != mark[next - 'a'].end(); ++it) {
						basin[it->x][it->y] = thisMark;
					}
					mark[thisMark - 'a'] = mark[next - 'a'];
				}	
				// */
				next ++;
			}
		}
		
		printf("Case #%d:\n", ncasa);
		for(int i = 0; i < H; i++) {
			for(int j = 0; j < W; j++) {
				if(j > 0) {
					printf(" ");
				}
				printf("%c", basin[i][j]);
			}
			printf("\n");
		}
	}
}


