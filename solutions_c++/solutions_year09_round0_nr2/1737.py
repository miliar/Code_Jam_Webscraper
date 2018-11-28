#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <climits>
using namespace std;

struct cell {
	int elevation;
	int basinNumber;
	bool isSink;
};

static vector<char> sinks;
static vector<vector<cell> > EleMap;

int height(int row, int col) {
	if(row < 0 || col < 0 || row >= EleMap.size() || col >= EleMap[row].size())
		return INT_MAX;

	return EleMap[row][col].elevation;
}

bool findLowest(int & row, int & col) {
	int north = height(row - 1, col);
	int west = height(row, col - 1);
	int east = height(row, col + 1);
	int south = height(row + 1, col);
	
	int here = height(row, col);
	int lowest = here;
	
	if(north < lowest) {
		lowest = north;
	}
	if(west < lowest) {
		lowest = west;
	}	
	if(east < lowest) {
		lowest = east;
	}
	if(south < lowest) {
		lowest = south;
	}
	
	if(lowest == here) {
		return true;
	}
	if(lowest == north) {
		row--;
		return false;
	}
	if(lowest == west) {
		col--;
		return false;
	}
	if(lowest == east) {
		col++;
		return false;
	}
	row++;
	return false;
}

int findBasin(int lineNum, int cellNum) {
	cell & currCell = EleMap[lineNum][cellNum];
	
	if(currCell.basinNumber >= 0)
		return currCell.basinNumber;
	
	if(findLowest(lineNum, cellNum)) {
		currCell.isSink = true;
		currCell.basinNumber = sinks.size();
		sinks.push_back('0');
		return currCell.basinNumber;
	}
	
	currCell.basinNumber = findBasin(lineNum, cellNum);
	
	return currCell.basinNumber;
}

int main (int argc, char * const argv[]) {
    cout << "Input file name: ";
	string filename;
	getline(cin, filename);
	
	cout << "Output file name: ";
	string outFileName;
	getline(cin, outFileName);
	
	ifstream in;
	in.open(filename.c_str());
	
	if(in.fail()) {
		cout << "File not found" << endl;
		exit(1);
	}
	
	ofstream out;
	out.open(outFileName.c_str());
	
	string params;
	getline(in, params);
	stringstream paramsStream;
	paramsStream << params;
	
	int T;
	
	paramsStream >> T;
	
	for(int mapNum = 0; mapNum < T; mapNum++) {
		out << "Case #" << mapNum + 1 << ":" << endl;
		string mapsize;
		getline(in, mapsize);
		stringstream mapSizeStream;
		mapSizeStream << mapsize;
		
		int H;
		int W;
		
		mapSizeStream >> H >> W;
		EleMap.clear();
		for(int lineNum = 0; lineNum < H; lineNum++) {
			string line;
			getline(in, line);
			stringstream lineStream;
			lineStream << line;
			vector<cell> lineVec;
			EleMap.push_back(lineVec);
			vector<cell> & lineVRef = EleMap[lineNum];
			for(int cellNum = 0; cellNum < W; cellNum++) {
				cell newCell;
				newCell.basinNumber = -1;
				lineStream >> newCell.elevation;
				lineVRef.push_back(newCell);
			}
		}
		
		for(int lineNum = 0; lineNum < H; lineNum++) {
			for(int cellNum = 0; cellNum < W; cellNum++) {
				findBasin(lineNum, cellNum);
			}
		}
		
		char sinkLetter = 'a';
		for(int lineNum = 0; lineNum < H; lineNum++) {
			for(int cellNum = 0; cellNum < W; cellNum++) {
				if(sinks[EleMap[lineNum][cellNum].basinNumber] == '0')
					sinks[EleMap[lineNum][cellNum].basinNumber] = sinkLetter++;
			}
		}
		
		for(int lineNum = 0; lineNum < H; lineNum++, out << endl) {
			for(int cellNum = 0; cellNum < W; cellNum++, out << ' ') {
				out << sinks[EleMap[lineNum][cellNum].basinNumber];
			}
		}
		
	}
	string dummy;
	getline(cin, dummy);
    return 0;
}
