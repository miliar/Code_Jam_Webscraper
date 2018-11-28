#include<cstdio>
#include<cassert>
#include<cstring>
#include<map>
#include<set>
#include<time.h>
#include<algorithm>
#include<stack>
#include<queue>
#include<utility>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
using namespace std;

int h, w, d;
int density[501][501];
long long xsum[501][501], ysum[501][501], dsum[501][501];

long long sum(long long psum[501][501], int y1, int x1, int y2, int x2) {
	long long ret = psum[y2][x2];
	if(y1) ret -= psum[y1-1][x2];
	if(x1) ret -= psum[y2][x1-1];
	if(y1 && x1) ret += psum[y1-1][x1-1];
	return ret;
}

void toPartialSums(long long psum[501][501]) {
	for(int i = 0; i < h; i++)
		for(int j = 0; j < w; j++) {
			if(i) psum[i][j] += psum[i-1][j];
			if(j) psum[i][j] += psum[i][j-1];
			if(i && j) psum[i][j] -= psum[i-1][j-1];
		}
}

void genPartialSums() {
	for(int i = 0; i < h; i++)
		for(int j = 0; j < w; j++) {
			dsum[i][j] = density[i][j];
			xsum[i][j] = density[i][j] * (j * 2 + 1);
			ysum[i][j] = density[i][j] * (i * 2 + 1);
		}
	toPartialSums(dsum);
	toPartialSums(xsum);
	toPartialSums(ysum);
}

bool balanced(int y1, int x1, long long size) {
	int y2 = y1 + size - 1, x2 = x1 + size - 1;
	// y1 + size == weightedY / (size*size-4)
	// x1 + size == weightedX / (size*size-4)
	long long weightedY = sum(ysum, y1, x1, y2, x2) 
		- (y1*2+1) * (density[y1][x1] + density[y1][x2])
		- (y2*2+1) * (density[y2][x1] + density[y2][x2]);
	long long weightedX = sum(xsum, y1, x1, y2, x2) 
		- (x1*2+1) * (density[y1][x1] + density[y2][x1])
		- (x2*2+1) * (density[y1][x2] + density[y2][x2]);
	long long weight = sum(dsum, y1, x1, y2, x2) 
		- density[y1][x1] - density[y1][x2] 
		- density[y2][x1] - density[y2][x2];
	bool ret = (y1 * 2 + size) * weight == weightedY &&
		(x1 * 2 + size) * weight == weightedX;
	//printf("balanced(%d,%d,%Ld) = %d\n", y1, x1, size, int(ret));
	//printf("weightedY = %Ld, weightedX = %Ld, weight = %Ld\n", weightedY, weightedX, weight);
	return ret;
}

void solve() {
	for(int size = min(h, w); size >= 3; --size) {
		for(int y = 0; y + size <= h; ++y)
			for(int x = 0; x + size <= w; x++) {
				if(balanced(y, x, size)) {
					printf("%d\n", size);
					return;
				}					
			}
	}
	printf("IMPOSSIBLE\n");
}

int main() {
    int cases;
    scanf("%d", &cases);
    for(int cc = 0; cc < cases; ++cc) {
    	scanf("%d %d %d", &h, &w, &d);
    	for(int i = 0; i < h; i++) {
    		static char buf[601];
    		scanf("%s", buf);
			for(int j = 0; j < w; j++) 
				density[i][j] = d + buf[j] - '0';
		}
		genPartialSums();
		balanced(1, 1, 5);
		printf("Case #%d: ", cc+1);
		solve();
    }
}

