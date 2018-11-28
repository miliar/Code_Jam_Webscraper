#include<iostream>
#include<fstream>
#include<vector>
#include<string>

using namespace std;

char who_won(vector<string> grid) {
	char toMatch;
	char drawOrIncomplete = 'D';
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if(grid[i][j] == '.') {
				drawOrIncomplete = 'I';
				break;
			}
			if(j == 0 || toMatch == 'T') {
				toMatch = grid[i][j];
			} else if(grid[i][j] != toMatch && grid[i][j] != 'T') {
				break;
			} else if(j == 3 && (grid[i][j] == toMatch || grid[i][j] == 'T')) {
				return toMatch;
			}
		}
	}
	for(int j = 0; j < 4; j++) {
		for(int i = 0; i < 4; i++) {
			if(grid[i][j] == '.') {
				drawOrIncomplete = 'I';
				break;
			}
			if(i == 0 || toMatch == 'T') {
				toMatch = grid[i][j];
			} else if(grid[i][j] != toMatch && grid[i][j] != 'T') {
				break;
			} else if(i == 3 && (grid[i][j] == toMatch || grid[i][j] == 'T')) {
				return toMatch;
			}
		}
	}
	int j = 0;
	for(int i = 0; i < 4 && j < 4; i++) {
		if(grid[i][j] == '.') {
			drawOrIncomplete = 'I';
			break;
		}
		if(j == 0 || toMatch == 'T') {
			toMatch = grid[i][j];
		} else if(grid[i][j] != toMatch && grid[i][j] != 'T') {
			break;
		} else if(j == 3 && (grid[i][j] == toMatch || grid[i][j] == 'T')) {
			return toMatch;
		}
		j++;
	}
	j = 3;
	for(int i = 0; i < 4 && j >= 0; i++) {
		if(grid[i][j] == '.') {
			drawOrIncomplete = 'I';
			break;
		}
		if(i == 0 || toMatch == 'T') {
			toMatch = grid[i][j];
		} else if(grid[i][j] != toMatch && grid[i][j] != 'T') {
			break;
		} else if(i == 3 && (grid[i][j] == toMatch || grid[i][j] == 'T')) {
			return toMatch;
		}
		j--;
	}
	return drawOrIncomplete;
}

int main(int argc, char* argv[]) {
	if(argc != 3) {
		cout << "Please provide the input name followed by the output name\n";
	}
	int cases;
	vector<char> results;
	ifstream file_in(argv[1]);
	ofstream file_out(argv[2]);
	file_in >> cases;
	for(int i = 0; i < cases; i++) {
		vector<string> grid;
		for(int j = 0; j < 4; j++) {
			string line;
			file_in >> line;
			grid.push_back(line);
		}
		file_in.get();
		results.push_back(who_won(grid));
	}
	for(int i = 0; i < cases; i++) {
		file_out << "Case #" << i + 1 << ": ";
		switch(results[i]) {
			case 'D':
				file_out << "Draw\n";
				break;
			case 'I':
				file_out << "Game has not completed\n";
				break;
			default:
				file_out << results[i] << " won\n";
				break;
		}
	}
	return 0;
}

