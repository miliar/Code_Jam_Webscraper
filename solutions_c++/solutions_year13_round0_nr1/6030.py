#include "board.h"

void Board::readInput() {

	for(int i=0; i < 4; ++i){
		std::string row;
		std::cin >> row;

		rows.push_back(row);
	}
}

void Board::processData() {
	if(foundInRow()){
		printOutput();
	}
	else if(foundInColumn()){
		printOutput();
	}
	else if(foundInDiagonal()){
		printOutput();
	}
	else{
		printOutput();
	}

}

void Board::printOutput() {

	for(int i=0; i<4; ++i){
	}
	std::cout << "Case #" << casenum << ": ";

	if(winning_player != 'N'){
		std::cout << winning_player << " won" << std::endl;
	}
	else{
		if(draw){
			std::cout << "Draw" << std::endl;
		}
		else{
			std::cout << "Game has not completed" << std::endl;
		}
	}

}

bool Board::foundInRow() {
	for(int i=0; i<4; ++i){
		bool won = true;
		char first_val;
		if(rows[i][0] == 'T'){
			if(rows[i][1] == '.'){
				draw = false;
				continue;
			}
			first_val = rows[i][1];
		}
		else if(rows[i][0] == '.'){
			draw = false;
			continue;
		}
		else{
			first_val = rows[i][0];
		}
		for(int j=1; j<4; ++j){
			if(won){
				won = check(i,j,first_val);
			}
		}
		if(won){
			//std::cout << "Won in Row" << std::endl;
			winning_player = first_val;
			return true;
		}

	}
	return false;
}

bool Board::foundInColumn() {
	for(int i=0; i<4; ++i){
		char first_val;
		if(rows[0][i] == 'T'){
			if(rows[1][i] == '.'){
				draw = false;
				continue;
			}
			first_val = rows[1][i];
		}
		else if(rows[0][i] == '.'){
			draw = false;
			continue;
		}
		else{
			first_val = rows[0][i];
		}
		bool won = true;
		for(int j=1; j<4; ++j){
			if(won){
				won = check(j,i,first_val);
			}
		}
		if(won){
			//std::cout << "Won in Column" << std::endl;
			winning_player = first_val;
			return true;
		}

	}
	return false;
}

bool Board::check(int i, int j,const char first_val) {
	bool won = true;
	if(rows[i][j] != first_val){

		if(rows[i][j] != 'T'){

			if(rows[i][j] == '.'){
				draw = false;
				won = false;
			}
			won = false;
		}
	}
	return won;
}

bool Board::foundInDiagonal() {
	char first_val;
	bool won = true;
	if(rows[0][0] == 'T'){
		if(rows[1][1] == '.'){
				won = false;
				draw = false;
		}
		first_val = rows[1][1];
	}
	else if(rows[0][0] == '.'){
		won = false;
		draw = false;
	}
	else{
		first_val = rows[0][0];
	}

	for(int i=0; i<4; ++i){
		if(won){
			won = check(i,i,first_val);
		}
	}
	if(won){
		//std::cout << "Won in First Diagonal" << std::endl;
		winning_player = first_val;
		return true;
	}
//////// sencond part
	won = true;
	if(rows[0][3] == 'T'){
		if(rows[1][2] == '.'){
				won = false;
				draw = false;
			}
		first_val = rows[1][2];
	}
	else if(rows[0][3] == '.'){
		won = false;
		draw = false;
	}
	else{
		first_val = rows[0][3];
	}

	if(won){
		if(check(1,2,first_val) && check(2,1,first_val) &&
				check(3,0,first_val) && check(0,3,first_val)){
			won = true;
		}
		else{
			won = false;
		}
	}
	if(won){
		//std::cout << "Won in Second Diagonal" << std::endl;
		winning_player = first_val;
		return true;
	}
	else{
		return false;
	}
}
