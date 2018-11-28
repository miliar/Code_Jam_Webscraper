//============================================================================
// Name        : Tiny2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <fstream>
#define rep(i,n) for(int i = 0;i<n;i++)

using namespace std;



char board[4][4];
bool isOwin(){
	char tmp[4][4];
	rep(i,4)rep(j,4){
		if(board[i][j] == 'T'){
			tmp[i][j] = 'O';
		}else{
			tmp[i][j] = board[i][j];
		}
	}
	bool flag = true;
	rep(i,4){
		flag = true;
		rep(j,4){
			flag = flag && (tmp[i][j] == 'O');
		}
		if(flag) return true;
	}
	rep(i,4){
		flag = true;
		rep(j,4){
			flag = flag && (tmp[j][i] == 'O');
		}
		if(flag) return true;
	}
	flag = true;
	rep(i,4){
		flag = flag && (tmp[i][i] == 'O');
	}
	if(flag) return true;
	flag = true;
	rep(i,4){
		flag = flag && (tmp[i][3-i] == 'O');
	}
	if(flag) return true;
	return false;
}
bool isXwin(){
	char tmp[4][4];
	rep(i,4)rep(j,4){
		if(board[i][j] == 'T'){
			tmp[i][j] = 'X';
		}else{
			tmp[i][j] = board[i][j];
		}
	}
	bool flag = true;
	rep(i,4){
		flag = true;
		rep(j,4){
			flag = flag && (tmp[i][j] == 'X');
		}
		if(flag) return true;
	}
	rep(i,4){
		flag = true;
		rep(j,4){
			flag = flag && (tmp[j][i] == 'X');
		}
		if(flag) return true;
	}
	flag = true;
	rep(i,4){
		flag = flag && (tmp[i][i] == 'X');
	}
	if(flag) return true;
	flag = true;
	rep(i,4){
		flag = flag && (tmp[i][3-i] == 'X');
	}
	if(flag) return true;
	return false;
}
bool isFilled(){
	bool flag = true;
	rep(i,4)rep(j,4){
		flag = flag && (board[i][j] != '.');
	}
	return flag;
}

int main() {

	ifstream fin("./input.txt");
	ofstream fout("./output.txt");
	int N;
	fin >> N;
	for(int Case = 1;Case<=N;Case++){
		rep(i,4){
			string s;
			fin >> s;
			rep(j,4){
				board[i][j] = s[j];
			}
		}
		if(isXwin()){
			fout << "Case #" << Case << ": X won" << endl;
		}else if(isOwin()){
			fout << "Case #" << Case << ": O won" << endl;
		}else if(isFilled()){
			fout << "Case #" << Case << ": Draw" << endl;
		}else{
			fout << "Case #" << Case << ": Game has not completed" << endl;
		}
	}

	return 0;
}
