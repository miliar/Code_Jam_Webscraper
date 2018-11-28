//File: main.cpp
//Autor: Vukasin Rankovic
#pragma comment(linker, "/STACK:268435456")

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <map>
#include <bitset>
#include <math.h>
#include <stdio.h>
#include <limits.h>
#include <stack>

using namespace std;

ifstream myin("A-large.in");
ofstream myout("A-large.out");

char tableTx[4][4];
char tableTo[4][4];

void main2(){
	char *tmp = new char[6];
	bool full = true;

	//read data
	myin.getline(tmp,6);
	for(int i=0 ; i<4 ; i++){
		myin.getline(tmp,6);
		for(int j=0 ; j<4 ; j++){
			if(tmp[j] == 'T'){
				tableTx[i][j] = 'X';
				tableTo[i][j] = 'O';
			}
			else{
				tableTx[i][j] = tmp[j];
				tableTo[i][j] = tmp[j];
			}
			if(tmp[j]=='.'){
				full = false;
			}
		}
	}

	//horisontal win
	for(int i=0 ; i<4 ; i++){
		char co = tableTo[i][0];
		char cx = tableTx[i][0];
		if(co != '.' && tableTo[i][1] == co && tableTo[i][2] == co && tableTo[i][3] == co){
			myout << co << " won";
			return;
		}
		if(cx != '.' && tableTx[i][1] == cx && tableTx[i][2] == cx && tableTx[i][3] == cx){
			myout << cx << " won";
			return;
		}
	}

	//vertical win
	for(int i=0 ; i<4 ; i++){
		char co = tableTo[0][i];
		char cx = tableTx[0][i];
		if(co != '.' && tableTo[1][i] == co && tableTo[2][i] == co && tableTo[3][i] == co){
			myout << co << " won";
			return;
		}
		if(cx != '.' && tableTx[1][i] == cx && tableTx[2][i] == cx && tableTx[3][i] == cx){
			myout << cx << " won";
			return;
		}
	}

	//diagonal win
	char co = tableTo[0][0];
	char cx = tableTx[0][0];
	if(co != '.' && tableTo[1][1] == co && tableTo[2][2] == co && tableTo[3][3] == co){
		myout << co << " won";
		return;
	}
	if(cx != '.' && tableTx[1][1] == cx && tableTx[2][2] == cx && tableTx[3][3] == cx){
		myout << cx << " won";
		return;
	}
	co = tableTo[0][3];
	cx = tableTx[0][3];
	if(co != '.' && tableTo[1][2] == co && tableTo[2][1] == co && tableTo[3][0] == co){
		myout << co << " won";
		return;
	}
	if(cx != '.' && tableTx[1][2] == cx && tableTx[2][1] == cx && tableTx[3][0] == cx){
		myout << cx << " won";
		return;
	}

	if(full){
		myout << "Draw";
	}
	else{
		myout << "Game has not completed";
	}
}

//Multiple test cases
int main(){
	int t;
	myin >> t;
	for(int i=1 ; i<=t ; i++){
		myout << "Case #" << i << ": ";
		main2();
		myout << endl;
	}
}