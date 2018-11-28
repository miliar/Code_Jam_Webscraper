/*
 *  Tic_Tac_Toe_Tomek.cpp
 *  Google_Jam
 *
 *  Created by Hugo Manet on 13/04/13.
 *  Copyright 2013. All rights reserved.
 *
 */

/*  
 *  So much particular cases => I use goto ! :p
 */

#include <iostream>

using namespace std;

enum State { empty = '.', toX = 'X', toO = 'O', toBoth = 'T' };

State board[4][4];

void readBoard()
{
    for (int line = 0; line < 4; line++)
    {
        cin >> skipws;
        for (int col = 0; col < 4; col++)
            cin >> (char&) board[line][col];
    }
}

bool hasWon(State player)
{
    for (int line = 0; line < 4; line++)
    {
        for (int col = 0; col < 4; col++)
            if (board[line][col] != player && board[line][col] != toBoth)
                goto nextLine;
        
        return true;
        
    nextLine:    // I think it's clearer this way.
        ;
    }
    
    for (int col = 0; col < 4; col++)
    {
        for (int line = 0; line < 4; line++)
            if (board[line][col] != player && board[line][col] != toBoth)
                goto nextCol;
        
        return true;
        
    nextCol:    // I would use "continue", but it isn't available in the inner loop.
        ;
    }
    
    for (int diagoIdx = 0; diagoIdx < 4; diagoIdx++)
        if (board[diagoIdx][diagoIdx] != player && board[diagoIdx][diagoIdx] != toBoth)
            goto nextDiago;
    
    return true;
    
nextDiago:
    
    for (int diagoIdx = 0; diagoIdx < 4; diagoIdx++)
        if (board[diagoIdx][3 - diagoIdx] != player && board[diagoIdx][3 - diagoIdx] != toBoth)
            return false;
    
    return true;
}

void solveOne(int numTest)
{
    readBoard();
    
    cout << "Case #" << numTest << ": ";
    
    if (hasWon(toX))
        cout << "X won\n";
    else if (hasWon(toO))
        cout << "O won\n";
    else
    {
        for (int line = 0; line < 4; line++)
            for (int col = 0; col < 4; col++)
                if (board[line][col] == empty)
                    goto notCompleted;
    
        cout << "Draw\n";
        return;
        
    notCompleted:
        cout << "Game has not completed\n";
    }
}

int main()
{
    int  nbTest;
    cin>>nbTest;
    
    for (int numTest = 1; numTest <= nbTest; numTest++)
        solveOne(numTest);
}
