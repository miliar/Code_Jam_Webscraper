//
//  main.cpp
//  QualifsTicTacToe
//
//  Created by MrAaaah on 12/04/13.
//  Copyright (c) 2013 MrAaaah. All rights reserved.
//

#include <iostream>
using namespace std;

bool hasWon(int board)
{
    int y = board & (board >> 4);
    if (y & (y >> 2 * 4)) // check \ diagonal
        return true;
    y = board & (board >> 5);
    if (y & (y >> 2 * 5)) // check horizontal
        return true;
    y = board & (board >> 6);
    if (y & (y >> 2 * 6)) // check / diagonal
        return true;
    y = board & (board >> 1);
    if (y & (y >> 2))     // check vertical
        return true;
    return false;
}

int indexToBitboard(int i) {
    return (1 << ((i%4) * 5 + (3 - i / 4)));
}

int main(int argc, const char * argv[])
{
    int cases, boardO, boardX;
    bool O, X, ended;
    char p;
    
	cin >> cases;
    
	for (long c = 1; c <= cases; ++c)
	{
        O = false; X = false; boardO = 0; boardX = 0; ended = true;
        
        for (int i = 0; i < 16; ++i) {
            cin >> p;

            if (p == 'X') {
                boardX |= indexToBitboard(i);
            }
            else if (p == 'O') {
                boardO |= indexToBitboard(i);
            }
            else if (p == 'T') {
                boardX |= indexToBitboard(i);
                boardO |= indexToBitboard(i);
            }
            else {
                ended = false;
            }

            O = hasWon(boardO);
            X = hasWon(boardX);
        }
        
        cout << "Case #" << c << ": ";
        
        if (O && X) {
            cout << "Draw";
        }
        else if (O) {
            cout << "O won";
        }
        else if (X) {
            cout << "X won";
        }
        else if (!ended){
            cout << "Game has not completed";
        }
        else {
            cout << "Draw";
        }
        
        cout << endl;
	}

    return 0;
}

