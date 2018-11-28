#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <cstring>
using namespace std;

int rows, cols;

bool solve(char grid[50][51], int remaining)
{

				if (remaining == 0) {
					for (int r = 0; r < rows; r++)
						cout << grid[r] << endl;
					return true;
				}

	for (int r = 0; r < rows-1; r++) {
		for (int c = 0; c < cols-1; c++) {
			if (grid[r][c] == '#' &&
			    grid[r+1][c] == '#' &&
				grid[r][c+1] == '#' &&
				grid[r+1][c+1] == '#') {
				//char newGrid[50][51];
				//memcpy(newGrid, grid, rows*(cols+1));
				//for (int i = 0; i < rows; i++)
				//	memcpy(newGrid[i], grid[i], cols+1);
				grid[r][c] = '/';
				grid[r+1][c] = '\\';
				grid[r][c+1] = '\\';
				grid[r+1][c+1] = '/';
				//bool result = solve(newGrid, remaining-4);
				//if (result)
				//	return true;
				remaining -=4;


				if (remaining == 0) {
					for (int r = 0; r < rows; r++)
						cout << grid[r] << endl;
				return true;
				}
			}
		}
	}

	return false;
}

int main()
{
	int c;
	cin >> c;
	for (int i = 0; i < c; i++) {
		char grid[50][51];
		int count = 0;
		cin >> rows >> cols;
		for (int j = 0; j < rows; j++) {
			string line;
			cin >> line;
			for (int k = 0; k < cols; k++) {
				grid[j][k] = line[k];
				if (grid[j][k] == '#')
					count++;
			}
			grid[j][cols] = '\0';
			//cout << grid[j] << endl;
		}
		cout << "Case #" << i+1 << ": " << endl;
		if (!solve(grid, count))
			cout << "Impossible" << endl;
	}
}
