#include <cmath>
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int MAXABS = 3001;

int N;
int L;

vector<int> xGrid[2*3001];
vector<int> yGrid[2*3001];

int grid[2*3001][2*3001];

int currX, currY, dir;

int main() {
	fstream in;
	fstream out;
	in.open("prob1.in", fstream::in);
	out.open("prob1.out",fstream::out);

	in >> N;
	for (int a = 0; a < N; a++) {
		in >> L;
		string dirs;
		char move;
		int num;
		currX = MAXABS;
		currY = MAXABS;
		dir = 0;
		for (int aa = 0; aa < 2*MAXABS; aa++) {
			xGrid[aa].clear();
			yGrid[aa].clear();
		}
		for (int b = 0; b < L; b++) {
			in >> dirs >> num;
			for (int c = 0; c < num; c++) {
				for (int d = 0; d < dirs.length(); d++) {
					move = dirs.at(d);
					if (move == 'L') {
						dir = (dir + 3) % 4;
					} else if (move == 'R') {
						dir = (dir + 1) % 4;
					} else if (move == 'F') {
						if (dir == 0) {
							xGrid[currY].push_back(currX);
							currY++;
						} else if (dir == 1) {
							yGrid[currX].push_back(currY);
							currX++;
						} else if (dir == 2) {
							xGrid[currY-1].push_back(currX);
							currY--;
						} else if (dir == 3) {
							yGrid[currX-1].push_back(currY);
							currX--;
						}
					}
				}
			}
		}
		for (int e = 0; e < 2*MAXABS; e++) {
			sort(xGrid[e].begin(),xGrid[e].end());
			sort(yGrid[e].begin(),yGrid[e].end());
		}

		for (int i = 0; i < 2*MAXABS; i++) {
			for (int j = 0; j < 2 *MAXABS; j++) {
				grid[i][j] = -1;
			}
		}

		int ans = 0;
		for (int x = 0; x < 2*MAXABS; x++) {
			for (int y = 0; y < xGrid[x].size(); y++) {
				if (y % 2 == 0 && y > 0) {
					for (int z = xGrid[x].at(y-1); z < xGrid[x].at(y); z++) {
						grid[z][x] = 1;
						ans++;
					}
				}
			}
		}
		for (int xx = 0; xx < 2*MAXABS; xx++) {
			for (int yy = 0; yy < yGrid[xx].size(); yy++) {
				if (yy % 2 == 0 && yy > 0) {
					for (int zz = yGrid[xx].at(yy-1); zz < yGrid[xx].at(yy); zz++) {
						if (grid[xx][zz] == -1) {
							ans++;
						}
						grid[xx][zz] = 1;
					}
				}
			}
		}

		out << "Case #" << a+1 << ": " << ans << endl;
	}
	
	in.close();
	out.close();
	return 0;
}