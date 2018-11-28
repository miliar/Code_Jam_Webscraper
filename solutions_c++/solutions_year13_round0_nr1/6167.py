//
//  TicTacToe.cpp
//  Tic-Tac-Toe-Tomek
//
//  Created by Matthew Wein on 4/13/13.
//  Copyright (c) 2013 Matthew Wein. All rights reserved.
//

#include "TicTacToe.h"

bool CTicTacToe::IsComplete()
{
    for (int i = 0; i < 4; i++ )
    {
        for (int j = 0; j < 4; j++)
        {
            if(m_board[i][j] == '.')
            {
                return false;
            }
        }
    }
    return true;
}

bool CTicTacToe::PlayerWon(char player)
{
    // check rows
    for (int i = 0; i < 4; i++ )
    {
        bool win = true;
        
        for (int j = 0; j < 4; j++)
        {
            if(m_board[i][j] != player && m_board[i][j] != m_wild_card)
            {
                win = false;
            }
        }
        if (win)
        {
            return true;
        }
    }
    
    // check columns
    for (int i = 0; i < 4; i++ )
    {
        bool win = true;
        
        for (int j = 0; j < 4; j++)
        {
            if(m_board[j][i] != player && m_board[j][i] != m_wild_card)
            {
                win = false;
            }
        }
        if (win)
        {
            return true;
        }
    }
    
    // check diagonals
    for (int i = 0; i < 2; i++)
    {
        bool win = true;
        
        for (int j = 0; j < 4; j++ )
        {
            int c = i == 0 ? j : 3 - j;
            if (m_board[j][c] != player && m_board[j][c] != m_wild_card)
            {
                win = false;
            }
        }
        if (win)
        {
            return true;
        }
    }
    
    return false;
}