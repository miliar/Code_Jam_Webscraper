#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <map>

using namespace std;

void spike() {
	cout << endl;
	vector<string > tiles;
	int r,c; cin >> r >> c;
	
	for (int i = 0; i < r; i++) {
		string s;
		cin >> s;
		tiles.push_back(s);
	}

	bool possible = true;
	for (int y = 0; y < r - 1; y++)
		for (int x = 0; x < c - 1; x++ ) {
			if(tiles[y][x] == '#') {
				if( tiles[y+1][x] == '#' && tiles[y][x+1] == '#' && tiles[y+1][x+1] == '#') {
					tiles[y][x] = tiles[y+1][x+1] = '/';
					tiles[y+1][x] = tiles[y][x+1] = '\\';
				}	
				else
					possible = false;
			}
		}

	for (int y = 0; y < r; y++)
		for (int x = 0; x < c; x++ ) 
			if(tiles[y][x] == '#')
				possible = false;

	if(!possible) 
		cout << "Impossible" << endl;
	else
		for (int i = 0; i < r; i++)
			cout << tiles[i] << endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);

	int z;
	cin >> z;
	for (int i = 0; i < z; i++) {
		cout << "Case #" << i+1 << ": ";
		spike();
	}
}