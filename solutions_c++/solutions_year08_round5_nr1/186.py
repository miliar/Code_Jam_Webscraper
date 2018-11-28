#include <cstdio>
#include <cctype>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxl = 606;
const int delta = 303;
const int sx = maxl - 1;
const int sy = maxl - 1;
const int maxn = 100000;
const int dire[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

bool link[maxl][maxl][4];
bool used[maxl][maxl], mark[maxl][maxl];
int area_1, area_2;
char str[maxl];

void Init() {
    int dd = 0, x = delta, y = delta;
    int L, T, i;
    scanf("%d", &L);
    memset(link, 1, sizeof link);
    memset(mark, 0, sizeof mark);
    mark[x][y] = 1;
    while (L--) {
	scanf("%s %d", str, &T);
	while (T--) {
	    for (i = 0; str[i]; i++)
		switch (toupper(str[i])) {
		case 'F' : {
		    switch (dd) {
		    case 0 : {
			link[x][y][3] = link[x - 1][y][1] = 0;
		    } break;
		    case 1 : {
			link[x][y][2] = link[x][y - 1][0] = 0;
		    } break;
		    case 2 : {
			link[x][y - 1][3] = link[x - 1][y - 1][1] = 0;
		    } break;
		    case 3 : {
			link[x - 1][y][2] = link[x - 1][y - 1][0] = 0;
		    } break;
		    }
		    x += dire[dd][0];
		    y += dire[dd][1];
		    mark[x][y] = 1;
		} break;
		case 'R' : {
		    dd = (dd + 1) % 4;
		} break;
		case 'L' : {
		    dd = (dd + 3) % 4;
		} break;
		}
	}
    }
    //printf("here\n");
}

inline bool Outside(int x, int y) {
    return x < 0 || y < 0 || x >= maxl || y >= maxl;
}

int queue[maxl * maxl][2];
int head, tail;

void Travel(int sx, int sy) {
    queue[0][0] = sx;
    queue[0][1] = sy;
    area_1 = 1;
    used[sx][sy] = 1;
    int x, y, _x, _y, i;
    for (head = tail = 0; head <= tail; head++) {
	x = queue[head][0];
	y = queue[head][1];
	for (i = 0; i < 4; i++)
	    if (link[x][y][i]) {
		_x = x + dire[i][0];
		_y = y + dire[i][1];
		if (Outside(_x, _y) || used[_x][_y]) continue;
		tail++;
		queue[tail][0] = _x;
		queue[tail][1] = _y;
		used[_x][_y] = 1;
		area_1++;
	    }
    }
}

/*
void Travel(int x, int y) {
    //printf("area_1 = %d\n", area_1);
    area_1++;
    used[x][y] = 1;
    int i, _x, _y;
    for (i = 0; i < 4; i++) {
	if (!link[x][y][i]) continue;
	_x = x + dire[i][0];
	_y = y + dire[i][1];
	if (Outside(_x, _y) || used[_x][_y]) continue;
	Travel(_x, _y);
    }
}
*/
void Work() {
    area_1 = 0;
    memset(used, 0, sizeof used);
    Travel(sx, sy);
    area_2 = area_1;
    int i, j, k, l;
    for (i = 0; i < maxl; i++) {
	for (j = 0; j < maxl && !mark[i][j]; j++);
	if (j >= maxl) continue;
	for (k = maxl - 1; k >= 0 && !mark[i][k]; k--);
	if (k < 0) continue;
	for (l = j; l < k; l++)
	    link[i][l][3] = link[i - 1][l][1] = 0;
    }
    for (i = 0; i < maxl; i++) {
	for (j = 0; j < maxl && !mark[j][i]; j++);
	if (j >= maxl) continue;
	for (k = maxl - 1; k >= 0 && !mark[k][i]; k--);
	if (k < 0) continue;
	for (l = j; l < k; l++)
	    link[l][i][2] = link[l][i - 1][0] = 0;
    }
    memset(used, 0, sizeof used);
    area_1 = 0;
    Travel(sx, sy);
    printf("%d\n", area_2 - area_1);
}

int main() {
    int t, i;
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
	printf("Case #%d: ", i + 1);
	Init();
	Work();
    }
    return 0;
}
