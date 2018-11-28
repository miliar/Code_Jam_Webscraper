#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

enum STATE{
	X_WON,
	O_WON,
	DRAW,
	NOT_COMPLETED,
};

void ReadFile(std::ifstream& ifs);
char GetToken(char c);
STATE Judge();
void Print(std::ofstream& ofs, int count, STATE state);

const char* IN = "source.txt";

const char* OUT = "out.txt";

const char DOT = 0;

const char X = 1;

const char O = 1 << 1;

const char T = O | X;

char g_board[4][4];

bool g_is_dot_exist = false;

int main(){
	std::ifstream ifs(IN);
	std::ofstream ofs(OUT);

	std::string buf;
	getline(ifs, buf);
	std::stringstream ss;
	ss << buf;
	int count;
	ss >> count;

	for(int i = 0; i < count; i++){
		ReadFile(ifs);

		STATE state = Judge();
		Print(ofs, i, state);
	}
	
	return 0;
}

void ReadFile(std::ifstream& ifs){
	g_is_dot_exist = false;

	for(int i = 0; i < 4; i++){
		char buf[5];
		ifs.getline(buf, 5);
		for(int j = 0; j < 4; j++){
			if(buf[j] == '.'){
				g_is_dot_exist = true;
			}

			g_board[i][j] = GetToken(buf[j]);
		}
	}

	ifs.ignore();
}

char GetToken(char c){
	switch(c){
	case 'O':
		return O;

	case 'X':
		return X;

	case 'T':
		return T;

	case '.':
		return DOT;
	}

	return -1;
}

STATE Judge(){
	char result;
	for(int i = 0; i < 4; i++){
		result = g_board[i][0] & g_board[i][1] & g_board[i][2] & g_board[i][3];
		if(result == X){
			return X_WON;
		}else if(result == O){
			return O_WON;
		}
	}

	for(int i = 0; i < 4; i++){
		result = g_board[0][i] & g_board[1][i] & g_board[2][i] & g_board[3][i];
		if(result == X){
			return X_WON;
		}else if(result == O){
			return O_WON;
		}
	}

	result =  g_board[0][0] & g_board[1][1] & g_board[2][2] & g_board[3][3];
	if(result == X){
		return X_WON;
	}else if(result == O){
		return O_WON;
	}

	result =  g_board[0][3] & g_board[1][2] & g_board[2][1] & g_board[3][0];
	if(result == X){
		return X_WON;
	}else if(result == O){
		return O_WON;
	}

	if(g_is_dot_exist){
		return NOT_COMPLETED;
	}

	return DRAW;
}

void Print(std::ofstream& ofs, int count, STATE state){
	std::string output;

	switch(state){
	case X_WON:
		output = "X won";
		break;

	case O_WON:
		output = "O won";
		break;

	case DRAW:
		output = "Draw";
		break;

	case NOT_COMPLETED:
		output = "Game has not completed";
		break;

	}

	ofs  << "Case #" << count + 1 << ": " << output << std::endl;
}
