#include <cstdio>

using namespace std;


bool checkColumn(int c, char board[4][4], char player)
{
    if (   (board[0][c] == player || board[0][c] == 'T') 
        && (board[1][c] == player || board[1][c] == 'T')
        && (board[2][c] == player || board[2][c] == 'T')
        && (board[3][c] == player || board[3][c] == 'T'))
    {
        return true;
    }
    return false;
}

bool checkRow(int c, char board[4][4], char player)
{
    if (   (board[c][0] == player || board[c][0] == 'T')
        && (board[c][1] == player || board[c][1] == 'T')
        && (board[c][2] == player || board[c][2] == 'T')
        && (board[c][3] == player || board[c][3] == 'T'))
    {
        return true;
    }
    return false;
}

int checkDiagonal(char board[4][4])
{
    if (  (board[0][0] == 'X' || board[0][0] == 'T')
        &&(board[1][1] == 'X' || board[1][1] == 'T')
        &&(board[2][2] == 'X' || board[2][2] == 'T')
        &&(board[3][3] == 'X' || board[3][3] == 'T'))
    {return 1;}
    else  if (  
          (board[0][0] == 'O' || board[0][0] == 'T')
        &&(board[1][1] == 'O' || board[1][1] == 'T')
        &&(board[2][2] == 'O' || board[2][2] == 'T')
        &&(board[3][3] == 'O' || board[3][3] == 'T'))
    {return 2;}

    else if (  
          (board[0][3] == 'O' || board[0][3] == 'T')
        &&(board[1][2] == 'O' || board[1][2] == 'T')
        &&(board[2][1] == 'O' || board[2][1] == 'T')
        &&(board[3][0] == 'O' || board[3][0] == 'T'))
    {return 2;}

    else if (  
          (board[0][3] == 'X' || board[0][3] == 'T')
        &&(board[1][2] == 'X' || board[1][2] == 'T')
        &&(board[2][1] == 'X' || board[2][1] == 'T')
        &&(board[3][0] == 'X' || board[3][0] == 'T'))
    {return 1;}
    else
        return -1;
}

bool checkIsDotPresent(char board[4][4])
{
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (board[i][j] == '.')
                return true;
        }
    }
    return false;
}

int solve(char board[4][4])
{
    int j = 0;

    // check all columns for X
    for (int i = 0; i < 4; i++) {
       if (checkColumn(i, board, 'X') ) 
           return 1;
    }
    
    // check all columns for Y
    for (int i = 0; i < 4; i++) {
       if (checkColumn(i, board, 'O') )
           return 2;
    }

    // check all rows for X
    for (int i = 0; i < 4; i++) {
       if (checkRow(i, board, 'X') )
           return 1;
    }

    // check all rows for Y
    for (int i = 0; i < 4; i++) {
       if (checkRow(i, board, 'O') )
           return 2;
    }

    int ret = checkDiagonal(board);
    if (ret != -1)
        return ret;

    if ( !checkIsDotPresent(board) )
        return 3; // draw
    else 
        return 4; // game continuing.

	return 1;
}

char* printResult(int state)
{
    if (state == 1)
        return "X won";
    if (state == 2)
        return "O won";
    else if (state == 3)
        return "Draw";
    else if (state == 4) 
        return "Game has not completed";    
    else return "error";
}

int main()
{
    FILE *fp = fopen("A-large.in", "r");  
    char board[4][4];

	int testcase;
    fscanf(fp, "%d\n", &testcase);

	for (int caseId = 1; caseId <= testcase; caseId++)
	{
        for (int i = 0; i < 4; i++) 
        {
            fscanf(fp, "%c", &board[i][0]);
            fscanf(fp, "%c", &board[i][1]);
            fscanf(fp, "%c", &board[i][2]);
            fscanf(fp, "%c", &board[i][3]);
            fscanf(fp, "\n"); // new line
        }        

		printf("Case #%d: %s\n", caseId, printResult(solve(board)));

        fscanf(fp, "\n");
        fscanf(fp, "\n");
	}
	return 0;
}