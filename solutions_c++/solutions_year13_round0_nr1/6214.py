/*
 * File:   main.cpp
 * Author: hawkwing
 *
 * Created on April 12, 2013, 6:29 PM
 */

#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

char* get_status(vector< vector<char> > board){
	int moves_left=0;
	for(int r=0;r<4;r++){//check rows
		int x=0;
		int o=0;
		for(int c=0;c<4;c++){
			if(board[r][c]=='X' or board[r][c]=='T'){
				x+=1;
			}
			if(board[r][c]=='O' or board[r][c]=='T'){//counts T for both x and o but that's ok
				o+=1;
			}
			if(board[r][c]=='.'){
				moves_left+=1;
			}
		}
		if(x==4) return "X won";
		if(o==4) return "O won";
	}
	for(int c=0;c<4;c++){//check columns
		int x=0;
		int o=0;
		for(int r=0;r<4;r++){
			if(board[r][c]=='X' or board[r][c]=='T'){
				x+=1;
			}
			if(board[r][c]=='O' or board[r][c]=='T'){
				o+=1;
			}
		}
		if(x==4) return "X won";
		if(o==4) return "O won";
	}
	int x=0;
	int o=0;
	for(int r=0;r<4;r++){//diagonal 1
		if(board[r][r]=='X' or board[r][r]=='T'){
			x+=1;
		}
		if(board[r][r]=='O' or board[r][r]=='T'){
			o+=1;
		}
	}
	if(x==4) return "X won";
	if(o==4) return "O won";

	x=0;
	o=0;
	for(int r=0;r<4;r++){//diagonal 2
		if(board[r][3-r]=='X' or board[r][3-r]=='T'){
			x+=1;
		}
		if(board[r][3-r]=='O' or board[r][3-r]=='T'){
			o+=1;
		}
	}
	if(x==4) return "X won";
	if(o==4) return "O won";
	if(moves_left>0) return "Game has not completed";
	if(moves_left==0) return "Draw";
}

int main(){
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int T;
	in >> T;
	for(int i=0;i<T;i++){
		out << "Case #" << i+1 << ": ";
		vector< vector<char> > board;
		for(int x=0;x<4;x++){
			vector<char> row;
			for(int y=0;y<4;y++){
				char c;
				in >> c;
				row.push_back(c);
			}
			board.push_back(row);
		}
		out << get_status(board) << endl;
		cout << i << endl;
	}
	return 0;
}