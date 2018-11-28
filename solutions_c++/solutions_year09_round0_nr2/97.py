#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <math.h>
#include <algorithm>
#define fori(n) for (int i = 0; i < n; i++)
#define forj(n) for (int j = 0; j < n; j++)
#define fork(n) for (int k = 0; k < n; k++)
#define MAXD 100
#define SUPER 999999
using namespace std;

int grid[MAXD][MAXD];
int basin[MAXD][MAXD];
char cbasin[MAXD][MAXD];
int T,H,W;
int max_basin = 0;

void cbasinfill(int num, char c) {
	for (int h = 0; h < H; h++) {
		for (int w = 0; w < W; w++) {
			if (basin[h][w] == num) {
				cbasin[h][w] = c;
			}
		}
	}
}

int getgrid(int h, int w) {
	if (h < 0 || w < 0 || h >= H || w >= W) return SUPER;
	//if (basin[h][w]) return SUPER
	return grid[h][w];
}

int get_basin_num(int h, int w) {
	if (basin[h][w]) return basin[h][w];
	int nh,nw;

	int cur = grid[h][w];

	int min_n = cur;
	bool sink = true;

	// NORTH
	if (getgrid(h-1,w) < min_n) {
		nh = h - 1;
		nw = w;
		min_n = getgrid(nh,nw);
		sink = false;
	}

	// WEST
	if (getgrid(h,w-1) < min_n) {
		nh = h;
		nw = w-1;
		min_n = getgrid(nh,nw);
		sink = false;
	}

	// EAST
	if (getgrid(h,w+1) < min_n) {
		nh = h;
		nw = w+1;
		min_n = getgrid(nh,nw);
		sink = false;
	}

	// SOUTH
	if (getgrid(h+1,w) < min_n) {
		nh = h + 1;
		nw = w;
		min_n = getgrid(nh,nw);
		sink = false;
	}

	if (sink) {
		max_basin++;
		basin[h][w] = max_basin;
		return max_basin;
	} else {
		basin[h][w] = get_basin_num(nh,nw);
	}
}

/*
int floodfill(int h, int w, int basin_num) {
	if (getgrid(h,w) == -1) return 0;
	basin[h][w] = basin_num;

	int floodcount = 1;
	int cur = grid[h][w];

	if (cur < getgrid(h-1,w)) floodcount += floodfill(h-1,w,basin_num);
	if (cur < getgrid(h+1,w)) floodcount += floodfill(h+1,w,basin_num);
	if (cur < getgrid(h,w-1)) floodcount += floodfill(h,w-1,basin_num);
	if (cur < getgrid(h,w+1)) floodcount += floodfill(h,w+1,basin_num);

	return floodcount;
}*/

int main() {
	ifstream in("watersheds.in");
	FILE* out = fopen("watersheds.out","w");
	in >> T;
	for (int t = 0; t < T; t++) {
		max_basin = 0;

		//cout << "----------- CASE " << t << endl;
		in >> H >> W;
		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				in >> grid[h][w];
				basin[h][w] = 0;
				cbasin[h][w] = '.';
			}
		}

		/*
		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				cout << grid[h][w] << " ";
			}
			cout << endl;
		}*/

		for (int i = 0; i < H*W; i++) {
			int min = SUPER;
			int minw = 0, minh = 0;

			for (int h = 0; h < H; h++) {
				for (int w = 0; w < W; w++) {
					if (grid[h][w] < min && !basin[h][w]) {
						min = grid[h][w];
						minh = h;
						minw = w;
					}
				}
			}
			get_basin_num(minh,minw);
		}

		char basin_let = 'a';

		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				if (cbasin[h][w] == '.') {
					cbasinfill(basin[h][w],basin_let++);
				}
			}
		}
			
		printf("Case #%d:\n",t+1);
		fprintf(out,"Case #%d:\n",t+1);
		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				if (w) fprintf(out," ");
				fprintf(out,"%c",cbasin[h][w]);
				cout << cbasin[h][w] << " ";
			}
			fprintf(out,"\n");
			cout << endl;
		}
	}


	return 0;
}
