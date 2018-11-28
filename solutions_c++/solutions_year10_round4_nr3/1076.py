#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

typedef vector<vector<char> > cell_t;

class Bacteria {
public:
	int solve(cell_t& cell) {
		int ans;
		cell_t copy_cell(cell);
		bool has_bacteria = true;
		int cnt = 0;
		while (has_bacteria) {
			has_bacteria = false;
			for (int i = 1; i < cell.size() - 1; i++) {
				for (int j = 1; j < cell[i].size() - 1; j++) {
					if (!has_bacteria && cell[i][j] == 1) has_bacteria = true;
					if (cell[i-1][j] == 1 && cell[i][j-1] == 1)
						copy_cell[i][j] = 1;
					if (cell[i-1][j] == 0 && cell[i][j-1] == 0)
						copy_cell[i][j] = 0;
				}
			}
			cell = copy_cell;
			cnt++;
//			cerr << cnt << endl; /////
		}
		return cnt - 1;
	}
};

int main()
{
//	fstream fs("test.in", ios_base::in);
	fstream fs("C-small-attempt1.in", ios_base::in);
	string line;
	stringstream ss;

	Bacteria bac;

	getline(fs, line);
	ss.str(line);
	int C, R, X1, Y1, X2, Y2;
	ss >> C;
	ss.clear();  ss.str("");
	int cnt = 0;
	for (int i = 0; i < C; i++) {
		cell_t cell(500, vector<char>(500, 0));
		getline(fs, line);
		ss.str(line);
		ss >> R;
		ss.clear();  ss.str("");
		for (int j = 0; j < R; j++) {
			getline(fs, line);
			ss.str(line);
			ss >> X1 >> Y1 >> X2 >> Y2;
			for (int x = X1; x <= X2; x++)
				for (int y = Y1; y <= Y2; y++)
					cell[x][y] = 1;
			ss.clear();  ss.str("");
		}
		cout << "Case #" << ++cnt << ": " << bac.solve(cell) << endl;
	}

	return 0;
}
