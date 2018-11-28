//
//  TicTacToeTomek.cpp
//  TicTacToeTomek
//
//  Created by Ahmed Mohammed Abdurahman on 4/13/13.
//  Copyright (c) 2013 Better MDM LLC. All rights reserved.
//

#include <cstdio>
#include <stdlib.h>
#include <fstream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;



int main(int argc, const char * argv[])
{

    if (argc < 3)
    {
        printf("Usage: %s <input file> <output file>\n", argv[0]);
        exit(1);
    }
    
    
    // open files
    ifstream fin(argv[1], ios::in|ios::ate);
    if (!fin.is_open())
    {
        printf("Unable to open input file\n");
        exit(1);
    }
    fin.seekg(0);
    
    ofstream fout(argv[2], ios::out|ios::ate);
    if (!fout.is_open())
    {
        printf("Unable to open output file\n");
        exit(1);
    }
    fout.seekp(0);
    
    
    
    
    uint64_t testcase_count;
    fin >> testcase_count;
    for (uint64_t tcase = 0; tcase < testcase_count; tcase++)
    {           // process each test case
        bool not_completed = false;
        
        // read input
        int board[4][4];        // 0 = empty, 1 = X, 2 = O, 3 = T
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                char ch;
                fin >> ch;
                
                switch (ch)
                {
                    case '.':
                        board[i][j] = 0;
                        not_completed = true;
                        break;
                    case 'X':
                        board[i][j] = 1;
                        break;
                    case 'O':
                        board[i][j] = 2;
                        break;
                    case 'T':
                        board[i][j] = 3;
                        break;
                    default:
                        j--;
                        break;
                }
            }
        }
        
    
        int winner = 0;    // 0 = none, 1 = X, 2 = O
        
        // check rows
        for (int i = 0; i < 4; i++)
        {
            int j = 0, temp = board[i][0];
            for (; j < 3; j++)
            {
                int cur = board[i][j], next = board[i][j+1];
                
                if (cur == 3)
                {
                    temp = next;
                    continue;
                }
                
                if (next == 3)
                {
                    temp = cur;
                    j++;
                    if (j < 3)
                    {
                        next = board[i][j+1];
                    }
                    else continue;
                }
                
                if (cur != next) break;
            }
            
            if ((j > 2) && temp)
            {
                winner = temp;
                goto case_done;
            }
        }
        
        // check columns
        for (int j = 0; j < 4; j++)
        {
            int i = 0, temp = board[0][j];
            for (; i < 3; i++)
            {
                int cur = board[i][j], next = board[i+1][j];
                
                if (cur == 3)
                {
                    temp = next;
                    continue;
                }
                
                if (next == 3)
                {
                    temp = cur;
                    i++;
                    if (i < 3)
                    {
                        next = board[i+1][j];
                    }
                    else continue;
                }
                
                if (cur != next) break;
            }
            
            if ((i > 2) && temp)
            {
                winner = temp;
                goto case_done;
            }
        }
        
        // check diagonal (UL)
        {
            int i = 0, temp  = board[0][0];
            for (; i < 3; i++)
            {
                int cur = board[i][i], next = board[i+1][i+1];
                
                if (cur == 3)
                {
                    temp = next;
                    continue;
                }
                
                if (next == 3)
                {
                    temp = cur;
                    i++;
                    if (i < 3)
                    {
                        next = board[i+1][i+1];
                    }
                    else continue;
                }
                
                if (cur != next) break;
            }
            
            if ((i > 2) && temp)
            {
                winner = temp;
                goto case_done;
            }
        }
        
        // check diagonal (UR)
        {
            int i = 0, temp  = board[0][3];
            for (; i < 3; i++)
            {
                int cur = board[i][3-i], next = board[i+1][2-i];
                if (cur == 3)
                {
                    temp = next;
                    continue;
                }
                
                if (next == 3)
                {
                    temp = cur;
                    i++;
                    if (i < 3)
                    {
                        next = board[i+1][2-i];
                    }
                    else continue;
                }
                
                if (cur != next) break;
            }
            
            if ((i > 2) && temp)
            {
                winner = temp;
                goto case_done;
            }
        }
        
    case_done:
        fout << "Case #" << (tcase + 1) << ": ";
        if (winner) fout << (winner == 1 ? "X" : "O") << " won" << endl;
        else if (not_completed) fout << "Game has not completed" << endl;
        else fout << "Draw" << endl;
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}

