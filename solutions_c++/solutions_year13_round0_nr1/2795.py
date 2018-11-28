/* Tic Tac Toe Tomek */
/*
 Auther: MM BARI
 progrmming language: c++
 email: talashbari@gmail.com
 */


#include <string>
using std::string;

#include <iostream>
using std::cerr;
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;
using std::ofstream;

using namespace std;
char board[4][4];

bool is_player_won(char player)
{
	int count = 0;
	for (size_t row = 0; row < 4; ++row) {
		count = 0;
		for (size_t col = 0; col < 4; ++col) {
			if ((board[row][col] == player || board[row][col] == 'T')) {
				++count;
			} else {
				break;
			}
		}
		if (count == 4) return true;
	}
	
	for (size_t row = 0; row < 4; ++row) {
		count = 0;
		for (size_t col = 0; col < 4; ++col) {
			if ((board[col][row] == player || board[col][row] == 'T')) {
				++count;
			} else {
				break;
			}
		}
		if (count == 4) return true;
	}
			
	count = 0;
	for (size_t row = 0; row < 4; ++row) {
		if ((board[row][row] == player || board[row][row] == 'T')) {
			++count;
		} else {
			break;
		}
	}
	if (count == 4) return true;

	if ((board[0][3] == player || board[0][3] == 'T') && (board[1][2] == player || board[1][2] == 'T') &&
		(board[2][1] == player || board[2][1] == 'T') && (board[3][0] == player || board[3][0] == 'T')) {
		return true;
	}
	return false;
}

int main()
{
	
	ifstream input_file;
	ofstream output_file; 
	
    input_file.open("input.txt");
    output_file.open("output.txt");
  
	size_t cases;
	input_file >> cases;
	
	int A;
	int B;
	
	string line;
	bool game_continue = false;

	
	for (size_t i = 1; i <= cases; ++i) {
		game_continue = false;
		for (size_t row = 0; row < 4; ++row) {
			for (size_t col = 0; col < 4; ++col) {
				input_file >> board[row][col];
				if (board[row][col] == '.') {
					game_continue = true;
				}
			}
		}
	
		if (is_player_won('X')) {
			output_file << "Case #" << i << ": " << "X won";
		} else if (is_player_won('O')) {
			output_file << "Case #" << i << ": " << "O won";
		} else if (game_continue) {
			output_file << "Case #" << i << ": " << "Game has not completed";
		} else {
			output_file << "Case #" << i << ": " << "Draw";
		}
		
		if (i != cases) {
			output_file << endl;
		}
	
			
	}				
	
    input_file.close();
    output_file.close();
	return 0;
}