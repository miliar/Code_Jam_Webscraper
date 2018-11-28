/*
 * main.cpp
 *
 *  Created on: 7 avr. 2013
 *      Author: Khabat95
 */


#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cassert>
#include <complex>

using namespace std;

void algo() {
	char board[4][4];

	for(int i=0; i<4; ++i) {
		for(int j=0; j<4; ++j)
			cin >> board[i][j];
	}


	bool x = false;
	bool o = false;
	bool empty_case = false;
	int x_lines[4] = {0, 0, 0, 0};
	int x_columns[4] = {0, 0, 0, 0};
	int x_diags[2] = {0, 0};
	int o_lines[4] = {0, 0, 0, 0};
	int o_columns[4] = {0, 0, 0, 0};
	int o_diags[2] = {0, 0};
	for(int i=0; i<4; ++i) {
		for(int j=0; j<4; ++j) {
			if(board[i][j] == '.') {
				empty_case = true;
			}
			else if(board[i][j] == 'X') {
				x_lines[i]++;
				x_columns[j]++;
				if(i == j)
					x_diags[0]++;
				if(i+j == 4)
					x_diags[1]++;
			}
			else if(board[i][j] == 'O') {
				o_lines[i]++;
				o_columns[j]++;
				if(i == j)
					o_diags[0]++;
				if(i+j == 3)
					o_diags[1]++;
			}
			else if(board[i][j] == 'T') {
				x_lines[i]++;
				x_columns[j]++;
				o_lines[i]++;
				o_columns[j]++;
				if(i == j) {
					x_diags[0]++;
					o_diags[0]++;
				}
				if(i+j == 3) {
					x_diags[1]++;
					o_diags[1]++;
				}
			}

			if(x_columns[j] == 4) {
				x = true;
				break;
			}
			if(o_columns[j] == 4) {
				o = true;
				break;
			}
		}

		if(x_lines[i] == 4) {
			x = true;
			break;
		}
		if(o_lines[i] == 4) {
			o = true;
			break;
		}
		if(x_diags[0] == 4) {
			x = true;
			break;
		}
		if(x_diags[1] == 4) {
			x = true;
			break;
		}
		if(o_diags[0] == 4) {
			o = true;
			break;
		}
		if(o_diags[1] == 4) {
			o = true;
			break;
		}
	}

	if(x)
		cout << "X won" << endl;
	else if(o)
		cout << "O won" << endl;
	else if(empty_case)
		cout << "Game has not completed" << endl;
	else
		cout << "Draw" << endl;
}

int main() {
	int n_cases;
	cin >> n_cases;

	for(int i=0; i<n_cases; ++i) {
		cout << "Case #" << i+1 << ": ";
		algo();
	}
}

