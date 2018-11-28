#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

const int MAXN = 100;
const int MAXAT = 10000;
const int DIR[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int cnt;
int H, W;
int map[MAXN][MAXN];
char basin[MAXN][MAXN];

inline bool check(int r, int c){
	return (r >= 0 && r < H && c >= 0 && c < W);
}

void makeBasin(int r, int c){
	int minAt = MAXAT+1, minD = -1;
	for(int d=0; d<4; d++){
		int nr = r+DIR[d][0];
		int nc = c+DIR[d][1];
		if (check(nr, nc) && map[nr][nc] < minAt){
			minAt = map[nr][nc];
			minD = d;
		}
	}
	if (minAt >= map[r][c]){
		basin[r][c] = 'a'+cnt++;
		return;
	}
	int nr = r+DIR[minD][0];
	int nc = c+DIR[minD][1];
	if (basin[nr][nc] == 0)
		makeBasin(nr, nc);
	basin[r][c] = basin[nr][nc];
}

int main(int argc, char* args[]){
	if (argc < 3){
		cout << "lack of args" << endl;
		return 0;
	}
	freopen(args[1], "r", stdin);
	freopen(args[2], "w", stdout);
	int T;
	cin >> T;
	for(int ic=0; ic<T; ic++){
		cin >> H >> W;
		for(int r=0; r<H; r++)
			for(int c=0; c<W; c++)
				cin >> map[r][c];
		memset(basin, 0, sizeof(basin));
		cnt = 0;
		for(int r=0; r<H; r++)
			for(int c=0; c<W; c++)
				if (basin[r][c] == 0)
					makeBasin(r, c);
		printf("Case #%d:\n", ic+1);
		for(int r=0; r<H; r++)
			for(int c=0; c<W; c++){
				cout << basin[r][c];
				if (c < W-1)
					cout << ' ';
				else
					cout << endl;
			}
	}
}

