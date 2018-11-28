#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;
int automaton[11][4] = {
	1,5,9,10,
	2,10,2,10,
	3,10,3,10,
	4,10,4,10,
	4,4,4,4,
	10,6,6,10,
	10,7,7,10,
	10,8,8,10,
	8,8,8,8,
	2,6,10,10,
	10,10,10,10
};
char testRow(vector<string> &matrix,int row){
	int currentState = 0;
	char element;
	int next;
	for(int i=0;i<4;i++){
		element = matrix[row][i];
		if(element=='X') next = 0;
		else if(element=='O') next = 1;
		else if(element=='T') next = 2;
		else next = 3;
		currentState = automaton[currentState][next];
	}
	if(currentState==4) return 'X';
	else if(currentState==8) return 'O';
	else return '.';
}
char testCol(vector<string> &matrix,int col){
	int currentState = 0;
	char element;
	int next;
	for(int i=0;i<4;i++){
		element = matrix[i][col];
		if(element=='X') next = 0;
		else if(element=='O') next = 1;
		else if(element=='T') next = 2;
		else next = 3;
		currentState = automaton[currentState][next];
	}
	if(currentState==4) return 'X';
	else if(currentState==8) return 'O';
	else return '.';
}
char testDiag(vector<string> &matrix,bool down){
	int currentState = 0;
	char element;
	int next;
	for(int i=0;i<4;i++){
		if(down)
			element = matrix[i][i];
		else
			element = matrix[i][3-i];
		if(element=='X') next = 0;
		else if(element=='O') next = 1;
		else if(element=='T') next = 2;
		else next = 3;
		currentState = automaton[currentState][next];
	}
	if(currentState==4) return 'X';
	else if(currentState==8) return 'O';
	else return '.';
}
int main(){
	int tests;
	cin>>tests;
	vector<string> matrix(4,"....");
	char input;
	for(int test=1;test<=tests;test++){
		bool dot = false;
		for(int i=0;i<4;i++){
			cin>>matrix[i];
			for(int j=0;j<matrix[i].size();j++){
				if(matrix[i][j]=='.') dot = true;
			}
		}
		char winner='.';
		for(int i=0;i<4;i++){
			winner = testRow(matrix,i);
			if(winner!='.') break;
		}
		if(winner=='.'){
			for(int i=0;i<4;i++){
				winner = testCol(matrix,i);
				if(winner!='.') break;
			}
			if(winner=='.'){
				winner = testDiag(matrix,true);
				if(winner=='.')
					winner = testDiag(matrix,false);
			}
		}
		if(winner=='.'){
			if(dot){
				printf("Case #%d: Game has not completed\n",test);
			}
			else{
				printf("Case #%d: Draw\n",test);
			}
		}
		else{
			printf("Case #%d: %c won\n",test,winner);
		}
	}
	return 0;
}