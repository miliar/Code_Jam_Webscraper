#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <fstream>
using namespace std;

// Function Prototypes
int numberOfPiecesOnBoard(const vector<string>& board);
bool winHorizontal(const vector<string>& board, char player); 
bool winVertical(const vector<string>& board, char player);
bool winDiagonal(const vector<string>& board, char player);
/** END FUNCTION PROTOTYPES **/

// Function to count the number of pieces on the board:
int numberOfPiecesOnBoard(const vector<string>& board) {
	int temp = 0;

	for(int i = 0; i < 4; i++) {
		string nextRow = board[i];
		for(int j = 0; j < 4; j++) {
			if(nextRow[j] != '.') {
				temp++;
			}
		}
	}

	return temp;
}

// Function to check for a horizontal win:
bool winHorizontal(const vector<string>& board, char player) {

	bool didWin = false;

	for(unsigned int i = 0; i < 4; i++) {
		string nextRow = board[i];
		
		if( ((nextRow[0] == player) && (nextRow[1] == player) && (nextRow[2] == player) && (nextRow[3] == player)) ||
			((nextRow[0] == 'T') && (nextRow[1] == player) && (nextRow[2] == player) && (nextRow[3] == player)) ||
			((nextRow[0] == player) && (nextRow[1] == 'T') && (nextRow[2] == player) && (nextRow[3] == player)) ||
			((nextRow[0] == player) && (nextRow[1] == player) && (nextRow[2] == 'T') && (nextRow[3] == player)) ||
			((nextRow[0] == player) && (nextRow[1] == player) && (nextRow[2] == player) && (nextRow[3] == 'T'))) {

			didWin = true;
			break;
		}
	}

	return didWin;

} /** END FUNCTION winHorizontal **/

// Function to check for a vertical win:
bool winVertical(const vector<string>& board, char player) {
	
	bool didWin = false;
	
	string firstRow = board[0];
	string secondRow = board[1];
	string thirdRow = board[2];
	string fourthRow = board[3];

	for(int col = 0; col < 4; col++) {
				
		if( ((firstRow[col] == player) && (secondRow[col] == player) && (thirdRow[col] == player) && (fourthRow[col] == player)) ||
			((firstRow[col] == 'T') && (secondRow[col] == player) && (thirdRow[col] == player) && (fourthRow[col] == player)) ||
			((firstRow[col] == player) && (secondRow[col] == 'T') && (thirdRow[col] == player) && (fourthRow[col] == player)) ||
			((firstRow[col] == player) && (secondRow[col] == player) && (thirdRow[col] == 'T') && (fourthRow[col] == player)) ||
			((firstRow[col] == player) && (secondRow[col] == player) && (thirdRow[col] == player) && (fourthRow[col] == 'T'))) {

			didWin = true;
			break;
		}

	}


	return didWin;

} /** END FUNCTION winVertical **/

// Function to check for a diagonal win:
bool winDiagonal(const vector<string>& board, char player) {

	bool didWin = false;

	string firstRow = board[0];
	string secondRow = board[1];
	string thirdRow = board[2];
	string fourthRow = board[3];

	// Check main diagonal:
	if( ((firstRow[0] == player) && (secondRow[1] == player) && (thirdRow[2] == player) && (fourthRow[3] == player)) ||
		((firstRow[0] == 'T') && (secondRow[1] == player) && (thirdRow[2] == player) && (fourthRow[3] == player)) ||
		((firstRow[0] == player) && (secondRow[1] == 'T') && (thirdRow[2] == player) && (fourthRow[3] == player)) ||
		((firstRow[0] == player) && (secondRow[1] == player) && (thirdRow[2] == 'T') && (fourthRow[3] == player)) ||
		((firstRow[0] == player) && (secondRow[1] == player) && (thirdRow[2] == player) && (fourthRow[3] == 'T'))) {
		
		didWin = true;
	}
	// Check for anti diagonal: 
	else if( ((firstRow[3] == player) && (secondRow[2] == player) && (thirdRow[1] == player) && (fourthRow[0] == player)) ||
			 ((firstRow[3] == 'T') && (secondRow[2] == player) && (thirdRow[1] == player) && (fourthRow[0] == player)) ||
 			 ((firstRow[3] == player) && (secondRow[2] == 'T') && (thirdRow[1] == player) && (fourthRow[0] == player)) ||
			 ((firstRow[3] == player) && (secondRow[2] == player) && (thirdRow[1] == 'T') && (fourthRow[0] == player)) ||
			 ((firstRow[3] == player) && (secondRow[2] == player) && (thirdRow[1] == player) && (fourthRow[0] == 'T'))) {

		didWin = true;
	}
			

	return didWin;

} /** END FUNCTION winDiagonal **/

int main(int argc, char* argv[]) {
	
	// Variable to determine if the first line has been read:
	bool firstLineRead = false;

	if(argc != 2) {
		cout << "Usage: ./tictactoe <filename>" << endl;
		exit(1);
	}

	// String to hold the file name:
	string fileName = argv[1]; 

	// File stream for the text file:
	ifstream myfile;
	myfile.open(argv[1]);

	// 2 dimensional 4 x 4 vector to hold the boards:
	vector<vector<string> > boards;

	// Variable to hold the number of test cases:
	int numberOfTestCases;

	// Read in the data:
	string nextLine;
	while(myfile >> nextLine) {

		vector<string> currentBoard;

		// If the first line hasn't been read, do so: 
		if(!firstLineRead) {
			numberOfTestCases = atoi(nextLine.c_str());
			//cout << "Number of test cases is: " << numberOfTestCases << endl;
			firstLineRead = true;
		} else {
			string firstLine = nextLine;
			//cout << "firstLine is " << firstLine << endl;
			myfile >> nextLine;
			string secondLine = nextLine;
			//cout << "secondLine is " << secondLine << endl;
			myfile >> nextLine;
			string thirdLine = nextLine;
			//cout << "thirdLine is " << thirdLine << endl;
			myfile >> nextLine;
			string fourthLine = nextLine;
			//cout << "fourthLine is " << fourthLine << endl;
			// Ignore the space:
			//myfile >> nextLine;

			// Add the strings to the board:
			currentBoard.push_back(firstLine);
			currentBoard.push_back(secondLine);
			currentBoard.push_back(thirdLine);
			currentBoard.push_back(fourthLine);

			// Add this currentBoard to boards:
			boards.push_back(currentBoard);
		}

		/*
		// DEBUG ONLY - Print out the board:
		for(unsigned int i = 0; i < currentBoard.size(); i++) {
			cout << currentBoard[i] << endl;
		}*/

		
	}
	// Good policy to close the file:
	myfile.close();

	//cout << "boards' size is: " << boards.size() << endl << endl;
	ofstream results;
	results.open("results1.txt");

	// Go through the boards vector, find the result:
	for(int i = 0; i < numberOfTestCases; i++) {
		// Get the next board:
		vector<string> nextBoard = boards[i];

		// DEBUG ONLY
		for(unsigned int j = 0; j < nextBoard.size(); j++) {
			cout << nextBoard[j] << endl;
		}

		// DEBUG ONLY
		//cout << "NOW TRYING TO GET THE NUMBER OF PIECES" << endl;
		// Get the number of pieces:
		int numPieces = numberOfPiecesOnBoard(nextBoard);
		//cout << "SUCCESSFULLY GOT THE NUMBER OF PIECES" << endl;
		
		// DEBUG ONLY
		//cout << "number of pieces on this board is: " << numPieces << endl;	

		// Check if player x won:
		if(winHorizontal(nextBoard, 'X') || winVertical(nextBoard, 'X') || winDiagonal(nextBoard, 'X')) {
			results << "Case #" << i+1 << ": X won" << endl;
		} else if(winHorizontal(nextBoard, 'O') || winVertical(nextBoard, 'O') || winDiagonal(nextBoard, 'O')) {
			results << "Case #" << i+1 << ": O won" << endl;
		} else if(numPieces == 16) {
			results << "Case #" << i+1 << ": Draw" << endl;
		} else {
			results << "Case #" << i+1 << ": Game has not completed" << endl;
		}
	}	
	results.close();
	
	return 0;
}
