#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;
#define DIM 4

/* Global variables */
char board[DIM][DIM];


/* prototypes */


int main(){
	int numCases;
	cin >> numCases;
	for(int caseN=1; caseN <= numCases; caseN++){
		for(int i=0; i<DIM; i++){
		for(int j=0; j<DIM; j++){
			cin >> board[i][j];
			
		}
		}	
		
/* print map
		for(int i=0; i<DIM; i++){
		for(int j=0; j<DIM; j++){
			cout << board[i][j];
			
		}
		cout << endl;
		}	
		cout << endl;
*/
		// now determine who won
		bool won = false;
		bool draw = true;
		char wonChar;

		// 1.1 horizontal

		for(int i=0; i<DIM; i++){
			if(board[i][0] == '.'){ continue;}
		for(int j=0; j< (DIM-1); j++){
			if((board[i][j] != board[i][j+1]) and (board[i][j] != 'T') and (board[i][j+1] != 'T')){
				break;
			} else {
				if(board[i][j] != 'T'){
					wonChar = board[i][j];
				} else {
					wonChar = board[i][j+1];
				}

				if( j == DIM -2 and wonChar != '.'){
					won = true;
					goto printCase;
				}
			}

		}
	
		}
		// if all matched		
		
endHorizontal:
		// won is still false here

		// 1.2 vertical

		for(int i=0; i<DIM; i++){
			if(board[0][i] == '.'){ continue;}
		for(int j=0; j< (DIM-1); j++){
			if((board[j][i] != board[j+1][i]) and (board[j][i] != 'T') and (board[j+1][i] != 'T')){
				break;
			} else {
				if(board[j][i] != 'T'){
					wonChar = board[j][i];
				} else {
					wonChar = board[j+1][i];
				}

				if( j == DIM -2 and wonChar!= '.'){
					won = true;
					goto printCase;
				}
			}

		}
	
		}

		// 1.3 diagonal /* / */
		for(int ii=0; ii< (DIM-1); ii++){
			if(board[ii][ii] != board[ii+1][ii+1] and board[ii][ii] != 'T' and board[ii+1][ii+1] != 'T'){
				goto endDiagonal;
			} else {
				if(board[ii][ii] != 'T'){
					wonChar = board[ii][ii];
				} else {
					wonChar = board[ii+1][ii+1];
				}
				if(wonChar == '.'){
					goto endDiagonal;
				}
			}
		}
		won = true;
		goto printCase;
endDiagonal:
		
		// 1.4 diagonal /* \ */
		for(int ii=0; ii< (DIM-1); ii++){
			if(board[DIM - ii-1][ii] != board[DIM - (ii +1)-1][ii+1] and board[DIM - ii-1][ii] != 'T' and board[DIM - (ii+1)-1][ii+1] != 'T'){
				goto endDiagonal2;
			} else {
				if(board[DIM-ii-1][ii] != 'T'){
					wonChar = board[DIM-ii-1][ii];
				} else {
					wonChar = board[DIM-(ii+1)-1][ii+1];
				}
				if(wonChar == '.'){
					goto endDiagonal2;
				}
			}
		}
		won = true;
		goto printCase;
endDiagonal2:

		
		// here check if the game still has .
		for(int i=0; i<DIM; i++){
		for(int j=0; j<DIM; j++){
			if(board[i][j] == '.'){
				draw = false;
				goto printCase;
			}
		}
		}


printCase:
		cout << "Case #" << caseN << ": ";
		if(won){
			cout << wonChar << " won";
		} else if(draw){
			// is it a draw or not completed
			cout << "Draw";
		} else {
			cout << "Game has not completed";
		}
		cout << endl;
	}
}
