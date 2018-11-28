#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

char map[51][51];

int main() {
	
	int T,r,c;
	char tmp;
	
	cin >> T;
	
	for(int test = 1; test <= T; test++) {
	
		cin >> r >> c;
		
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
			
				scanf("%c", &tmp);
				
				if(tmp == 10) scanf("%c", &tmp);
				
				map[i][j] = tmp;
					
				
			}
		} 
		
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
			
				if(map[i][j] == '#' && map[i][j+1] == '#' && map[i+1][j] == '#' && map[i+1][j+1] == '#') {
					
					map[i][j] = '/';
					map[i][j+1] = '\\';
					map[i+1][j] = '\\';
					map[i+1][j+1] = '/';
					
				}
			
			}

		} 



		
		bool impos = false;
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {

					if(map[i][j] == '#')
						impos = true;
			
			}
		} 
		
		cout << "Case #" << test << ":\n";
		
		if(impos){ 
			cout << "Impossible" << endl;
		} else {
		
			for(int i = 0; i < r; i++) {
				for(int j = 0; j < c; j++) {

					cout << map[i][j];
			
				}
				cout << endl;
			} 
		}
		
		
	}



return 0;
}
