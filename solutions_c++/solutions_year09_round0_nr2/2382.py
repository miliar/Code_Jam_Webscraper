//============================================================================
// Name        : watersheds.cpp
// Author      : Akshay Singh
// Version     :
// Copyright   : 
// Description : Hello World in C, Ansi-style
//============================================================================

#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

short altitude[100][100];
char map[100][100];
int h = 0, w = 0;
int direction[][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };
char curr = '\0';

char assign(int r, int c) {
	if(map[r][c]==0) {
		int dir = -1;
		int alt = -1;
		for(int i=0; i<4; i++)
		{
			int nr = r + direction[i][0];
			int nc = c + direction[i][1];
			if(nr > -1 && nr < h && nc > -1 && nc < w) {
				if(altitude[nr][nc] < alt || dir==-1) {
					dir = i;
					alt = altitude[nr][nc];
				}
			}
		}
		
		if(dir == -1 || altitude[r][c] <= alt)
			map[r][c] = curr++;
		else
			map[r][c] = assign(r + direction[dir][0], c + direction[dir][1]);
	}
	
	return map[r][c];
}

int main(void) {
	int n = 0;
	
	cin >> n;
	for(int cno = 0; cno<n; cno++) {
		memset(map, '\0', 10000);
		
		cin>>h>>w;
		for(int i=0; i<h; i++) {
			for(int j=0; j<w; j++) {
				cin>>altitude[i][j];
			}
		}
		
		curr = 'a';
		for(int i=0; i<h; i++) {
			for(int j=0; j<w; j++) {
				if(map[i][j]==0) {
					assign(i, j);
				}
			}
		}
		
		cout<<"Case #"<<(cno+1)<<":"<<endl;
		for(int i=0; i<h; i++) {
			for(int j=0; j<w; j++) {
				cout << map[i][j] << " ";
			}
			cout<<endl;
		}
	}
	
	return EXIT_SUCCESS;
}
