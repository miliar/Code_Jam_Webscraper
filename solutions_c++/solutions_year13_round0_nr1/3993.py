//============================================================================
// Name        : GoogleCodeJam.cpp
// Author      : Luis Eduardo Oliveira Lizardo
// Version     :
// Copyright   :
// Description : Problem A. Tic-Tac-Toe-Tomek
//============================================================================

#include <iostream>
#include <stdio.h>
using namespace std;

#define SIZE 4

int main() {

	int T;
	char c;

	scanf("%d%*c", &T);

	for (int t = 1; t <= T; ++t) {

		if(t > 1)
			scanf("%*c");

		int column[SIZE];
		int line[SIZE];
		int diagUL = 0;
		int diagUR = 0;

		bool columnT[SIZE];
		bool lineT[SIZE];

		bool isFinished = true;

		for (int i = 0; i < SIZE; ++i) {
			column[i] = 0;
			line[i] = 0;

			columnT[i] = false;
			lineT[i] = false;
		}

		for (int i = 0; i < SIZE; ++i) {
			for (int j = 0; j < SIZE; ++j) {
				scanf("%c", &c);

				if(c == 'X'){
					column[j] ++;
					line[i] ++;
					if (i == j) diagUL ++;
					if (i == SIZE-1-j) diagUR ++;
				}
				else if(c == 'O'){
					column[j] --;
					line[i] --;
					if (i == j) diagUL --;
					if (i == SIZE-1-j) diagUR --;
				}
				else if(c == 'T'){
					columnT[j] = true;
					lineT[i] = true;
				}
				else {
					isFinished = false;
				}
			}
			scanf("%*c");
		}


		bool winner = false;
		int resDiagUL = 4;
		int resDiagUR = 4;

		for (int i = 0; i < SIZE; ++i) {

			int resColumn = 4;
			if(columnT[i] == true){
				resColumn = 3;
			}

			int resLine = 4;
			if(lineT[i] == true){
				resLine = 3;
			}

			if(lineT[i] == true && columnT[i] == true){
				resDiagUL = 3;
			}

			if(lineT[i] == true && columnT[SIZE-1-i] == true){
				resDiagUR = 3;
			}

			if(column[i] == resColumn || line[i] == resLine) {
				printf("Case #%d: X won\n", t);
				winner = true;
				break;
			} else if (column[i] == resColumn*(-1) || line[i] == resLine*(-1)) {
				printf("Case #%d: O won\n", t);
				winner = true;
				break;
			}
		}

		if (winner == false ) {

			if (diagUL == resDiagUL || diagUR == resDiagUR) {
				printf("Case #%d: X won\n", t);

			} else if (diagUL == resDiagUL*(-1) || diagUR == resDiagUR*(-1)) {
				printf("Case #%d: O won\n", t);

			} else if (isFinished == true){
				printf("Case #%d: Draw\n", t);

			} else {
				printf("Case #%d: Game has not completed\n", t);
			}
		}

	}

	return 0;
}


/*
1
XXXT
....
OO..
....

1
XXXX
XXXX
XXTX
XXXX

1
O.X.
O.X.
O.X.
X.O.

1
OOOO
.OOO
.T.O
OOOO

1
X...
.O..
..T.
...O
 */
