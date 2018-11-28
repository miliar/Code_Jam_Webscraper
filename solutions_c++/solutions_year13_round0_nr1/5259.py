#include <iostream>
#include <set>
#include <string>
#include <cstdio>
#define ROW 10
#define COL 100
#define DIAG1 -1
#define DIAG2 -2
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t=1; t <= T; t++) {

		set<int> x_wins, o_wins;

		for (int i=0; i<4; i++) {
			x_wins.insert(ROW+i);
			x_wins.insert(COL+i);
			o_wins.insert(ROW+i);
			o_wins.insert(COL+i);
		}
		x_wins.insert(DIAG1);
		x_wins.insert(DIAG2);
		o_wins.insert(DIAG1);
		o_wins.insert(DIAG2);

		bool completed = true;
		for (int i=0; i<4; i++) {
			string row;
			cin >> row;

			for (int j=0; j<4; j++) {
				
				if (row[j] == 'X') {
					o_wins.erase(ROW+i);
					o_wins.erase(COL+j);
					if (i==j) 
						o_wins.erase(DIAG1);

					if ((i+j) == 3)
						o_wins.erase(DIAG2);
				} else if (row[j] == 'O') {
					x_wins.erase(ROW+i);
					x_wins.erase(COL+j);
					if (i==j) 
						x_wins.erase(DIAG1);

					if ((i+j) == 3)
						x_wins.erase(DIAG2);
				} else if (row[j] == '.') {
					x_wins.erase(ROW+i);
					x_wins.erase(COL+j);
					o_wins.erase(ROW+i);
					o_wins.erase(COL+j);
					completed = false;
					if (i==j) {
						x_wins.erase(DIAG1);
						o_wins.erase(DIAG1);
					}

					if ((i+j) == 3) {
						o_wins.erase(DIAG2);
						x_wins.erase(DIAG2);
					}
				}
			}
		}
		if (!o_wins.empty()) {
			printf("Case #%d: O won\n",t);
		} else if (!x_wins.empty()) {
			printf("Case #%d: X won\n",t);
		} else if (completed) {
			printf("Case #%d: Draw\n",t);
		} else {
			printf("Case #%d: Game has not completed\n",t);
		}
	}
}