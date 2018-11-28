#include <queue>
#include <sstream>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <set>
#include <cmath>
using namespace std;

const int M = 128;
const double eps=1e-9;
const int DIR[2][2]={{0,-1},{-1,0}}; //R,D,L,U
const int DIRX[8][2]={{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0},{-1,1}};

int R;
bool map[M][M];
bool newmap[M][M];

bool live(int r, int c) {
	bool alllive = true;
	bool alldead = true;
	for (int i = 0; i < 2; ++i) {
		int nr = r + DIR[i][0];
		int nc = c + DIR[i][1];
		if (nr >= 0 && nr < M && nc >= 0 && nc < M) {
			if (map[nr][nc])
				alldead = false;
			else
				alllive = false;
		} else {
			alllive = false;
		}
	}
	if (map[r][c])
		return !alldead;
	else
		return alllive;
}

int main() {
	int t, x1, x2, y1, y2;
	cin >> t;
	for (int kase = 0; kase < t; ++kase) {
		cin >> R;
		bool allfalse = true;
		for (int i = 0; i < R; ++i) {
			cin >> x1 >> y1 >> x2 >> y2;
			for (int r = y1 - 1; r < y2; ++r) {
				for (int c = x1 - 1; c < x2; ++c) {
					map[r][c] = true;
					allfalse = false;
				}
			}
		}
		int ret = 0;
		while (true) {
			bool haslive = false;
			for (int r = 0; r < M; ++r) {
				for (int c = 0; c < M; ++c) {
					if (map[r][c]) haslive = true; 
				}
				//printf("\n");
			}
			if (!haslive) break;
			ret ++;
			for (int r = 0; r < M; ++r) {
				for (int c = 0; c < M; ++c) {
					//printf("%d ", map[r][c]);
					newmap[r][c] = live(r, c);
					if (newmap[r][c])
						haslive = true; 
				}
				//printf("\n");
			}
			for (int r = 0; r < M; ++r) {
				for (int c = 0; c < M; ++c) {
					map[r][c] = newmap[r][c];
				}
			}
			memset(newmap, 0, sizeof(newmap));
		}
		cout << "Case #" << kase + 1 << ": " << ret << endl;
	}
	return 0;
}


