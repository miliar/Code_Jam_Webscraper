#include<iostream>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<vector>
#include<string>
#include<math.h>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; cin>>T;
	for (int t=1; t<=T; t++) {
		int R,C; cin>>R>>C;
		char grid[R][C];
		for (int i=0; i<R; i++) for(int j=0; j<C; j++) cin>>grid[i][j];

		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				if(0<=i && i+1<R && 0<=j && j+1<C) {
					bool flag=true;
					for (int ii=0; ii<2; ii++) {
						for (int jj=0; jj<2; jj++) {
							if(grid[i+ii][j+jj]!='#') { flag=false; break; }
						}
					}
	
					if(flag) {
						grid[i][j]='/';
						grid[i][j+1]= '\\' ;
						grid[i+1][j]='\\';
						grid[i+1][j+1]='/';
					}
				}
			}
		}

		bool OK=true;
		for (int i=0; i<R; i++) for(int j=0; j<C; j++) if(grid[i][j]=='#') { OK=false; break;}

		cout << "Case #" << t << ":" << endl;
		if(OK) {
			for (int i=0; i<R; i++) {
				for (int j=0; j<C; j++) cout << grid[i][j];
				cout << endl;
			}
		} else cout << "Impossible" << endl;
	}

	return 0;
}
