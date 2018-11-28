#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct Entry {
	int alt;
	bool is_basin;
	char basin_id;
};

void get_basins(vector<vector<Entry> >& table);
char get_answer(vector<vector<Entry> >& table, int r, int c, char& basin_id);

int main() {
	int T;
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		// read in the inputs
		int H, W;
		cin >> H >> W;
		vector<vector<Entry> > table;
		struct Entry e;
		for (int i = 0; i < H; i++) {
			vector<Entry> row;
			for (int j = 0; j < W; j++) {
				cin >> e.alt;
				row.push_back(e);
			}
			table.push_back(row);
		}
		// get the answer
		get_basins(table);
		char basin_id = 'a';
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				char answer = get_answer(table, i, j, basin_id);
				if (answer == '1') {
					basin_id++;
				}
			}
		}
		// print out answer
		cout << "Case #" << test_case << ":" << endl;
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W - 1; j++)
				cout << table[i][j].basin_id << " ";
			cout << table[i][W - 1].basin_id << endl;
		}
	}
}

void get_basins(vector<vector<Entry> >& table) {
	for (int r = 0; r < table.size(); r++) {
		for (int c = 0; c < table[r].size(); c++) {
			table[r][c].basin_id = '0';
			if ((r > 0 && table[r - 1][c].alt < table[r][c].alt)
				|| (r < table.size() - 1 && table[r + 1][c].alt < table[r][c].alt)
				|| (c > 0 && table[r][c - 1].alt < table[r][c].alt)
				|| (c < table[r].size() - 1 && table[r][c + 1].alt < table[r][c].alt))
				table[r][c].is_basin = false;
			else
				table[r][c].is_basin = true;
		}
	}
}

char get_answer(vector<vector<Entry> >& table, int r, int c, char& basin_id) {
//cout << "recursed on: " << r << ", " << c << endl;
	// base case
	if (table[r][c].basin_id != '0') {
//cout << "hi" << endl;
		return table[r][c].basin_id;
	}
	if (table[r][c].is_basin) {
		table[r][c].basin_id = basin_id;
		basin_id = basin_id + 1;
//cout << "the basin id = " << basin_id << endl;
		return basin_id - 1;
	}
	// recursive step
//cout << "recursive step" << endl;
	table[r][c].basin_id = '1';
	int min = table[r][c].alt + 10000;
	int r_next, c_next;
	if (r > 0 && table[r - 1][c].alt < min) {
		r_next = r - 1;
		c_next = c;
		min = table[r - 1][c].alt;
	}
	if (c > 0 && table[r][c - 1].alt < min) {
		r_next = r;
		c_next = c - 1;
		min = table[r][c - 1].alt;
	}
	if (c < table[r].size() - 1 && table[r][c + 1].alt < min) {
		r_next = r;
		c_next = c + 1;
		min = table[r][c + 1].alt;
	}
	if (r < table.size() - 1 && table[r + 1][c].alt < min) {
		r_next = r + 1;
		c_next = c;
		min = table[r + 1][c].alt;
	}
	table[r][c].basin_id = get_answer(table, r_next, c_next, basin_id);
	if (table[r][c].basin_id == '1') {
		table[r][c].basin_id = basin_id;
		table[r_next][c_next].basin_id = basin_id;
		return '1';
	}
	return table[r][c].basin_id;
}

