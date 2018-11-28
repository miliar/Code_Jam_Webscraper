#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int T, K, N;
    string tempS;
    char tempC;
    vector<vector< int > > board, newBoard;
    vector<int> tempLine;

    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    fin >> T;
    for ( int i = 0; i < T; i++ )
    {
        board.clear();
        newBoard.clear();

        fin >> N >> K;

        tempLine.resize(N,0);


        for ( int j = 0; j < N; j++ )
        {
            board.push_back(tempLine);
            newBoard.push_back(tempLine);

            fin >> tempS;

            for ( int k = 0; k < N; k++ )
            {
                tempC = tempS[k];
                if ( tempC == '.')
                    board[j][k] = 0;
                if ( tempC == 'R')
                    board[j][k] = 1;
                if ( tempC == 'B')
                    board[j][k] = 2;
            }
        }

        /*for ( int j = 0; j < board.size(); j++ )
        {
            for ( int k = 0; k < board[j].size(); k++ )
            {
                cout << board[j][k] << " ";
            }
            cout << endl;
        }*/
        int currPos;
        for ( int j = 0; j < N; j++ )   //rows of old
        {
            currPos = N-1;  //curr pos in the nwe board
            for ( int k = N-1; k >= 0; k-- )   //cols of old
            {
                if ( board[j][k] != 0 )
                {
                    newBoard[currPos][N-1-j] = board[j][k];
                    currPos --;
                }
            }
        }
/*
        for ( int j = 0; j < newBoard.size(); j++ )
        {
            for ( int k = 0; k < newBoard[j].size(); k++ )
            {
                cout << newBoard[j][k] << " ";
            }
            cout << endl;
        }*/

        //find things
        //find horiz
        bool redWin=false, blueWin = false;

        int currCount = 0;
        for ( int j = 0; j < N-K+1; j++ )
        {
            for ( int k = 0; k < N; k++ )
            {
                currCount = 0;
                for ( int l = 0; l < K; l++ )
                {
                    if ( newBoard[j+l][k] == 1)
                        currCount++;
                }
                if (currCount == K)
                    redWin=true;
            }
        }
        for ( int j = 0; j < N-K+1; j++ )
        {
            for ( int k = 0; k < N; k++ )
            {
                currCount = 0;
                for ( int l = 0; l < K; l++ )
                {
                    if ( newBoard[j+l][k] == 2)
                        currCount++;
                }
                if (currCount == K)
                    blueWin=true;
            }
        }

        //vertical
        for ( int j = 0; j < N-K+1; j++ )
        {
            for ( int k = 0; k < N; k++ )
            {
                currCount = 0;
                for ( int l = 0; l < K; l++ )
                {
                    if ( newBoard[k][j+l] == 2)
                        currCount++;
                }
                if (currCount == K)
                    blueWin=true;
            }
        }
        for ( int j = 0; j < N-K+1; j++ )
        {
            for ( int k = 0; k < N; k++ )
            {
                currCount = 0;
                for ( int l = 0; l < K; l++ )
                {
                    if ( newBoard[k][j+l] == 1)
                        currCount++;
                }
                if (currCount == K)
                    redWin=true;
            }
        }
//==============================================================================================================
        //diagonals:

        for ( int j = 0; j < N-K+1; j++ )
        {
            for ( int k = 0; k < N-K+1; k++ )
            {
                currCount = 0;
                for ( int l = 0; l < K; l++ )
                {
                    if ( newBoard[k+l][j+l] == 2)
                        currCount++;
                }
                if (currCount == K)
                    blueWin=true;
            }
        }
        for ( int j = 0; j < N-K+1; j++ )
        {
            for ( int k = 0; k < N-K+1; k++ )
            {
                currCount = 0;
                for ( int l = 0; l < K; l++ )
                {
                    if ( newBoard[k+l][j+l] == 1)
                        currCount++;
                }
                if (currCount == K)
                    redWin=true;
            }
        }

        for ( int j = K-1; j < N; j++ )
        {
            for ( int k = 0; k < N-K+1; k++ )
            {
                currCount = 0;
                for ( int l = 0; l < K; l++ )
                {
                    if ( newBoard[k+l][j-l] == 2)
                        currCount++;
                }
                if (currCount == K)
                    blueWin=true;
            }
        }

        for ( int j = K-1; j < N; j++ )
        {
            for ( int k = 0; k < N-K+1; k++ )
            {
                currCount = 0;
                for ( int l = 0; l < K; l++ )
                {
                    if ( newBoard[k+l][j-l] == 1)
                        currCount++;
                }
                if (currCount == K)
                    redWin=true;
            }
        }


        fout << "Case #" << i+1 << ": ";
        if ( redWin)
        {
            if(blueWin)
                fout <<"Both" << endl;
            else
                fout << "Red" << endl;
        }
        else
        {
            if(blueWin)
                fout <<"Blue" << endl;
            else
                fout << "Neither" << endl;
        }


    }
    return 0;
}
