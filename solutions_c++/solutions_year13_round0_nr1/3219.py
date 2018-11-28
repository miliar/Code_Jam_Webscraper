#include <iostream>
#include <string>

using namespace std;

char getFirst(string s){
	char first = s[0];
	int index = 0;
	while(first == 'T')
		first = s[++index];
	return first;
}


bool findWinner(string line){
	bool canWin = true;
	char first = getFirst(line);

	for(int j = 0; j < 4 && canWin; ++j){
		if(line[j] == '.' || (line[j] != first && line[j] != 'T')){
			canWin = false;
			break;
		}
	}
	if(canWin){
		cout << first << " won" << endl;
		return true;
	}

	return false;
}


bool isDraw(string board[]){
	for(int i = 0; i < 4; ++i){
		if (string::npos != board[i].find("."))
			return false;
	}
	return true;
}

int main(){
	int k;
	cin >> k;
	bool isFound = false;

	for(int c = 1; c < k+1; ++c){
		cout << " Case #" << c << ": ";
		isFound = false;
		
		string board[] = { "", "", "", ""};
		for(size_t row = 0; row < 4; ++row)
			cin >> board[row];
		
		for(int i = 0; i < 4; ++i){
			if(findWinner(board[i])){
				isFound = true;
				break;
			}
		}
		if(isFound)
			continue;

		string vert = "";
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j)
				vert += board[j][i];
			if(findWinner(vert)){
				isFound = true;
				break;
			}
			vert = "";
		}
		if(isFound)
			continue;

		for(int i = 0; i < 4; ++i)
				vert += board[i][i];
		
		if(findWinner(vert))
			continue;
		vert = "";

		for (int i = 0; i < 4; ++i)
			vert += board[i][3-i];
		if (findWinner(vert))
			continue;

		if(isDraw(board))
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
		
	}


}
	//




