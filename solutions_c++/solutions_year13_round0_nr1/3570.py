#include<string>
#include<iostream>
#include<vector>
#include<array>

enum{X_WON,O_WON,DRAW,NOT_FINISHED};
std::string r_string[]={"X won","O won","Draw","Game has not completed"};
std::vector<std::array<std::array<char,4>,4 > > cases;

void parse_input(std::istream& input){
	int cases_n; 	input>>cases_n; 
	cases.resize(cases_n);
	for(auto& board:cases){
		for(int i=0;i<4;i++){
		       for(int j=0;j<4;j++) input>>board[i][j];
		       //char endl; input>>endl;
		}
		//char endl; input>>endl;
	}
}

int solve_case(std::array<std::array<char,4>,4 >& board){
	for(int i=0;i<4;i++){
		if((board[i][0]=='X' || board[i][0]=='T') && (board[i][1]=='X' || board[i][1]=='T') && (board[i][2]=='X' || board[i][2]=='T') && (board[i][3]=='X' || board[i][3]=='T')) return X_WON;
		if((board[i][0]=='O' || board[i][0]=='T') && (board[i][1]=='O' || board[i][1]=='T') && (board[i][2]=='O' || board[i][2]=='T') && (board[i][3]=='O' || board[i][3]=='T')) return O_WON;
	}
	for(int j=0;j<4;j++){
		if((board[0][j]=='X' || board[0][j]=='T') && (board[1][j]=='X' || board[1][j]=='T') && (board[2][j]=='X' || board[2][j]=='T') && (board[3][j]=='X' || board[3][j]=='T')) return X_WON;
		if((board[0][j]=='O' || board[0][j]=='T') && (board[1][j]=='O' || board[1][j]=='T') && (board[2][j]=='O' || board[2][j]=='T') && (board[3][j]=='O' || board[3][j]=='T')) return O_WON;
	}
	if((board[0][0]=='X' || board[0][0]=='T') && (board[1][1]=='X' || board[1][1]=='T') && (board[2][2]=='X' || board[2][2]=='T') && (board[3][3]=='X' || board[3][3]=='T')) return X_WON;
	if((board[0][0]=='O' || board[0][0]=='T') && (board[1][1]=='O' || board[1][1]=='T') && (board[2][2]=='O' || board[2][2]=='T') && (board[3][3]=='O' || board[3][3]=='T')) return O_WON;
	if((board[0][3]=='X' || board[0][3]=='T') && (board[1][2]=='X' || board[1][2]=='T') && (board[2][1]=='X' || board[2][1]=='T') && (board[3][0]=='X' || board[3][0]=='T')) return X_WON;
	if((board[0][3]=='O' || board[0][3]=='T') && (board[1][2]=='O' || board[1][2]=='T') && (board[2][1]=='O' || board[2][1]=='T') && (board[3][0]=='O' || board[3][0]=='T')) return O_WON;
	for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(board[i][j]=='.')return NOT_FINISHED;
	return DRAW;
}

int main(){
	parse_input(std::cin);
	for(int i=0;i<cases.size();i++){
		std::cout<<"Case #"<<i+1<<": "<<r_string[solve_case(cases[i])]<<std::endl;
	}

	return 0;
}
