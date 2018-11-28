#include <iostream>
using namespace std;

#define BOARD_SIZE 4
int main(){
    char board[BOARD_SIZE][BOARD_SIZE];
    int num_case;
    bool x_win, y_win, draw, incomplete;

    char ch;
    cin >> num_case;
    for(int k =1; k <=num_case; k++){
	x_win = y_win = draw = incomplete = 0;
	for(int i=0; i<BOARD_SIZE; i++){
	    for(int j=0; j<BOARD_SIZE; j++){
		cin >> ch;
		board[i][j] = ch;
	    }
	}
	int pt_x = 0;
	int pt_y = 0;
	for(int i=0; i<BOARD_SIZE; i++){
	    for(int j=0; j<BOARD_SIZE; j++){
		if(board[i][j]=='X') pt_x++;
		if(board[i][j]=='O') pt_y++;
		if(board[i][j] == 'T'){
		    pt_x++;
		    pt_y++;
		}	
	    }
	    if(pt_x == 4) x_win = 1;
	    if(pt_y == 4) y_win = 1;
	    pt_x = pt_y = 0;
	}
	
	for(int i=0; i< BOARD_SIZE; i++){
	    for(int j=0; j < BOARD_SIZE; j++){
		if(board[j][i] == 'X') pt_x++;
		if(board[j][i] == 'O') pt_y++;
		if(board[j][i] == 'T'){
		    pt_x++;
		    pt_y++;
		}
	    }
	    if(pt_x == 4) x_win = 1;
	    if(pt_y == 4) y_win = 1;
	    pt_x = pt_y = 0;
	}
	// done vertical and horizontal
	
	for(int i=0; i < BOARD_SIZE; i++){
	    if(board[i][i] == 'X') pt_x ++;
	    if(board[i][i] == 'O') pt_y ++;
	    if( board[i][i] == 'T'){
		pt_x++;
		pt_y++;
	    }
	}
	if(pt_x == 4) x_win = 1;
	if(pt_y == 4) y_win = 1;
	pt_x = pt_y = 0;
	
	for(int i=0; i < BOARD_SIZE; i++){
	    int j = BOARD_SIZE-i-1;
	    if(board[i][j]=='X') pt_x++;
	    if(board[i][j]=='O') pt_y++;
	    if(board[i][j] == 'T'){
		pt_x++; pt_y++;
	    }
	}
	if(pt_x==4) x_win = 1;
	if(pt_y==4) y_win = 1;
	pt_x = pt_y = 0;
	// done diagonal
	
	cout << "Case #" << k << ": ";
	if(x_win) cout << "X won " << endl;
	else if(y_win) cout << "O won" << endl;
	else{
	    for(int i=0; i < BOARD_SIZE; i++){
		for(int j=0; j < BOARD_SIZE; j++){
		    if(board[i][j] == '.') {
			incomplete = 1;
			break;
		    }
		}
	    }
	    if(incomplete) cout << "Game has not completed" << endl;
	    else cout << "Draw" << endl;
	}
    }
    
}
