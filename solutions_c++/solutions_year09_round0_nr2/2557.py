//#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

typedef vector<string> StringVector;

struct drainpipe {
	char* drainletter;
	drainpipe* dlink;
	drainpipe() : drainletter(NULL), dlink(NULL) { }
	drainpipe(char* let, drainpipe* lnk) : drainletter(let), dlink(lnk) { }
};

int map[100][100];
drainpipe drainlink[100][100];
int T, H, W;
drainpipe theDrain;
char virtualDrains[26];

char* trace(drainpipe* bob) {
	if (bob->dlink == &theDrain) {
		return bob->drainletter;
	} else {
		bob->drainletter = trace(bob->dlink);
		bob->dlink = &theDrain;
		return bob->drainletter;
	}
}

int main() {
	ifstream fin ("B-large.in");
	ofstream fout ("B-large.out");

	fin >> T;

	for (int mapnum = 1; mapnum <= T; mapnum++) {
		
		
		fin >> H;
		fin >> W;
		//cout << H << " " << W << endl;
	
		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++) {
				fin >> map[x][y];
				//cout << map[x][y] << " ";
			}
			//cout << endl;
		}
//if (mapnum > T/2) {

		fout << "Case #" << mapnum << ": " << endl;

		int nextDrainLetter = 97;
		int nextDrainID = 0;
		for (int i = 0; i < 26; i++)
			virtualDrains[i] = '+';

		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++) {
				int lowx, lowy;
				int best = 10001;
				if (map[x][y-1] < best && y != 0) { lowx = x; lowy = y-1; best = map[x][y-1]; }
				if (map[x-1][y] < best && x != 0) { lowx = x-1; lowy = y; best = map[x-1][y]; }
				if (map[x+1][y] < best && x != W-1) { lowx = x+1; lowy = y; best = map[x+1][y]; }
				if (map[x][y+1] < best && y != H-1) { lowx = x; lowy = y+1; best = map[x][y+1]; }
				if (best < map[x][y]) {
					drainlink[x][y] = drainpipe(NULL,&drainlink[lowx][lowy]);
				} else {
					drainlink[x][y] = drainpipe(&virtualDrains[nextDrainID], &theDrain);
					nextDrainID++;
				}				
			}
		}

		
		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++) {
				char* tmp = trace(&drainlink[x][y]);
				if (*tmp == '+') {
					*tmp = (char)nextDrainLetter;
					nextDrainLetter++;
				}
				fout << *tmp << " ";
			}
			fout << endl;
		}
//}
	}
	//char bah;
	//cin >> bah;
}