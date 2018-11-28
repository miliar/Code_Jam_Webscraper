#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

#define for0(i,n) for(int i = 0; i < (n); i ++)

int r, c;

string tile[60];

int main() {
	
	int kases; cin >> kases;
	
	for0(kase, kases) {
		cin >> r >> c;
		for0(i, r) cin >> tile[i];
		
		bool possible = true;
		for0(i, r) for0(j, c) {
			if (tile[i][j] == '#') {
				if (i == r-1 || j == c-1) {
					possible = false;
					break;
				} else if (tile[i+1][j] != '#' ||
					tile[i][j+1] != '#' ||
					tile[i+1][j+1] != '#') {
					possible = false;
					break;
				} else {
					tile[i][j] = '/';
					tile[i+1][j] = '\\';
					tile[i][j+1] = '\\';
					tile[i+1][j+1] = '/';
				}
					
			}
		}
		cout << "Case #" << (kase+1) << ":" << endl;
		if (!possible) {
			cout << "Impossible" << endl;
		} else {
			for0(i, r) cout << tile[i] << endl;
		}
	}
}