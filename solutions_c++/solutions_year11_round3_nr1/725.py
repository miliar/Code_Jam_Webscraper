#include <iostream>
#include <array>
#include <vector>
#include <cassert>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <iomanip>
#include <list>

using namespace std;

char table[50][50];

bool solve(int R,int C) {
	for (int i=0;i < R;++i) {
		for (int j=0;j < C;++j) {
			if (table[i][j] == '#') {
				if (i == R-1 || j == C-1) return false;
				if (table[i][j+1] != '#' ||
					table[i+1][j] != '#' ||
					table[i+1][j+1] != '#') return false;
				table[i][j] = '/';
				table[i][j+1] = '\\';
				table[i+1][j] = '\\';
				table[i+1][j+1] = '/';
			}
		}
	}
	return true;
}

int main(int argc, char **argv) {
	cout << fixed << setprecision(12);
	int T;
	cin >> T;

	for(int i=0;i < T;++i) {
		int R,C;
		cin >> R >> C;
		
		memset(table,0,sizeof(table));
		
		for (int j=0;j < R;++j) {
			cin >> table[j];
		}
		
		bool ans = solve(R,C);
		cout << "Case #" << i+1 << ": " << endl;
		
		if (!ans) cout << "Impossible" << endl;
		else {
			for (int j=0;j < R;++j) {
				for (int k=0;k < C;++k)
					cout <<table[j][k];
				cout << endl;
			}
		}
	}
	
    return 0;
}
