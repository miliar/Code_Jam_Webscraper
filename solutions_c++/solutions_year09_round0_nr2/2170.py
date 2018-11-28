#include <fstream>
#include <iostream>
#include <strstream>
#include <string>
#include <vector>

using namespace std;

void eol(istream &is) {
	string str;
	getline(is, str);
}

template <typename T>
T GetOneInALine(istream &inStream) {
	T toReturn;
	inStream >> toReturn;
	eol(inStream);
	return toReturn;
}

template <typename T>
vector<T> GetAllInALine(istream &inStream) {
	string line;
	getline(inStream, line);
	istrstream lineStream(line.c_str());
	vector<T> toReturn;
	T toAdd;
	while (!lineStream.eof()) {
		lineStream >> toAdd;
		toReturn.push_back(toAdd);
	}
	return toReturn;
}

struct Map {
	int h, w;
	int *map;
	int *Coord(int row, int col) {
		if (row < 0 || col < 0)
			return NULL;
		return &map[row*w+col];
	}
	char *basin;
	char *BasinCoord(int row, int col) {
		return &basin[row*w+col];
	}
};

char ProcessCoord(Map *map, int row, int col, char *lastColor) {
	if (*map->BasinCoord(row, col))
		return *map->BasinCoord(row,col);
	int rowS=-1, colS=-1;
	int altToBeat=100000;
	// North
	if (row > 0 && *map->Coord(row-1, col) < altToBeat) {
		altToBeat = *map->Coord(row-1, col);
		rowS = row-1;
		colS = col;
	}
	// West
	if (col > 0 && *map->Coord(row, col-1) < altToBeat) {
		altToBeat = *map->Coord(row, col-1);
		rowS = row;
		colS = col-1;
	}
	// East
	if (col < map->w-1 && *map->Coord(row, col+1) < altToBeat) {
		altToBeat = *map->Coord(row, col+1);
		rowS = row;
		colS = col+1;
	}
	// South
	if (row < map->h-1 && *map->Coord(row+1, col) < altToBeat) {
		altToBeat = *map->Coord(row+1, col);
		rowS = row+1;
		colS = col;
	}
	if (altToBeat < *map->Coord(row, col))
		*map->BasinCoord(row,col) = ProcessCoord(map, rowS, colS, lastColor);
	else
		*map->BasinCoord(row,col) = ++*lastColor;
	return *map->BasinCoord(row,col);
}

void ProcessMap(Map *map) {
	map->basin = (char*)malloc(map->h * map->w * sizeof(char));
	int i,j;
	for (i=0; i<map->h; ++i) 
		for (j=0; j<map->w; ++j)
			*map->BasinCoord(i,j) = 0;
	char lastColor = 0;
	for (i=0; i<map->h; ++i) 
		for (j=0; j<map->w; ++j)
			*map->BasinCoord(i,j) = ProcessCoord(map, i, j, &lastColor);
	for (i=0; i<map->h; ++i) {
		for (j=0; j<map->w; ++j) {
			char c = 'a' - 1 + (*map->BasinCoord(i,j));
			cout << c << " ";
		}
		cout << "\n";
	}
	free(map->basin);
	return;
}

int Run(istream &inStream) {
	int T;
	inStream >> T;
	eol(inStream);
	Map map;
	for (int i=0; i<T; ++i) {
		inStream >> map.h >> map.w;
		eol(inStream);
		map.map = (int*)malloc(map.h * map.w * sizeof(int));
		for (int j=0; j<map.h; ++j) {
			for (int k=0; k<map.w; ++k)
				inStream >> *map.Coord(j,k);
			eol(inStream);
		}
		cout << "Case #" << i+1 << ":\n";
		ProcessMap(&map);
		free(map.map);
	}
	return 0;
}

int main(int argc, char* argv[])
{
	if (argc < 2)
		return Run(cin);
	else {
		ifstream inStream(argv[1]);
		return Run(inStream);
	}
}
