#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

int main(int argc, char ** argv){
    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    int numberOfTest;

    inFile >> numberOfTest;

    char charTemp;

    int * board;

    board = new int[16];

    bool boardFull;
    int gameEnd;

    int temp;
    int temp2;

    string result;

    for(int count = 0 ; numberOfTest > count ; count++){
	boardFull   = true;
	gameEnd	= 0;
	for(int count2 = 0 ; 16  > count2 ; count2++){
	    inFile >> charTemp;
	    switch(charTemp){
		case 'X' :
		    board[count2] = 1;
		    break;
		case 'O' :
		    board[count2] = -1;
		    break;
		case 'T' :
		    board[count2] = 10;
		    break;
		case '.' :
		    board[count2] = 0;
		    boardFull   = false;
		    break;
	    }
	}


	for(int count2 = 0 ; 4 > count2 ; count2++){
	    temp	= 0;
	    temp2	= 0;
	    for(int count3 = 0 ; 4 > count3 ; count3++){
		temp += board[count2 * 4 + count3];
		temp2 += board[count2 + count3 * 4];
	    }
#define CHECK_GAME_STATUS   \
	    if((4 == temp) || (13 == temp) || (4 == temp2) || (13 == temp2)){	\
		if(gameEnd == 2){	\
		    result = "Draw";	\
		}else if(0 == gameEnd){	\
		    result =  "X won";	\
		    gameEnd = 1;	\
		}   \
	    }	\
	    if((-4 == temp) || (7 == temp) || (-4 == temp2) || (7 == temp2)){	\
		if(gameEnd == 1){	\
		    result = "Draw";	\
		}else if(0 == gameEnd){	\
		    result = "O won";	\
		    gameEnd = 2;	\
		}	\
	    }
	    CHECK_GAME_STATUS
	}

	temp = board[0] + board[5] + board[10] + board[15];
	temp2 = board[3] + board[6] + board[9] + board[12];
	CHECK_GAME_STATUS

	    if(0 == gameEnd){
		if(boardFull)
		    result = "Draw";
		else
		    result = "Game has not completed";
	    }

	outFile << "Case #" << count + 1 << ": " << result << endl;

    }
    delete board;
    return EXIT_SUCCESS;
}
