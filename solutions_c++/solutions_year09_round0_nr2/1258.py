#include <iostream>
#include <climits>
#include <vector>
#include <algorithm>
#include <cstring>

#define MAXH 128
#define MAXW 128
#define INF INT_MAX

using namespace std;

int mark[MAXH][MAXW];
int value[MAXH][MAXW];
int result[MAXH][MAXW];

int ndir = 4, dirs[4][2] = {{-1, 0},{0, -1},{0, 1},{1, 0}};
vector <pair <int, int> > adj[MAXH][MAXW];

void dfs(int y, int x, char base)
{
	mark[y][x] = 1;
	result[y][x] = base;

	for (int i = 0; i < adj[y][x].size(); i++) {
		pair <int, int> p = adj[y][x][i];
		int y2 = p.first, x2 = p.second;

		if (!mark[y2][x2])
			dfs(y2, x2, base);
	}
}

int main(int argc, char ** argv)
{
	int ntest;

	scanf(" %d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int height, width;

		scanf(" %d %d", &height, &width);

		for (int y = 0; y < height; y++)
			for (int x = 0; x < width; x++) {
				scanf(" %d", &value[y][x]);
				adj[y][x].clear();
			}

		for (int y = 0; y < height; y++)
			for (int x = 0; x < width; x++) {
				int minv = INF;

				for (int d = 0; d < ndir; d++) {
					int y2 = y + dirs[d][0], x2 = x + dirs[d][1];

					if (0 <= y2 && y2 < height && 0 <= x2 && x2 < width)
						minv = min(minv, value[y2][x2]);
				}

				if (minv < value[y][x]) {
					for (int d = 0; d < ndir; d++) {
						int y2 = y + dirs[d][0], x2 = x + dirs[d][1];
						
						if (0 <= y2 && y2 < height && 0 <= x2 && x2 < width && value[y2][x2] == minv) {
							adj[y][x].push_back(make_pair(y2, x2));
							adj[y2][x2].push_back(make_pair(y, x));
							break;
						}
					}					
				}
			}

		memset(mark, 0, sizeof(mark));
		memset(result, -1, sizeof(result));

		char base = 'a';

		printf("Case #%d:\n", t+1);
		for (int y = 0; y < height; y++) {
			for (int x = 0; x < width; x++) {
				if (result[y][x] == -1) {
					dfs(y, x, base);
					base ++;
				}
				printf("%c", result[y][x]);
				if (x+1 < width)
					printf(" ");
			}
			printf("\n");
		}
	}

	return 0;
}
