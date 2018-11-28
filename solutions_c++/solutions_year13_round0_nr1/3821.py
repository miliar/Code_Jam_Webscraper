#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool solve_helper_O(vector<string>& board, ofstream& output, int casenum){
	//check main diag:
	if (
		board[0][0]==board[1][1] &&
		board[0][0]==board[2][2] &&
		board[0][0]==board[3][3] &&
		board[0][0]!='.'
	){
		if (board[0][0]=='X'){
			output<<"Case #"<<casenum<<": X won"<<endl;
		} else {
			output<<"Case #"<<casenum<<": O won"<<endl;
		}
		return true;
	}

	//check reverse diag:
	if (
		board[0][3]==board[1][2] &&
		board[0][3]==board[2][1] &&
		board[0][3]==board[3][0] &&
		board[0][3]!='.'
	){
		if (board[0][3]=='X'){
			output<<"Case #"<<casenum<<": X won"<<endl;
		} else {
			output<<"Case #"<<casenum<<": O won"<<endl;
		}
		return true;
	}
	
	//check each row:
	for (int i=0; i<4; i++){
		string row = board[i];
		if (
			row[0]==row[1] &&
			row[0]==row[2] &&
			row[0]==row[3] &&
			row[0]!='.'
		){
			if (row[0]=='X'){
				output<<"Case #"<<casenum<<": X won"<<endl;
			} else {
				output<<"Case #"<<casenum<<": O won"<<endl;
			}
			return true;
		}
	}
	
	//check each col:
	for (int j=0; j<4; j++){
		char col[4];
		for (int i=0; i<4; i++)
			col[i] = board[i][j];
		if (
			col[0]==col[1] &&
			col[0]==col[2] &&
			col[0]==col[3] &&
			col[0]!='.'
		){
			if (col[0]=='X'){
				output<<"Case #"<<casenum<<": X won"<<endl;
			} else {
				output<<"Case #"<<casenum<<": O won"<<endl;
			}
			return true;
		}
	}
	
	return false;
}
void check_draw_incomplete(vector<string>& board, ofstream& output, int casenum){
	//check draw/incomplete (i.e. no./exist.)
	for (int i=0; i<4; i++){
		for (int j=0; j<4; j++){
			if (board[i][j]=='.'){
				output<<"Case #"<<casenum<<": Game has not completed"<<endl;
				return;
			}
		}
	}
	output<<"Case #"<<casenum<<": Draw"<<endl;
	return;
}

void solve_helper_X(vector<string>& board, ofstream& output, int casenum){
	//check main diag:
	if (
		board[0][0]==board[1][1] &&
		board[0][0]==board[2][2] &&
		board[0][0]==board[3][3] &&
		board[0][0]!='.'
	){
		if (board[0][0]=='X'){
			output<<"Case #"<<casenum<<": X won"<<endl;
		} else {
			output<<"Case #"<<casenum<<": O won"<<endl;
		}
		return;
	}

	//check reverse diag:
	if (
		board[0][3]==board[1][2] &&
		board[0][3]==board[2][1] &&
		board[0][3]==board[3][0] &&
		board[0][3]!='.'
	){
		if (board[0][3]=='X'){
			output<<"Case #"<<casenum<<": X won"<<endl;
		} else {
			output<<"Case #"<<casenum<<": O won"<<endl;
		}
		return;
	}
	
	//check each row:
	for (int i=0; i<4; i++){
		string row = board[i];
		if (
			row[0]==row[1] &&
			row[0]==row[2] &&
			row[0]==row[3] &&
			row[0]!='.'
		){
			if (row[0]=='X'){
				output<<"Case #"<<casenum<<": X won"<<endl;
			} else {
				output<<"Case #"<<casenum<<": O won"<<endl;
			}
			return;
		}
	}
	
	//check each col:
	for (int j=0; j<4; j++){
		char col[4];
		for (int i=0; i<4; i++)
			col[i] = board[i][j];
		if (
			col[0]==col[1] &&
			col[0]==col[2] &&
			col[0]==col[3] &&
			col[0]!='.'
		){
			if (col[0]=='X'){
				output<<"Case #"<<casenum<<": X won"<<endl;
			} else {
				output<<"Case #"<<casenum<<": O won"<<endl;
			}
			return;
		}
	}
	
	//check draw/incomplete (i.e. no./exist.)
	for (int i=0; i<4; i++){
		for (int j=0; j<4; j++){
			if (board[i][j]=='.'){
				output<<"Case #"<<casenum<<": Game has not completed"<<endl;
				return;
			}
		}
	}
	output<<"Case #"<<casenum<<": Draw"<<endl;
	return;
}
void solve(vector<string>& board, ofstream& output, int casenum){
	int Tx = -1;
	int Ty = -1;
	for (int i=0; i<4; i++){
		for (int j=0; j<4; j++){
			if (board[i][j]=='T'){
				board[i][j]='O';
				Tx = i;
				Ty = j;
			}
		}
	}
	if (!solve_helper_O(board, output, casenum)){
		if (Tx!=-1&&Ty!=-1){
			board[Tx][Ty] = 'X';
			solve_helper_X(board, output, casenum);
		} else {
			check_draw_incomplete(board, output, casenum);
		}
	}
	

}

int main(){
	ifstream input("input.txt");
	ofstream output;
	output.open("output.txt");
	if (input.is_open()){
		int numcases = -1;
		int casenum = 1;
		
		int numrowscanned = 0;
		
		vector<string> board;
		while (input.good()){
			string line;
			getline(input, line);
			if (numcases == -1){
				istringstream iss(line);
				iss>>numcases;
				board.clear();
				continue;
			}
			
			//cout<<"line: "<<line<<endl;
			
			if (line.size()==0){
				board.clear();
				continue;
			}
			
			board.push_back(line);
			numrowscanned = numrowscanned + 1;
			
			if (numrowscanned == 4){
				//flush test case:
				solve(board, output, casenum);
				casenum++;
				board.clear();
				numrowscanned = 0;
			}
			
		}
	}
	input.close();
	output.close();
	return 0;
}

