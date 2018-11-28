#include <cstdio>

int height[100][100];
int fd[100][100];
int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};
int c[100][100];
bool visited[100][100];
int component;
int h, w;

void fill(int y, int x) {
    if(visited[y][x])
	return;
    visited[y][x] = true;
    c[y][x] = component;

    for(int d = 0; d < 4; d++) {
	int y1 = y + dy[d];
	int x1 = x + dx[d];
	if(y1 >= 0 && h > y1 && x1 >= 0 && w > x1 && (fd[y][x] == d || (fd[y1][x1] >= 0 && fd[y1][x1] + d == 3)))
	    fill(y1, x1);
    }
}

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int nCases;
    scanf("%d", &nCases);

    for(int casenum = 1; casenum <= nCases; casenum++) {

	scanf("%d", &h);
	scanf("%d", &w);

	for(int i = 0; i < h; i++)
	    for(int j = 0; j < w; j++) {
		scanf("%d", &height[i][j]);
		c[i][j] = -1;
		visited[i][j] = false;
	    }

	for(int y = 0; y < h; y++) {
	    for(int x = 0; x < w; x++) {
		int minh = 1000000;
		fd[y][x] = -1;
		for(int d = 0; d < 4; d++) {
		    int x1 = x + dx[d];
		    int y1 = y + dy[d];
		    if(x1 >= 0 && w > x1 && y1 >= 0 && y1 < h && height[y1][x1] < minh && height[y1][x1] < height[y][x]) {
			minh = height[y1][x1];
			fd[y][x] = d;
		    }
		}
	    }
	}

	component = 0;
	for(int i = 0; i < h; i++)
	    for(int j = 0; j < w; j++) {
		if(c[i][j] == -1) {
		    fill(i,j);
		    component++;
		}
	    }

	printf("Case #%d:\n", casenum);
	for(int i = 0; i < h; i++) {
	    printf("%c", 'a' + (char)c[i][0]);
	    for(int j = 1; j < w; j++) {
		printf(" %c", 'a' + (char)c[i][j]);
	    }
	    printf("\n");
	}


    }
}
