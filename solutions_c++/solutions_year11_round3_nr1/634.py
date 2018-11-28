#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

#define REP(i,a,b) for(int i=a;i<=b;i++)

int solve(int no)
{
	int R, C;
	cin >> R >> C;
	
	char tiles[60][60];
	for(int i=0;i<R;i++) {
		cin >> tiles[i];
	}
	for(int i=0;i<C;i++) {
		tiles[R][i] = '\0';
	}
	
	for(int y=0;y<R;y++) {
		for(int x=0;x<C;x++) {
			if(tiles[y][x]!='#') continue;
			if(tiles[y+1][x]!='#' || tiles[y][x+1]!='#' || tiles[y+1][x+1]!='#') {
				cout << "Case #" << no << ":" << endl << "Impossible" << endl;
				return 0;
			}
			tiles[y][x] = '/'; tiles[y][x+1] = '\\';
			tiles[y+1][x] = '\\'; tiles[y+1][x+1] = '/';
		}
	}
	cout << "Case #" << no << ":" << endl;
	for(int i=0;i<R;i++) {
		cout << tiles[i] << endl;
	}
}

int main()
{
	int T;
	cin >> T;
	for(int no=1;no<=T;no++) {
		solve(no);
	}
	return 0;
}
