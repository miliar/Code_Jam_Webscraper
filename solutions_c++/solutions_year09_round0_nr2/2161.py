#include <iostream>
#include <vector>

using namespace std;

struct Cell {
	int altitude;
	char label;
	Cell* direction;
	vector<Cell*> children;
	bool isBasin;
};

void getLowestCell(Cell& self, vector<Cell*> neighbors) {
	Cell* lowestCell = &self;
	for (int i = 0; i < neighbors.size(); i++) {
		Cell* c = neighbors[i];
		if (c->altitude < lowestCell->altitude) {
			lowestCell = c;
		}
	}
	
	if (lowestCell == &self) {
		self.isBasin = true;
	} else {
		self.direction = lowestCell;
		lowestCell->children.push_back(&self);
	}
}

Cell* findBasin(Cell* cell) {
	while ( cell->isBasin == false ) {
		cell = cell->direction;
	}
	return cell;
}

void markLabelToRegion(Cell* cell, char label) {
	cell->label = label;
	for (int i = 0; i < cell->children.size(); i++) {
		markLabelToRegion( cell->children[i], label );
	}
}

int main() {
	int map_num;
	cin >> map_num;
	for (int map = 0; map < map_num; map++) {
		Cell cell[100][100];
		int H, W;
		cin >> H;
		cin >> W;
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				cin >> cell[i][j].altitude;
				cell[i][j].isBasin = false;
				cell[i][j].label = 0;
				cell[i][j].direction = &cell[i][j];
				cell[i][j].children.clear();
			}
		}

		

		// calculate direction
		
		// 4 corners
		{
			vector<Cell*> n;
			n.push_back(&cell[0][1]);
			n.push_back(&cell[1][0]);
			getLowestCell(cell[0][0], n);
		}
		{
			vector<Cell*> n;
			if (W > 1)
				n.push_back(&cell[0][W-2]);
			if (H > 1)
				n.push_back(&cell[1][W-1]);
			getLowestCell(cell[0][W-1], n);
		}
		{
			vector<Cell*> n;
			if (H > 1)
				n.push_back(&cell[H-2][0]);
			if (W > 1)
				n.push_back(&cell[H-1][1]);
			getLowestCell(cell[H-1][0], n);
		}
		{
			vector<Cell*> n;
			if (H > 1)
				n.push_back(&cell[H-2][W-1]);
			if (W > 1)
				n.push_back(&cell[H-1][W-2]);
			getLowestCell(cell[H-1][W-1], n);
		}

		// 4 edges
		for (int j = 1; j < W-1; j++) {
			vector<Cell*> n;
			n.push_back(&cell[0][j-1]);
			n.push_back(&cell[0][j+1]);
			if (H > 1)
				n.push_back(&cell[1][j]);
			getLowestCell(cell[0][j], n);
		}
		for (int j = 1; j < W-1; j++) {
			vector<Cell*> n;
			if (H > 1)
				n.push_back(&cell[H-2][j]);
			n.push_back(&cell[H-1][j-1]);
			n.push_back(&cell[H-1][j+1]);
			getLowestCell(cell[H-1][j], n);
		}
		for (int i = 1; i < H-1; i++) {
			vector<Cell*> n;
			n.push_back(&cell[i-1][0]);
			if (W > 1)
				n.push_back(&cell[i][1]);
			n.push_back(&cell[i+1][0]);
			getLowestCell(cell[i][0], n);
		}
		for (int i = 1; i < H-1; i++) {
			vector<Cell*> n;
			n.push_back(&cell[i-1][W-1]);
			if (W > 1)
				n.push_back(&cell[i][W-2]);
			n.push_back(&cell[i+1][W-1]);
			getLowestCell(cell[i][W-1], n);
		}
		
		// inside
		for (int i = 1; i < H-1; i++) {
			for (int j = 1; j < W-1; j++) {
				vector<Cell*> n;
				n.push_back(&cell[i-1][j]);
				n.push_back(&cell[i][j-1]);
				n.push_back(&cell[i][j+1]);
				n.push_back(&cell[i+1][j]);
				getLowestCell(cell[i][j], n);
			}
		}

		cout << "Case #" << map+1 << ":" << endl;
		char label = 'a';
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				Cell* thisCell = &cell[i][j];
				
				if (thisCell->label == 0) { // not label yet
					Cell* basin = findBasin(thisCell);
					markLabelToRegion(basin, label);
					label++;
				}
				
				cout << thisCell->label << " ";
			}
			cout << endl;
		}
	}
	return 0;
}
