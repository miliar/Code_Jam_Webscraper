#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int MAXN = 55;

int T;
int N, K;

char grid[MAXN][MAXN];

inline bool valid(int x) {return (x >= 0 && x < N);}
inline bool valid(int x, int y) {return (valid(x) && valid(y));}

inline bool line(int x, int y, int dx, int dy, char c) {
	for(int i = 0 ; i < K ; i++) {
		int xx = x + dx * i;
		int yy = y + dy * i;
		if (!valid(xx,yy) || grid[xx][yy] != c) {return false;}
	}
	return true;
}

inline bool good(char c) {
	for(int i = 0 ; i < N ; i++) {
		for(int j = 0 ; j < N ; j++) {
			if (line(i, j, 0, 1, c) || line(i, j, 1, 0, c) || line(i, j, 1, 1, c) || line(i, j, 1, -1, c)) {
				return true;
			}
		}
	}
	return false;
}

int main() {
	scanf("%d",&T);
	for(int t = 1 ; t <= T ; t++) {
		scanf("%d %d\n",&N,&K);
		for(int i = 0 ; i < N ; i++) {
			scanf("%s\n",&grid[i]);
			int ind = N - 1;
			for(int j = N - 1 ; j >= 0 ; j--) {
				if (grid[i][j] != '.') {
					grid[i][ind--] = grid[i][j];
				}
			}
			for(int j = ind ; j >= 0 ; j--) {
				grid[i][j] = '.';
			}
		}
		/*for(int i = 0 ; i < N ; i++) {
			for(int j = 0 ; j < N ; j++) {
				printf("%c",grid[i][j]);
			}
			printf("\n");
		}
		printf("\n");*/
		bool R = good('R'), B = good('B');
		printf("Case #%d: ",t);
		if (R) {
			if (B) {
				printf("Both\n");
			}	else {
				printf("Red\n");
			}
		}	else {
			if (B) {
				printf("Blue\n");
			}	else {
				printf("Neither\n");
			}
		}
		
	}
	return 0;
}
