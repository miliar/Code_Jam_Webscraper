#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

string board[5];

bool playerwon(char player){
	bool ar = true;
	for(int i = 0; i < 4; i++){
		ar = true;
		for(int j = 0; j < 4; j++)
			if(board[i][j] != player && board[i][j] != 'T')
				ar = false;
		if(ar)
			return true;
		}
	
	for(int i = 0; i < 4; i++){
		ar = true;
		for(int j = 0; j < 4; j++)
			if(board[j][i] != player && board[j][i] != 'T')
				ar = false;
		if(ar)
			return true;
		}
	
	ar = true;
	for(int i = 0; i < 4; i++)
		if(board[i][i] != player && board[i][i] != 'T')
			ar = false;
	if(ar)
		return true;
		
	
	ar = true;
	for(int i = 0; i < 4; i++)
		if(board[i][3 - i] != player && board[i][3 - i] != 'T')
			ar = false;
	if(ar)
		return true;
		
	return false;
	}

void solve(){
	if(playerwon('X')){
		printf("X won\n");
		return;
		}
	if(playerwon('O')){
		printf("O won\n");
		return;
		}
	
	bool ended = true;
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(board[i][j] == '.')
				ended = false;
	
	if(ended)
		printf("Draw\n");
	else
		printf("Game has not completed\n");
	}

int main(){
	int testcases;
	scanf("%d", &testcases);
	
	for(int testcase = 0; testcase < testcases; testcase++){
		for(int i = 0; i < 4; i++)
			cin >> board[i];
		scanf("\n");
		printf("Case #%d: ", testcase+1);
		solve();
		}
	
	
	return 0;
}
