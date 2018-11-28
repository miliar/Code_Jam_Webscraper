#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

char tile[60][60];

int solve(int row, int col) 
{
	for (int i = 0; i < row; ++i) {
		for (int j = 0; j < col; ++j) {
			if (tile[i][j] == '#') {
				if (++j >= col || tile[i][j] != '#') {
					return 0;
				}
				tile[i][j - 1] = '/';
				tile[i][j] = '\\';
			}
		}
	} // for (int i = 0; i < row; ++i)
	for (int j = 0; j < col; ++j) {
		for (int i = 0; i < row; ++i) {
			if (tile[i][j] == '/' || tile[i][j] == '\\') {
				if (++i >= row || (tile[i][j] != '/' && tile[i][j] != '\\')) {
					return 0;
				}
				else {
					tile[i][j] = (tile[i - 1][j] == '/' ?	'\\' : '/');
				}
			}
		}
	}
	return 1;
}

int main(int argc, char* argv[]) {
	int numOfCases;
	int curCase = 1;
	cin >> numOfCases;
	for (;curCase <= numOfCases; ++curCase) {
		int row, col;
		cin >>row >> col;
		for (int i = 0; i < row; ++i) {
			for (int j = 0; j < col; ++j) {
				cin >> tile[i][j];
			}
		} // for (int i = 0; i < row; ++i)
		int result = solve(row, col);
		if (!result) {
			cout << "Case #" <<curCase << ":\n" << "Impossible" <<endl;
		} else {
			cout << "Case #" <<curCase << ":" <<endl;
			for (int i = 0; i < row; ++i) {
				for (int j = 0; j < col; ++j) {
					cout <<tile[i][j];
				}
				cout <<endl;
			}
		}
	}
}