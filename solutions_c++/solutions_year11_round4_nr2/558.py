#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int MAXN = 500+5;

int R, C, D;

char w[MAXN][MAXN];

int cx, cy;
int massX, massY;

void add(int x, int y, int d) {
	int wx = x-cx;
	int wy = y-cy;

	massX += d*(w[x][y]+D)*wx;
	massY += d*(w[x][y]+D)*wy;
}

void add2(int x, int y, int d) {	
	int ox = x;
	int oy = y;

	int cx = 2*::cx+1;
	int cy = 2*::cy+1;
	x*=2;
	y*=2;
	int wx = x-cx;
	int wy = y-cy;

	massX += d*(w[ox][oy]+D)*wx;
	massY += d*(w[ox][oy]+D)*wy;
}


void solve(int caseNumber) {
	scanf("%d %d %d", &R, &C, &D); 

	D = 0;
	for(int i = 0; i < R; i++) scanf("%s", w[i]);

	
	
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {		
			w[i][j] -= '0';
		}
	}

	int res = 0;

	for(cx = 0; cx < R; cx++) {
		for(cy = 0; cy < C; cy++) {

			massX = 0;
			massY = 0;

			for(int k = 1; k;k++) {

				int leftCornerX = cx - k;
				int leftCornerY = cy - k;

				int width = 2*k+1;

				int rightCornerX = leftCornerX+width-1;				
				int rightCornerY = leftCornerY+width-1;

				if(leftCornerX < 0 || leftCornerY < 0 || rightCornerX >= R || rightCornerY >= C) break;


				for(int i = 0; i < width; i++) {
					add(leftCornerX+i, leftCornerY, 1);	
					add(leftCornerX+i, rightCornerY, 1);					
					add(leftCornerX, leftCornerY+i, 1);
					add(rightCornerX, leftCornerY+i, 1);
				}

				add(leftCornerX, leftCornerY, -2);	
				add(leftCornerX, rightCornerY, -2);					
				add(rightCornerX, leftCornerY, -2);
				add(rightCornerX, rightCornerY, -2);

				if(massX == 0 && massY == 0 && width >= 3) {
					res = max(res, width);
				}
				add(leftCornerX, leftCornerY, 1);	
				add(leftCornerX, rightCornerY, 1);					
				add(rightCornerX, leftCornerY, 1);
				add(rightCornerX, rightCornerY, 1);			

			}
		}
	}


	for(cx = 0; cx < R; cx++) {
		for(cy = 0; cy < C; cy++) {

			massX = 0;
			massY = 0;

			for(int k = 1; k;k++) {

				int leftCornerX = cx - k+1;
				int leftCornerY = cy - k+1;

				int width = 2*k;

				int rightCornerX = leftCornerX+width-1;				
				int rightCornerY = leftCornerY+width-1;

				if(leftCornerX < 0 || leftCornerY < 0 || rightCornerX >= R || rightCornerY >= C) break;


				for(int i = 0; i < width; i++) {
					add2(leftCornerX+i, leftCornerY, 1);	
					add2(leftCornerX+i, rightCornerY, 1);					
					add2(leftCornerX, leftCornerY+i, 1);
					add2(rightCornerX, leftCornerY+i, 1);
				}

				add2(leftCornerX, leftCornerY, -2);	
				add2(leftCornerX, rightCornerY, -2);					
				add2(rightCornerX, leftCornerY, -2);
				add2(rightCornerX, rightCornerY, -2);

				if(massX == 0 && massY == 0 && width >= 3) {
					res = max(res, width);
				}
				add2(leftCornerX, leftCornerY, 1);	
				add2(leftCornerX, rightCornerY, 1);					
				add2(rightCornerX, leftCornerY, 1);
				add2(rightCornerX, rightCornerY, 1);			

			}
		}
	}




	printf("Case #%d: ", caseNumber);
	if(res == 0) printf("IMPOSSIBLE\n");
	else printf("%d\n",  res);

}


int main() {
//	freopen("in.txt", "r", stdin);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) solve(i);
}