// main.cpp
//
//  Tic-Tac-Toe-Tomek
//
//     -- Google Code Jam -- Problem A
//
//  By: Victor Grzeda
//
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define COLSIZE 4
#define ROWSIZE 4

void boardClear( char board[ROWSIZE][COLSIZE] );
void boardClear( int board[ROWSIZE][COLSIZE] );
int boardWinner( int board[ROWSIZE][COLSIZE] );

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        cout << "Usage: \n" << argv[0] << "<input file>" << endl;
        return 1;
    }

    //Open input file
    ifstream inputFile;
    ofstream outputFile;
    inputFile.open(argv[1], ifstream::in);
    outputFile.open("results.out", ofstream::out);

    if ( !inputFile.is_open() ) {
        cout << "Could not open file" << endl;
        return 1;
    }

    //Variables
    int tests;
    int count = 1;
    int emptyCnt;
    int resultFlag;

    char board[ROWSIZE][COLSIZE];
    int numBoard[ROWSIZE][COLSIZE];
    boardClear( board );


    inputFile >> tests;

    cout << tests << endl;

    while( count <= tests )
    {
        emptyCnt = 0;
        for( unsigned int r=0; r < ROWSIZE; r++ )
        {
            for( unsigned int c=0; c < COLSIZE; c++ )
            {
                inputFile >> board[r][c];
                if ( board[r][c] == 'X' ) {
                    numBoard[r][c] = 1;
                } else if ( board[r][c] == 'O' ) {
                    numBoard[r][c] = 3;
                } else if ( board[r][c] == 'T' ) {
                    numBoard[r][c] = 2;
                } else if ( board[r][c] == '.' ) {
                    numBoard[r][c] = -10;
                    emptyCnt++;
                }
            }
        }

        cout << endl;
        //Print
        for( unsigned int r=0; r < ROWSIZE; r++ )
        {
            for( unsigned int c=0; c < COLSIZE; c++ )
            {
                cout << board[r][c];
            }
            cout << endl;
        }

        /* Determine the Board Winner
        *   1-> X won | 2-> O won | 0-> No Winner
        */
        resultFlag = boardWinner( numBoard );

        if ( resultFlag == 1 ) {

            cout << "Case #" << count << ": X won" << endl;
            outputFile << "Case #" << count << ": X won" << endl;

        } else if ( resultFlag == 2 ) {

            cout << "Case #" << count << ": O won" << endl;
            outputFile << "Case #" << count << ": O won" << endl;

        } else {
            if ( emptyCnt == 0 ) {

                cout << "Case #" << count << ": Draw" << endl;
                outputFile << "Case #" << count << ": Draw" << endl;

            } else {

                cout << "Case #" << count << ": Game has not completed" << endl;
                outputFile << "Case #" << count << ": Game has not completed" << endl;

            }
        }


        //boardClear( board );
        boardClear( numBoard );
        count++;
    }

    inputFile.close();
    outputFile.close();


    return 0;
}

void boardClear( char board[ROWSIZE][COLSIZE] )
{
    for( unsigned int r=0; r < ROWSIZE; r++ )
    {
        for( unsigned int c=0; c < COLSIZE; c++ )
        {
            board[r][c] = 0;
        }
    }

    return;
}
void boardClear( int board[ROWSIZE][COLSIZE] )
{
    for( unsigned int r=0; r < ROWSIZE; r++ )
    {
        for( unsigned int c=0; c < COLSIZE; c++ )
        {
            board[r][c] = 0;
        }
    }

    return;
}


int boardWinner( int board[ROWSIZE][COLSIZE] )
{
    //Variables
    int flag = 0;  // 1-> X won | 2-> O won | 0-> No Winner
    int sum = 0;

    int rowSums[10];

    //Horizontal
    rowSums[0] = board[0][0] + board[0][1] + board[0][2] + board[0][3];
    rowSums[1] = board[1][0] + board[1][1] + board[1][2] + board[1][3];
    rowSums[2] = board[2][0] + board[2][1] + board[2][2] + board[2][3];
    rowSums[3] = board[3][0] + board[3][1] + board[3][2] + board[3][3];

    //Vertical
    rowSums[4] = board[0][0] + board[1][0] + board[2][0] + board[3][0];
    rowSums[5] = board[0][1] + board[1][1] + board[2][1] + board[3][1];
    rowSums[6] = board[0][2] + board[1][2] + board[2][2] + board[3][2];
    rowSums[7] = board[0][3] + board[1][3] + board[2][3] + board[3][3];

    //Diagonal
    rowSums[8] = board[0][0] + board[1][1] + board[2][2] + board[3][3];
    rowSums[9] = board[3][0] + board[2][1] + board[1][2] + board[0][3];

    for( unsigned int i=0; i < 10; i++ )
    {
        sum = rowSums[i];

        if ( (sum == 4) || (sum == 5) ) {
            flag = 1;
            break;
        } else if ( (sum == 11) || (sum == 12) ) {
            flag = 2;
        }
    }

    return flag;
}

