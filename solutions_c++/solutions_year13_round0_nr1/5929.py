#include <stdio.h>
#include <vector>

using namespace std;

int checkRow(vector< vector <int> > board, int row) {

	int result = 0;
	int j = 0;

	result = 1;
	j = 0;
	while (j < 4) {
		if (board[row][j] != 1 && board[row][j] != 3)
			result = 0;
		j++;
	}

	if (result == 0) {
		result = 2;
		j = 0;
		while (j < 4) {
			if (board[row][j] != 2 && board[row][j] != 3)
                        	result = 0;
			j++;
		}
	}
	
	return result;
}

int checkCol(vector< vector <int> > board, int col) {

        int result = 0;
        int j = 0;

        result = 1;
        j = 0;
        while (j < 4) {
                if (board[j][col] != 1 && board[j][col] != 3)
                        result = 0;
		j++;
        }

        if (result == 0) {
                result = 2;
                j = 0;
                while (j < 4) {
                        if (board[j][col] != 2 && board[j][col] != 3)
                                result = 0;
			j++;
                }
        }

        return result;
}

int checkDiag(vector< vector <int> > board) {

        int result = 0;
        int j = 0;

        result = 1;
        j = 0;
        while (j < 4) {
                if (board[j][j] != 1 && board[j][j] != 3)
                        result = 0;
		j++;
        }

        if (result == 0) {
                result = 2;
                j = 0;
                while (j < 4) {
                        if (board[j][j] != 2 && board[j][j] != 3)
                                result = 0;
			j++;
                }
        }

	if (result == 0) {
		result = 1;
		if (board[0][3] != 1 && board[0][3] != 3)
			result = 0;
		if (board[1][2] != 1 && board[1][2] != 3)
                        result = 0;
		if (board[2][1] != 1 && board[2][1] != 3)
                        result = 0;
		if (board[3][0] != 1 && board[3][0] != 3)
                        result = 0;
	}

	if (result == 0) {
		result = 2;
		if (board[0][3] != 2 && board[0][3] != 3)
                        result = 0;
                if (board[1][2] != 2 && board[1][2] != 3)
                        result = 0;
                if (board[2][1] != 2 && board[2][1] != 3)
                        result = 0;
                if (board[3][0] != 2 && board[3][0] != 3)
                        result = 0;
	}

        return result;
}


int main() 
{
	int tests, result;
	char ch;
	int flag;

	scanf("%d\n", &tests);	

	vector< vector<int> > board(4, vector<int> (4));


	for (int i = 1; i <= tests; i++) {
		flag = 0;
		for (int j = 0; j < 4; j++) {
		    for (int k = 0; k < 4; k++) {
			ch = getchar();
			if (ch == 'X')
				board[j][k] = 1;
			else if (ch == 'O')
				board[j][k] = 2;
			else if (ch == 'T')
				board[j][k] = 3;
			else { 
				board[j][k] = 0; 
				flag = 1; 
			}
		    }
		    ch = getchar();
		}
		ch = getchar();
		int j = 0;
		result = 0;
		while ((j < 4) && (result == 0)) {
			result = checkRow(board, j);
			j++;
		}
		if (result == 0) {
			int j = 0;
                	while ((j < 4) && (result == 0)) {
                        	result = checkCol(board, j);
				j++;
                	}
			if (result == 0) {
				result = checkDiag(board);
				if (result == 0) {
					if (flag == 0) 
						printf("Case #%d: Draw\n", i);
					else printf("Case #%d: Game has not completed\n", i);
				}
				else printf("Case #%d: %c won\n", i, (result==1) ? 'X' : 'O');
			}
			else printf("Case #%d: %c won\n", i, (result==1) ? 'X' : 'O');
		}	
		else
			printf("Case #%d: %c won\n", i, (result==1) ? 'X' : 'O');
	}
	return 0;
}
