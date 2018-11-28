#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <queue>
#include <cstdio>
#include <fstream>
using namespace std;

string gameState(string board[4]){
	//rows
	for (int i=0; i<4; i++){
		if (board[i][0]==board[i][1]&&board[i][1]==board[i][2]&&board[i][2]==board[i][3]){
			if(board[i][0]=='X') return "X won";
			if(board[i][0]=='O') return "O won";
		}
	}
	//cols
	for (int i=0; i<4; i++){
		if (board[0][i]==board[1][i]&&board[1][i]==board[2][i]&&board[2][i]==board[3][i]){
			if(board[0][i]=='X') return "X won";
			if(board[0][i]=='O') return "O won";
		}
	}
	//diags
	if (board[0][0]==board[1][1]&&board[1][1]==board[2][2]&&board[2][2]==board[3][3]){
		if(board[0][0]=='X') return "X won";
		if(board[0][0]=='O') return "O won";
	}
	if (board[0][3]==board[1][2]&&board[1][2]==board[2][1]&&board[2][1]==board[3][0]){
		if(board[0][3]=='X') return "X won";
		if(board[0][3]=='O') return "O won";
	}

	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			if (board[i][j]=='.')
				return "Game has not completed";

	return "Draw";
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T=0;
	cin>>T;
	for (int t=1; t<=T; t++){
		string board[4];
		for (int i=0; i<4; i++)
			cin>>board[i];
		string board1[4];string board2[4];
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++){
				if (board[i][j]=='T') board1[i]+='X';
				else board1[i]+=board[i][j];
			}	
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++){
				if (board[i][j]=='T') board2[i]+='O';
				else board2[i]+=board[i][j];
			}
		string state1 = gameState(board1);
		string state2 = gameState(board2);

		if (state1=="X won"||state1=="O won"){
			cout<<"Case #"<<t<<": "<<state1<<"\n";
			continue;
		}
		if (state2=="X won"||state2=="O won"){
			cout<<"Case #"<<t<<": "<<state2<<"\n";
			continue;
		}

		if (state1=="Game has not completed"||state2=="Game has not completed"){
			cout<<"Case #"<<t<<": "<<"Game has not completed"<<"\n";
			continue;
		}
		cout<<"Case #"<<t<<": "<<"Draw"<<"\n";
	}

	return 0;
}