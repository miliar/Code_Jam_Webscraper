#include <iostream>
#include <vector>
#include <map>

using std::ostream;
using std::string;
using std::vector;


class ElvMap {
	
	public:
		
		ElvMap(int rows, int cols);
		
		void printBasins();
		
		friend ostream& operator<<(ostream& os, const ElvMap& elvmap);
		
	private:
		
		class Coord {
			public:
				Coord(int r, int c) : row(r), col(c) {};
				int row;
				int col;
		};
		
		void findBasin(Coord cell);
		
		bool isSink(Coord cell) const;
		
		Coord drain(Coord cell) const;
		
		int r;
		int c;
		int basins;
		vector<vector<int> > m;
		vector<vector<char> > b;
		
		
};


int main()  {
	
	int t;
	std::cin >> t;
	for (int i = 0; i < t; i++) {
		int rows,cols;
		std::cin >> rows >> cols;
		ElvMap elvmap(rows, cols);
		std::cout << "Case #" << i+1 << ":" << std::endl;
		try {
			elvmap.printBasins();
		}
		catch (string& str) {
			std::cout << str << std::endl;
		}
	}		
		
	return 0;
}


ElvMap::ElvMap(int rows, int cols) : r(rows), c(cols), basins(0) {
	
	for (int i = 0; i < rows; i++) {
		vector<int> row;
		vector<char> basinsRow;
		for (int j = 0; j < cols; j++) {
			int cell;
			std::cin >> cell;
			row.push_back(cell);
			basinsRow.push_back(' ');		// unknown basin
		}
		m.push_back(row);
		b.push_back(basinsRow);
	}
}


void ElvMap::printBasins() {
	
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (b[i][j] == ' ') {		// unknown basin
				findBasin(Coord(i,j));
			}
			std::cout << b[i][j];
			if (j < c - 1) {
				std::cout << " ";
			}
		}
		std::cout << std::endl;
	}
}


void ElvMap::findBasin(Coord cell) {		// recursive function

//std::cout << "findBasin(" << cell.row << "," << cell.col << ")";
	
	if (b[cell.row][cell.col] == ' ') {
		if (isSink(cell)) {
			b[cell.row][cell.col] = 'a' + basins;
			basins++;
			if (basins > 26)
				throw string("too many sinks?");
		} else {
			findBasin(drain(cell));
			b[cell.row][cell.col] = b[drain(cell).row][drain(cell).col];
		}
	}
	
}


bool ElvMap::isSink(Coord cell) const {
	
	return ((drain(cell).row == cell.row) && (drain(cell).col == cell.col));
}


ElvMap::Coord ElvMap::drain(Coord cell) const {
	
	int row = cell.row;
	int col = cell.col;
	int alt = m[row][col];	// lowest alt. found
	Coord result(row, col);	// default is current cell
	if (row > 0) {	// drain north
		if (m[row-1][col] < alt) {
			alt = m[row-1][col];
			result = Coord(row-1, col);
		}
	}
	if (col > 0) {	// drain west
		if (m[row][col-1] < alt) {
			alt = m[row][col-1];
			result = Coord(row, col-1);
		}
	}
	if (col < c-1) {	// drain east
		if (m[row][col+1] < alt) {
			alt = m[row][col+1];
			result = Coord(row, col+1);
		}
	}
	if (row < r-1) {	// drain south
		if (m[row+1][col] < alt) {
			alt = m[row+1][col];
			result = Coord(row+1, col);
		}
	}
	return result;
	
}


ostream& operator<<(ostream& os, const ElvMap& elvmap) {
	
	for (int i = 0; i < elvmap.r; i++) {
		for (int j = 0; j < elvmap.c; j++)
			os << elvmap.m[i][j] << " ";
		os << std::endl;
	}
	
	return os;
}




