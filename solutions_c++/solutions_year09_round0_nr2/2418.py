#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#define ARRAY_WIDTH 100
using namespace std;

struct node {
	int elevation;
	int letter;
	node *path;
};

int currentLetter;

void OpenFiles(ifstream &in, ofstream &out) {
	in.open("B-large.in");
	out.open("result.txt");
	
	if(in.fail() || out.fail())
		cout << "Failed to open input or output file." << endl;
}

void FillMap(node* map[][ARRAY_WIDTH], ifstream &in, int height, int width) {
	for (int i = 0; i < height; ++i) {
		for (int j = 0; j < width; ++j) {
			node *newNode = new node;
			in >> newNode->elevation;
			in.get();
			newNode->letter = 0;
			newNode->path = NULL; //path water travels
			map[i][j] = newNode;
		}
	}
}

inline void FindLowest(node* map[][ARRAY_WIDTH], int &lowest, node *&lowestPath, int pathY, int pathX) {
	lowest = map[pathY][pathX]->elevation;
	lowestPath = map[pathY][pathX];
}

int LabelNode(node* map[][ARRAY_WIDTH], int y, int x, int height, int width) {
	if (map[y][x]->letter != 0) return map[y][x]->letter;
	
	// find lowest neighbor
	int lowest = 10001;
	int pathX, pathY;
	node *lowestPath = NULL;
	
	// north
	if (y-1 >= 0) {
		if (map[y-1][x]->elevation < lowest) {
			pathY = y-1;
			pathX = x;
			FindLowest(map, lowest, lowestPath, pathY, pathX);
		}
	}
	// west
	if (x-1 >= 0) {
		if (map[y][x-1]->elevation < lowest) {
			pathY = y;
			pathX = x-1;
			FindLowest(map, lowest, lowestPath, pathY, pathX);
		}
	}
	// east
	if (x+1 < width) {
		if (map[y][x+1]->elevation < lowest) {
			pathY = y;
			pathX = x+1;
			FindLowest(map, lowest, lowestPath, pathY, pathX);
		}
	}
	// south
	if (y+1 < height) {
		if (map[y+1][x]->elevation < lowest) {
			pathY = y+1;
			pathX = x;
			FindLowest(map, lowest, lowestPath, pathY, pathX);
		}
	}
	
	int basinLetter;
	if (lowest < map[y][x]->elevation) {
		// not a basin
		map[y][x]->path = lowestPath;
		basinLetter = LabelNode(map, pathY, pathX, height, width);
	} else {
		// found a basin
		basinLetter = currentLetter++;
	}
	map[y][x]->letter = basinLetter;
	return basinLetter;
}

int main (int argc, char * const argv[]) {
	ifstream in;
	ofstream out;
	OpenFiles(in, out);
    
	int numMaps;
	in >> numMaps;
	
	for (int i = 0; i < numMaps; ++i) {
		currentLetter = 'a';
		int height, width;
		in >> height;
		in.get();
		in >> width;
		in.get();

		node* map[height][ARRAY_WIDTH];
		FillMap(map, in, height, width);
		
		// label all nodes with basin letters
		for (int y = 0; y < height; ++y) {
			for (int x = 0; x < width; ++x) {
				LabelNode(map, y, x, height, width);
			}
		}
		
		out << "Case #" << i+1 << ":" << endl;
		for (int y = 0; y < height; ++y) {
			for (int x = 0; x < width; ++x) {
				out << (char)(map[y][x]->letter);
				if (x != width-1) out << " ";
			}
			out << endl;
		}
	}
	
	return 0;
}
