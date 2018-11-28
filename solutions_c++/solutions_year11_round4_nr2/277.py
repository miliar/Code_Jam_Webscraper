									/* in the name of Allah */
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <cstdio>
#include <cmath>
#include <map>

using namespace std;

ifstream fin("B_Spinning Blade.in");
ofstream fout("B_Spinning Blade.out");

#define cin fin
#define cout fout

int r, c, d;
char mat[110][110];

bool isposs(int x, int y, int k){
	return x + k - 1 < r && y + k - 1 < c;
}

int main(){
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> r >> c >> d;
		for(int i = 0; i < r; i++)
			for(int j = 0; j < c; j++)
				cin >> mat[i][j];
		int mx = -1;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				for(int k = 3; isposs(i, j, k); k++){
					int dx = 0, dy = 0;
					for(int x = i; x < i + k; x++){
						for(int y = j; y < j + k; y++){
							if((x == i || x == i + k - 1) && (y == j || y == j + k - 1))
								continue;
							dx += (2 * (x - i) - (k - 1)) * (mat[x][y] - '0');
							dy += (2 * (y - j) - (k - 1)) * (mat[x][y] - '0');
						}
					}
					if(dx == 0 && dy == 0){
						mx = max(mx, k);
						//cout << i << ' ' << j << ' ' << k << endl;
					}
				}
			}
		}
		cout << "Case #" << ++test << ": ";
		if(mx == -1)
			cout << "IMPOSSIBLE" << endl;
		else cout << mx << endl;
	}
	return 0;
}
	
