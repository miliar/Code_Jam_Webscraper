#include <stdio.h>
#include <vector>
#include <cassert>

using namespace std;

struct Cell {
	vector<Cell *> neighbours;
	int height;
	char group;
	Cell() {
		height = -1;
		group = ' ';
	}
};
int H, W;
Cell cells[150][150];

void ffill(Cell *cell, char label) {
	if (cell->group != ' ') {
		assert(cell->group == label);
	} else {
		cell->group = label;
		for (vector<Cell *>::iterator it = cell->neighbours.begin(); it != cell->neighbours.end(); ++it) {
			ffill(*it, label);
		}
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d %d", &H, &W);
		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				Cell c;
				scanf("%d", &c.height);
				cells[h][w] = c;
			}
		}
		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				// find the neighbour
				int min = 1000000;
				Cell *minCell = NULL;
				if (h > 0 && cells[h-1][w].height < min &&  cells[h-1][w].height < cells[h][w].height) {
					min = cells[h-1][w].height;
					minCell = &cells[h-1][w];
				}
				if (w > 0 && cells[h][w-1].height < min &&  cells[h][w-1].height < cells[h][w].height) {
					min = cells[h][w-1].height;
					minCell = &cells[h][w-1];
				}
				if (w < W - 1 && cells[h][w+1].height < min &&  cells[h][w+1].height < cells[h][w].height) {
					min = cells[h][w+1].height;
					minCell = &cells[h][w+1];
				}
				if (h < H - 1 && cells[h+1][w].height < min &&  cells[h+1][w].height < cells[h][w].height) {
					min = cells[h+1][w].height;
					minCell = &cells[h+1][w];
				}
				if (minCell != NULL) {
					cells[h][w].neighbours.push_back(minCell);
					minCell->neighbours.push_back(&cells[h][w]);
				}
			}
		}
		char nextLabel = 'a';
		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				// flood fill
				if (cells[h][w].group == ' ') { // not done yet
					ffill(&cells[h][w], nextLabel);
					nextLabel++;
				}
			}
		}
		printf("Case #%d:\n", t + 1);
		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				if (w > 0) printf(" ");
				printf("%c", cells[h][w].group);
			}
			printf("\n");
		}
	}
	return 0;
}