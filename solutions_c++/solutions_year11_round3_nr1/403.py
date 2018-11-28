/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  05/07/2011 09:33:17 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main(){
	int T, R, C;
	cin >> T;
	int grid[50][50];
	for(int i = 0 ; i  < T; ++i){
		cin >> R >> C;
		for(int r = 0; r < R; ++r){
			string row;
			cin >> row;
			for(int c = 0; c< C; ++c){
				if(row[c] == '.') grid[r][c] = 0;
				else grid[r][c] = 1;
			}
		}
		bool impossible = false;
		for(int r = 0; r < R; ++r){
			for(int c = 0; c< C; ++c){
				if(grid[r][c] == 1){
					if(c + 1 < C && r + 1 < R){
						if(grid[r][c+1] == 1 &&
						   grid[r+1][c] == 1 &&
						   grid[r+1][c+1] == 1){
							grid[r][c] = 2;
							grid[r][c+1] = 3;
							grid[r+1][c] = 3;
							grid[r+1][c+1] = 2;
						}
						else{
							impossible = true; break;
						}
					}
					else{
						impossible = true; break;
					}
				}
			}
			if(impossible) break;
		}
		cout << "Case #"<<i+1 <<": ";
		if(impossible) {

			cout <<endl << "Impossible" << endl;
		
			/*  for(int r = 0; r < R; ++r){
				for(int c = 0; c< C; ++c){
					cout << grid[r][c];
				}
				cout << endl;
			}*/
		}else{
			cout <<endl;
			for(int r = 0; r < R; ++r){
				for(int c = 0; c< C; ++c){
				  	if(grid[r][c] == 2) cout << "/";
					else if(grid[r][c] == 3) cout << "\\";
					else cout << ".";
			  	}
				cout << endl;
		  	}
		}
	}
}
