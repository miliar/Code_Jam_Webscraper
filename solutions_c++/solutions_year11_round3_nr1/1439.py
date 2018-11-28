#include<vector>
#include<iostream>
#include<fstream>
#include<stdio.h>

using namespace std;

bool replace(vector<vector<char>> &tiles)
{
	for(size_t i = 0; i < tiles.size(); i++){
		for(size_t j = 0; j < tiles[i].size(); j++){
			if(tiles[i][j] == '#'){
				tiles[i][j] = '/';
				if(j + 1 == tiles[i].size() || tiles[i][j + 1] != '#')
					return false;
				tiles[i][j + 1] = '\\';
				if(i + 1 == tiles.size() || tiles[i + 1][j] != '#')
					return false;
				tiles[i + 1][j] = '\\';
				if(i + 1 == tiles.size() || j == tiles[i].size() || tiles[i + 1][j + 1] != '#')
					return false;
				tiles[i + 1][j + 1] = '/';
			}
		}
	}
	return true;
}

int main(int argc, char *argv[])
{
	ifstream ifs(argv[1]);
	int T;
	ifs >> T;
	for(int x = 0; x < T; x++){
		size_t R, C;
		ifs >> R >> C;
		vector<vector<char>> tiles(R);
		for(size_t i = 0; i < R; i++){
			tiles[i].resize(C);
			for(size_t j = 0; j < C; j++)
				ifs >> tiles[i][j];
		}

		cout << "Case #" << x + 1 << ": " << endl;
		if(replace(tiles)){
			for(size_t i = 0; i < R; i++){
				for(size_t j = 0; j < C; j++)
					cout << tiles[i][j];
				cout << endl;
			}
		}
		else
			cout << "Impossible" << endl;
	}
	return 0;
}
