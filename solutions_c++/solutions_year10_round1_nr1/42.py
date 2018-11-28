#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define happify(c) if (c=='R') {redFlag=1;} else if (c == 'B') {blueFlag=1;}

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);
		
		int width, K;
		scanf("%d%d ",&width,&K);
		char grid[100][100];
		for (int i = 0; i < width; i++) {
			scanf("%s ",&grid[i]);
			for (int j = 0; j < width; j++) {
				for (int k = 0; k+1 < width; k++) {
					if (grid[i][k+1] == '.') {
						swap(grid[i][k],grid[i][k+1]);
					}
				}
			}
		}
		int blueFlag=0,redFlag=0;
		for (int i = 0; i < width; i++) {
			for (int j = 0; j < width; j++) {
				if (i+K-1 < width) {
					bool flag=1;
					for (int k = 0; k < K; k++) flag = flag && (grid[i][j] == grid[i+k][j]);
					if (flag) happify(grid[i][j]);
				}
				if (j+K-1 < width) {
					bool flag=1;
					for (int k = 0; k < K; k++) flag = flag && (grid[i][j] == grid[i][j+k]);
					if (flag) happify(grid[i][j]);
				}
				if (i+K-1 < width && j+K-1 < width) {
					bool flag=1;
					for (int k = 0; k < K; k++) flag = flag && (grid[i][j] == grid[i+k][j+k]);
					if (flag) happify(grid[i][j]);
				}
				if (i+K-1 < width && j >= K-1) {
					bool flag=1;
					for (int k = 0; k < K; k++) flag = flag && (grid[i][j] == grid[i+k][j-k]);
					if (flag) happify(grid[i][j]);
				}
			}
		}
		char* ans = "Neither";
		if (redFlag) {
			ans = "Red";
			if (blueFlag) ans = "Both";
		} else if (blueFlag) {
			ans = "Blue";
		}
		
		printf("Case #%d: %s\n",test,ans);
	}
}
