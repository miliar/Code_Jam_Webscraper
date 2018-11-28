#include <iostream>

#define SIZE 4

enum tile {
    EMPTY = 0, T, X, O, INVALID
};

int main(int argc, char *argv[])
{
    tile board[SIZE][SIZE];
    int numTests;
    
    char rep[INVALID]; 
    rep[EMPTY] = '.';
    rep[T] = 'T';
    rep[X] = 'X';
    rep[O] = 'O';   
    rep[INVALID] = '\0';

    std::cin >> numTests;

    for (int t = 1; t <= numTests; t++) {
	tile winner = EMPTY;
	std::cout << "Case #" << t << ": ";

	// Fill in board
	int numEmpty = SIZE * SIZE;
	for (int x = 0; x < SIZE; x++) {
	    //std::cout << std::endl;
	    for (int y = 0; y < SIZE; y++) {
		board[x][y] = INVALID;
		// Loop over chars until a proper one comes up
		while (board[x][y] == INVALID) {
		    char c;
		    std::cin >> c;
		    // Check for validity
		    for (int i = EMPTY; i < INVALID; i++) {
			if (rep[i] == c) {
			    board[x][y] = (tile) i;
			    if (i != EMPTY) {
				numEmpty--;
			    }
			    //std::cout << rep[i];
			    break;
			}
		    }
		    // OH THE NESTING!!
		}
	    }
	}
	
/**
	std::cout << std::endl;	
	for (int x = 0; x < SIZE; x++) {
	    for (int y = 0; y < SIZE; y++) {
		std::cout << rep[board[x][y]];
	    }
	    std::cout << std::endl;
	}
*/

	// Now check for wins.
	// Rows
	for (int x = 0; x < SIZE; x++) {
	    int count[4] = {0, 0, 0, 0};
	    for (int y = 0; y < SIZE; y++) {
	        count[board[x][y]]++;
	    }
	    if (count[X] + count[T] == SIZE) {
		std::cout << "X won";
		winner = X;
	    }
	    if (count[O] + count[T] == SIZE) {
		std::cout << "O won";
		winner = O;
	    }
	}

	// Columns
	if (winner == EMPTY) {
	    for (int y = 0; y < SIZE; y++) {
		int count[4] = {0, 0, 0, 0};
		for (int x = 0; x < SIZE; x++) {
		    count[board[x][y]]++;
		}
		if (count[X] + count[T] == SIZE) {
		    std::cout << "X won";
		    winner = X;
		}
		if (count[O] + count[T] == SIZE) {
		    std::cout << "O won";
		    winner = O;
		}
	    }
	}
	
	// Diagonals
	if (winner == EMPTY) {
	    int count[4] = {0, 0, 0, 0};
	    for (int d = 0; d < SIZE; d++) {
		count[board[d][d]]++;
	    }
	    if (count[X] + count[T] == SIZE) {
		std::cout << "X won";
		winner = X;
	    }
	    if (count[O] + count[T] == SIZE) {
		std::cout << "O won";
		winner = O;
	    }
	}
						
	// Other diagonal
	if (winner == EMPTY) {
	    int count[4] = {0, 0, 0, 0};
	    for (int d = 0; d < SIZE; d++) {
		count[board[d][SIZE - (d+1)]]++;
	    }
	    if (count[X] + count[T] == SIZE) {
		std::cout << "X won";
		winner = X;
	    }
	    if (count[O] + count[T] == SIZE) {
		std::cout << "O won";
		winner = O;
	    }
	}

	if (winner == EMPTY) {
	    if (numEmpty == 0) {
		std::cout << "Draw";
	    } else {
		std::cout << "Game has not completed";
	    }
	}

	std::cout << std::endl;
    }
}
