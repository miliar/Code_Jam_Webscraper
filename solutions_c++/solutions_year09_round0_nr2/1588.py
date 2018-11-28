// watersheds.cpp --  Thu Sep 03 2009
// http://code.google.com/codejam/contest/dashboard?c=90101#s=p1
#include <stdio.h>
#include <assert.h>
#include <memory.h>
#include <algorithm>

#define MAX_DIM 100
#define MAX_BASINS 26

int alt[MAX_DIM][MAX_DIM];
int basin_id[MAX_DIM][MAX_DIM];
char id_to_name[MAX_BASINS+1];

struct Node {
	int r, c;
	int h;
};

Node points[MAX_DIM*MAX_DIM];

bool operator<(const Node &lhs, const Node &rhs) {
	return lhs.h < rhs.h;
}

int main(int argc, char *argv[]) {
	int nt;
	scanf(" %d", &nt);
	for(int nti = 0; nti < nt; ++nti) {
		// Get Input
		int rows, cols;
		scanf(" %d %d", &rows, &cols);
		for(int r = 0, q = 0; r < rows; ++r) {
			for(int c = 0; c < cols; ++c, ++q) {
				scanf(" %d", &alt[r][c]);
				points[q].r = r;
				points[q].c = c;
				points[q].h = alt[r][c];
			}
		}

		// Calc
		memset(basin_id, 0, sizeof(basin_id));
		memset(id_to_name, 0, sizeof(id_to_name));
		int num_points = rows*cols;
		std::sort(points, points+num_points);
		int last_id = 0;
		for(int p = 0; p < num_points; ++p) {
			bool found = false;
			int r = points[p].r, c = points[p].c, h = points[p].h;
			int low = h, bid = 0;
			// North, West, East, South.
			if(r > 0 && alt[r-1][c] < low) low = alt[r-1][c], found = true, bid = basin_id[r-1][c];
			if(c > 0 && alt[r][c-1] < low) low = alt[r][c-1], found = true, bid = basin_id[r][c-1];
			if(c+1 < cols && alt[r][c+1] < low) low = alt[r][c+1], found = true, bid = basin_id[r][c+1];
			if(r+1 < rows && alt[r+1][c] < low) low = alt[r+1][c], found = true, bid = basin_id[r+1][c];
			basin_id[r][c] = found ? bid : ++last_id;
		}
		assert(last_id <= MAX_BASINS);

		// Output
		printf("Case #%d:\n", nti+1);
		char last_char = 'a'-1;
		int ccc = cols-1;
		for(int r = 0; r < rows; ++r) {
			for(int c = 0; c < cols; ++c) {
				if(!id_to_name[basin_id[r][c]]) id_to_name[basin_id[r][c]] = ++last_char;
				putchar(id_to_name[basin_id[r][c]]);
				putchar(c!=ccc ? ' ' : '\n');
			}
		}
	}
	return 0;
}

