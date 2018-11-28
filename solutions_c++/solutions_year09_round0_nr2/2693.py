#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void) {

	int numMaps;
	cin >> numMaps;

	for (int map = 0; map < numMaps; map++) {
		int hmap[102][102];
		char labels[102][102];

		// Initiliase
		for (int x = 0; x <= 101; x++) {
			for (int y = 0; y <= 101; y++) {
				hmap[x][y] = 99999;
				labels[x][y] = '-';
			}
		}

		int W, H;
		cin >> H >> W;

		// Read in data
		for (int y = 1; y <= H; y++) {
			for (int x = 1; x <= W; x++) {
				cin >> hmap[x][y];
			}
		}

		// Water down the hill
		char nextLabel = 'a';
		for (int y = 1; y <= H; y++) {
			for (int x = 1; x <= W; x++) {
				int oldX = x, oldY = y;
				//cout << "Start of for x=" << x <<", y=" << y << endl;
				vector< pair<int,int> > fillBack;
				bool keepGoing = true;
				while (keepGoing) {
					//cout << "Start of While x=" << x <<", y=" << y << endl;
					int curH = hmap[x][y];
					int hN = hmap[x][y-1], hS = hmap[x][y+1],
						hE = hmap[x+1][y], hW = hmap[x-1][y];
					
					if (labels[x][y] == '-') {
						char bestDir = 'X'; int lowestAlt = 999888777, dx = 0, dy = 0;
						if (hS <= lowestAlt && hS < curH) {bestDir = 'S'; lowestAlt = hS; dx = 0; dy = +1;}
						if (hE <= lowestAlt && hE < curH) {bestDir = 'E'; lowestAlt = hE; dx = +1; dy = 0;}
						if (hW <= lowestAlt && hW < curH) {bestDir = 'W'; lowestAlt = hW; dx = -1; dy = 0;}
						if (hN <= lowestAlt && hN < curH) {bestDir = 'N'; lowestAlt = hN; dx = 0;  dy = -1;}

						// Check if its a sink
						if (bestDir == 'X') {
							labels[x][y] = nextLabel;
							for (int z = 0; z < fillBack.size(); z++)
								labels[fillBack[z].first][fillBack[z].second] = labels[x][y];
							keepGoing = false;
							nextLabel++;
						} else {
							// Add it to the list, and move
							pair<int,int> newP(x,y);
							x = x+dx;
							y = y+dy;
							fillBack.push_back(newP);
						}
					} else {
						for (int z = 0; z < fillBack.size(); z++)
							labels[fillBack[z].first][fillBack[z].second] = labels[x][y];
						keepGoing = false;
					}
				}
				x = oldX; y = oldY;
			}
		}



		/*char nextLabel = 'a';
		for (int y = 1; y <= H; y++) {
		for (int x = 1; x <= W; x++) {
		int curH = hmap[x][y];
		int hN = hmap[x][y-1], hS = hmap[x][y+1],
		hE = hmap[x+1][y], hW = hmap[x-1][y];
		// Check if sink
		if (hN >= curH && hS >= curH && hE >= curH && hW >= curH) {
		// Are we unlabelled?
		if (labels[x][y] == '-') {
		labels[x][y] = nextLabel; nextLabel++;
		}
		// Check which is smallest
		} else {
		char bestDir = 'S'; int lowestAlt = hS, dx = 0, dy = +1;
		if (hE <= lowestAlt) {bestDir = 'E'; lowestAlt = hE; dx = +1; dy = 0;}
		if (hW <= lowestAlt) {bestDir = 'W'; lowestAlt = hW; dx = -1; dy = 0;}
		if (hN <= lowestAlt) {bestDir = 'N'; lowestAlt = hN; dx = 0;  dy = -1;}

		// Is the target labelled already?
		if (labels[x+dx][y+dy] != '-') {
		// Take its label
		labels[x][y] = labels[x+dx][y+dy];
		// Else if its not labelled...
		} else {
		// Then is the current point labelled
		if (labels[x][y] == '-') {
		labels[x][y] = nextLabel;
		labels[x+dx][y+dy] = nextLabel;
		nextLabel++;
		} else {
		// We've already been labelled, but the neighbour hasn't
		labels[x+dx][y+dy] = labels[x][y];
		}
		}
		}
		}
		}*/

		// Output results
		cout << "Case #" << (map+1) << ":" << endl;
		for (int y = 1; y <= H; y++) {
			for (int x = 1; x < W; x++) {
				cout << labels[x][y] << " ";
			}
			cout << labels[W][y] << endl;
		}

	}

}
