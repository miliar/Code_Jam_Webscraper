#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define ll long long
#define pii pair<int,int>

ofstream fout ("QA.out");
ifstream fin ("QA.in");

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Working on Case #" << t << endl;
		bool d = true;
		bool o = false;
		bool x = false;
		int grid[4][4];
		for (int i = 0; i < 4; i++) {
			string row;
			fin >> row;
			bool ot = true;
			bool xt = true;
			for (int j = 0; j < 4; j++) {
				if (row[j] == 'T') {
					grid[i][j] = 0;
				}
				else if (row[j] == 'X') {
					grid[i][j] = 1;
					ot = false;
				}
				else if (row[j] == 'O') {
					grid[i][j] = 2;
					xt = false;
				}
				else {
					grid[i][j] = -1;
					d = false;
					ot = xt = false;
				}
			}
			if (ot) o = true;
			else if (xt) x = true;
		}
		for (int j = 0; j < 4; j++) {
			bool ot = true;
			bool xt = true;
			for (int i = 0; i < 4; i++) {
				if (grid[i][j] == 1) {
					ot = false;
				}
				else if (grid[i][j] == 2) {
					xt = false;
				}
				else if (grid[i][j] == -1) {
					ot = xt = false;
				}
			}
			if (ot) o = true;
			else if (xt) x = true;
		}
		bool ot1 = true,ot2 = true,xt1 = true,xt2 = true;
		for (int i = 0; i < 4; i++) {
			if (grid[i][i] == 1) {
				ot1 = false;
			}
			else if (grid[i][i] == 2) {
				xt1 = false;
			}
			else if (grid[i][i] == -1) {
				ot1 = xt1 = false;
			}
			if (grid[i][3-i] == 1) {
				ot2 = false;
			}
			else if (grid[i][3-i] == 2) {
				xt2 = false;
			}
			else if (grid[i][3-i] == -1) {
				ot2 = xt2 = false;
			}
		}
		if (ot1 || ot2) o = true;
		if (xt1 || xt2) x = true;
		if (o) fout << "Case #" << t << ": O won" << endl;
		else if (x) fout << "Case #" << t << ": X won" << endl;
		else if (d) fout << "Case #" << t << ": Draw" << endl;
		else fout << "Case #" << t << ": Game has not completed" << endl;
	}
    return 0;
}