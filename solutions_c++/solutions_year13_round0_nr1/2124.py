#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cctype>
#include <cstdio>
#include <cstdlib>

using namespace std;

string solve(vector<string> board)
{	
	int dot = 0;
	for(int i=0;i<4;i++){
		int x_win = 0,o_win=0,t_play=0;
		for(int j=0;j<4;j++){
			char play = board[i][j];
			if(play == 'X') x_win++;
			if(play == 'O') o_win++;
			if(play == '.') dot++;
			if(play == 'T') t_play++; 
		}
		if(x_win == 4) return "X won";
		if(o_win == 4) return "O won";
		if(x_win == 3 && t_play == 1) return "X won";
		if(o_win == 3 && t_play == 1) return "O won";
	}
	

	for(int i=0;i<4;i++){
		int x_win = 0,o_win=0,t_play=0;
		for(int j=0;j<4;j++){
			char play = board[j][i];
			if(play == 'X') x_win++;
			if(play == 'O') o_win++;
			if(play == '.') dot++;
			if(play == 'T') t_play++; 
		}
		if(x_win == 4) return "X won";
		if(o_win == 4) return "O won";
		if(x_win == 3 && t_play == 1) return "X won";
		if(o_win == 3 && t_play == 1) return "O won";
	}

	int x_win = 0,o_win=0,t_play=0;
	int i =0,j=0;
	while(i < 4){
		char play = board[i][j];
		if(play == 'X') x_win++;
		if(play == 'O') o_win++;
		if(play == '.') dot++;
		if(play == 'T') t_play++;
		i++;j++;
	}
	if(x_win == 4) return "X won";
	if(o_win == 4) return "O won";
	if(x_win == 3 && t_play == 1) return "X won";
	if(o_win == 3 && t_play == 1) return "O won";

	x_win = 0,o_win=0,t_play=0;
	i=0,j=3;
	while(i < 4){
		char play = board[i][j];
		if(play == 'X') x_win++;
		if(play == 'O') o_win++;
		if(play == '.') dot++;
		if(play == 'T') t_play++;
		i++;j--;
	}
	if(x_win == 4) return "X won";
	if(o_win == 4) return "O won";
	if(x_win == 3 && t_play == 1) return "X won";
	if(o_win == 3 && t_play == 1) return "O won";

	if(dot == 0) return "Draw";
	return "Game has not completed";
}


int main()
{
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	vector<string> result;
	int caseno;
	scanf("%d",&caseno);
	for(int j=0;j<caseno;j++){
		vector<string> board;
		for(int i=0;i<4;i++){
			string games;
			cin >> games;
			board.push_back(games);
		}
		string data = solve(board);
		result.push_back(data);
	}

	for(int case_id=0;case_id<caseno;case_id++){
		cout << "Case #" << case_id+1 << ": " << result[case_id] << endl;
	}	
	return 0;
}