#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#pragma comment (linker, "/STACK:256000000")

using namespace std;
char table[4][4];
const char* players="XO";
const char  TAW = 'T';

void printWinner(int test, const char player)
{
    cout << "Case #" << test << ": " << player << " won" << endl; 
}

void solveTicTacToe(int test)
{
    bool bCouldBeDraw = true;

    // Read the table
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
        {
           cin >> table[i][j];
           if (table[i][j] == '.')
           {
               bCouldBeDraw = false;
           }
        }

    // Check for solution on lines/columns
    for (int i = 0; i < 4; i++)  
        for (int playerIndex = 0; playerIndex < 2; playerIndex++)       
            if ((table[i][0] == players[playerIndex] || table[i][0] == TAW) && 
                (table[i][1] == players[playerIndex] || table[i][1] == TAW) && 
                (table[i][2] == players[playerIndex] || table[i][2] == TAW) && 
                (table[i][3] == players[playerIndex] || table[i][3] == TAW))
            {
                // line winner
                printWinner(test, players[playerIndex]);
                return;
            }
            else if ((table[0][i] == players[playerIndex] || table[0][i] == TAW) && 
                     (table[1][i] == players[playerIndex] || table[1][i] == TAW) && 
                     (table[2][i] == players[playerIndex] || table[2][i] == TAW) && 
                     (table[3][i] == players[playerIndex] || table[3][i] == TAW))
            {
                // column winner
                printWinner(test, players[playerIndex]);
                return;
            }
       
    // Check solution on diagonals
    for (int playerIndex = 0; playerIndex < 2; playerIndex++) 
        if ((table[0][0] == players[playerIndex] || table[0][0] == TAW) && 
            (table[1][1] == players[playerIndex] || table[1][1] == TAW) && 
            (table[2][2] == players[playerIndex] || table[2][2] == TAW) && 
            (table[3][3] == players[playerIndex] || table[3][3] == TAW))
        {
            printWinner(test, players[playerIndex]);
            return;
        }
        else if ((table[0][3] == players[playerIndex] || table[0][3] == TAW) && 
                 (table[1][2] == players[playerIndex] || table[1][2] == TAW) && 
                 (table[2][1] == players[playerIndex] || table[2][1] == TAW) && 
                 (table[3][0] == players[playerIndex] || table[3][0] == TAW))
        {
            printWinner(test, players[playerIndex]);
            return;
        }

    // No winner
    if (bCouldBeDraw) 
    {
        cout << "Case #" << test << ": Draw" << endl; 
    }
    else
    {
        cout << "Case #" << test << ": Game has not completed" << endl;
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests = 0;
    scanf("%d", &tests);
    for (int i = 1; i <= tests; i++)
        solveTicTacToe(i);

    return 0;
}