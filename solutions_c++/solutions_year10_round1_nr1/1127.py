//      main.cpp
//      
//      Copyright 2010 Ryan <ryan@ryan-laptop>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.

#include <fstream>
#include <iostream>

using namespace std;
/*
struct node
  {  
     int size;
     int number;         
     bool firston;
     node *nxt;        // Pointer to next node
  };

node *start = NULL;
node *current;
node *nstart = NULL;

*/

bool check ( char color, int dx, int dy, int sx, int sy, int num);

char board[50][50];
int total,i,size,K;


int main(int argc, char** argv)
{
	
	ifstream fp("input.in");
    ofstream op ("output.txt");
	//int red[5000]; //2500 * 2
	//int blue[5000];
	bool rfound = false;
	bool bfound = false;
	bool done;
	fp >> total;
	
	
	for ( i = 1; i <= total; i++){
		
		rfound = false;
		bfound = false;
	
		fp >> size;
		fp >> K;
		
		for ( int px = 0; px < 50; px++){
			for ( int py = 0; py < 50; py++){
				board[px][py] = '.';
			}
		}
		for (int u = 0; u < size; u++){
			for (int h = 0; h < size; h++){
				fp >> board[size - 1 - u][h];
			}
		}
		
		for (int c = size; c >= 0; c--){
			for (int b = 0; b < size; b++){
				if ( board[b][c] != '.'){
					int tempb = b;
					int tempc = c;
					done = false;
					while ( done != true && c < size - 1){
						if ( board[b][c+1] == '.' ){
							
							board[b][c+1] = board[b][c];
							board[b][c] = '.';
							c = c + 1;
						}
						else { done = true; }
					}
					b = tempb;
					c = tempc;
				}
			}
		}
		for (int x = 0; x < size; x++ ){
			for (int y = 0; y < size; y++){
				if ( board[x][y] != '.' ){
					for (int cx = -1; cx <= 1; cx++){
						for ( int cy = -1; cy <=1; cy++){
							if ( cx != 0 || cy != 0){
								if ( rfound == false && board[x][y] == 'R' && check( 'R', cx, cy, x,y, K) == true){
									rfound = true;
								}
								else if( bfound == false && board[x][y] == 'B' && check('B',cx,cy,x,y,K) == true){
									bfound = true;
								}
							}
						}
					}
				}
			}
		}
		
		if ( rfound == true && bfound == true ){
			op << "Case #" << i << ": Both" << endl;
		}
		else if ( rfound == true ){
			op << "Case #" << i <<": Red" << endl;
		}
		else if ( bfound == true ){
			op <<"Case #" << i << ": Blue" << endl;
		}
		else {
			op <<"Case #" << i << ": Neither" << endl;
		}
		
		
	}
	return 0;
	
	
}
bool check ( char color, int dx, int dy, int sx, int sy, int num){
	
	if (board[sx + dx][sy + dy] != color){
		return false;
	}
	else if (num == 2){
		return true;
	}
	else {
		return check(color,dx,dy,sx + dx, sy + dy, num - 1);
	}
}
