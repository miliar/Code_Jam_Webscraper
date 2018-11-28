#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
//#include <string>
//#include <map>
#include <vector>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

int H, W;

// North, west, east, south
int dx[] = { -1,  0,  0,  1 };
int dy[] = {  0, -1,  1,  0 };

char dfs(const vector<vector<int> > &height, vector<vector<char> > &basin, char next, int x, int y) { 
	if(basin[x][y])
		return basin[x][y];

	int minh = height[x][y];
	int mindir = -1;

	for(int i = 0; i < 4; ++i) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if(nx >= 0 && nx < H && ny >= 0 && ny < W) {
			if(height.at(nx).at(ny) < minh) {
				minh = height[nx][ny];
				mindir = i;
			}
		}
	}

	if(mindir == -1) {
		basin[x][y] = next;
		return next++;
	}

	return basin[x][y] = dfs(height, basin, next, x + dx[mindir], y + dy[mindir]);
}

bool solve(int P) {
	printf("Case #%d:\n", P+1);
	if(scanf("%d%d", &H, &W) != 2)
		assert(!"Failed to read h,w");

	vector<vector<int> > height(H);
	vector<vector<char> > basin(H);

	for(int i = 0; i < H; ++i) {
		height[i].resize(W);
		basin[i].resize(W);
		for(int k = 0; k < W; ++k) {
			if(scanf("%d", &height[i][k]) != 1)
				assert(!"Failed to read height");
		}
	}

	char cur = 'a';

	for(int i = 0; i  < H; ++i) {
		for(int k = 0; k < W; ++k) {
			if(!basin[i][k]) {
				cur = max<char>(cur, dfs(height, basin, cur, i, k) + 1);
			}
		}
	}

	for(int i = 0; i < H; ++i) {
		for(int k = 0; k < W; ++k) {
			assert(basin[i][k]);
			if(k)
				printf(" ");
			printf("%c", basin[i][k]);
		}
		printf("\n");
	}

	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
