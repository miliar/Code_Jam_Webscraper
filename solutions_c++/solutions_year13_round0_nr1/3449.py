#include<iostream>
#include<vector>
#include<string>
using std::vector;
using std::cin;
using std::cout;
using std::endl;
using std::string;
void check(vector<string> board){
	int topRightX=0, topRightO=0;
	int topLeftX=0, topLeftO=0;
	int dotNum=0;
	for(int i=0; i<4; i++){
		if(board[i][i] =='X'){
			topLeftX++;
		}
		if(board[i][i] == 'O'){
			topLeftO++;
		}
		if(board[i][i] == '.'){
			topLeftX++;
			topLeftO++;
			dotNum++;
		}
		if(board[i][3-i] == 'X'){
			topRightX++;
		}
		if(board[i][3-i] == 'O'){
			topRightO++;
		}
		if(board[i][3-i] == '.'){
			topRightO++;
			topRightX++;
			dotNum++;
		}
		int X=0, O=0;
		for(int j=0; j<4; j++){
			if(board[i][j] == 'X'){
				X++;
			}
			if(board[i][j] == 'O'){
				O++;
			}
			if(board[i][j] == '.'){
				X++;
				O++;
				dotNum++;
			}
		}
		if(X == 0 && O != 0){
			cout<<"O won"<<endl;
			return;
		}
		if(X != 0 && O == 0){
			cout<<"X won"<<endl;
			return;
		}
		X=0;
		O=0;
		for(int j=0; j<4; j++){
			if(board[j][i] == 'X'){
				X++;
			}
			if(board[j][i] == 'O'){
				O++;
			}
			if(board[j][i] == '.'){
				X++;
				O++;
				dotNum++;
			}
		}
		if(X == 0 && O != 0){
			cout<<"O won"<<endl;
			return;
		}
		if(X != 0 && O == 0){
			cout<<"X won"<<endl;
			return;
		}		
	}
	if(topRightX == 0 && topRightO != 0){
		cout<<"O won"<<endl;
		return;
	}
	if(topRightX != 0 && topRightO == 0){
		cout<<"X won"<<endl;
		return;
	}
	if(topLeftX == 0 && topLeftO != 0){
		cout<<"O won"<<endl;
		return;
	}
	if(topLeftX !=0 && topLeftO == 0){
		cout<<"X won"<<endl;
		return;
	}
	if(dotNum == 0){
		cout<<"Draw"<<endl;
		return;
	}
	cout<<"Game has not completed"<<endl;
	return;
}
int main(){
	int caseNo;
	cin>>caseNo;
	for(int count=0; count<caseNo; count++){
		cout<<"Case #"<<count+1<<": ";
		vector<string> board;
		for(int i=0; i<4; i++){
			string str;
			cin>>str;
			board.push_back(str);
		}
		check(board);
	}
	return 0;
}