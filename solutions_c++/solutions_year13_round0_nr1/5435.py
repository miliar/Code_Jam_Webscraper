#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<map>
#include<queue>
#include<utility>
#include<string>
#include<sstream>

using namespace std;

#define tr(c, it) \
        for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)

// checks configuration of board
string check_config(vector<string> &board){

	string output;
	map<char, int>cnt;

	// flag is 1 if the board is full
	int flag = 0;

	// check rows
	for(int i = 0; i < 4; i++){
			
		cnt['X'] = 0;
		cnt['O'] = 0;

		for(int j = 0; j < 4; j++){

			if(board[i][j] == '.'){
				flag = 1;
				break;
			}

			char ch = board[i][j];
			cnt[ch] = cnt[ch] + 1;

			if(cnt['X'] && cnt['O']) break;
		
			if(j == 3){

		 		if( cnt['X'] > 0 ){
					output = "X won";
					return output;
				} 
		
				 else if( cnt['O'] > 0){
					output = "O won";
					return output;
				} 
		}
	}
	}
		
	// check columns
	for(int i = 0; i < 4; i++){
		
		cnt['X'] = 0;
		cnt['O'] = 0;

		for(int j = 0; j < 4; j++){

			if(board[j][i] == '.'){
				break;
			}

			char ch = board[j][i];
			cnt[ch] = cnt[ch] + 1;

			if(cnt['X'] && cnt['O']) break;
		
			if(j == 3){

		 		if( cnt['X'] > 0 ){
					output = "X won";
					return output;
				} 
		
				 else if( cnt['O'] > 0){
					output = "O won";
					return output;
				} 
		}
	}
	}

	cnt['X'] = 0;
	cnt['O'] = 0;
	// check diagonal 1
	for(int i = 0; i < 4; i++){

		int j = i;		
		if(board[j][i] == '.'){
			break;
		}

		char ch = board[j][i];
		cnt[ch] = cnt[ch] + 1;

		if(cnt['X'] && cnt['O']) break;
		
		if(j == 3){

		 	if( cnt['X'] > 0 ){
				output = "X won";
				return output;
			} 
		
			 else if( cnt['O'] > 0){
				output = "O won";
				return output;
			} 

		}
	}		

	cnt['X'] = 0;
	cnt['O'] = 0;
	// check diagonal 1
	for(int i = 0; i < 4; i++){

		int j = 4-i-1;		
		if(board[i][j] == '.'){
			break;
		}

		char ch = board[i][j];
		cnt[ch] = cnt[ch] + 1;

		if(cnt['X'] && cnt['O']) break;
		
		if(i == 3){

		 	if( cnt['X'] > 0 ){
				output = "X won";
				return output;
			} 
		
			 else if( cnt['O'] > 0){
				output = "O won";
				return output;
			} 

		}
	}		

	if(flag == 1){
		output = "Game has not completed";
		return output;
	}
	else{
		output = "Draw";
		return output;
		
	}
	
}

int main()
{	
	int N;
	cin >> N;

	for(int i = 0; i < N; i++){

		vector<string>board;
		string s;
		
		for(int k = 0; k < 4; k++){
			cin >> s;
			board.push_back(s);		
		}
		
		string output = check_config(board);
		
		cout << "Case #" << i+1 << ": " << output << endl;
	}

	return 0;
}
