#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;
char board[4][4];
bool full;
bool prov (char c, int x, int y)
{
        int counter = 0;
        for(int B = 0 ; B < 4 ; B++)
        {
                if(board[x][B] == 'T' || board[x][B] == c) counter++;
        }
         if(counter == 4) return true;
         counter = 0;
        for(int row = 0 ; row < 4 ; row++)
        {
                if(board[row][y] == 'T' || board[row][y] == c) counter++;
        }
        if(counter == 4) return true;
        counter = 0;
        if(x+y == 3)
        {
                for(int i = 0 ; i < 4 ; i++)
                {
                        for(int j = 0 ; j < 4 ; j++)
                        {
                                if(i+j == 3)
                                {
                                        if(board[i][j] == 'T' || board[i][j] == c) counter++;
                                }
                        }
                }
                if(counter == 4) return true;
                counter = 0;
        }
 
        if(x == y)
        {
                for(int i = 0 ; i < 4 ; i++)
                {
                        for(int j = 0 ; j < 4 ; j++)
                        {
                                if(!(i-j))
                                {
                                        if(board[i][j] == 'T' || board[i][j] == c) counter++;
                                }
                        }
                }
                if(counter == 4) return true;
                counter = 0;
        }
        return false;
}
int main()
{
        int test, counter = 1;
        scanf("%d", &test);
        while(test--)
        {
                memset(board, 0, sizeof(board));
                 for(int i = 0 ; i < 4 ; i++)
                {
                        scanf("%s", board[i]);
                }
 
                string winner = "Draw";
                full = true;
                for(int i = 0 ; i < 4 ; i++)
                {
                        for(int j = 0 ; j < 4 ; j++)
                        {
                                if(board[i][j] == '.') full = false;
                                else if(board[i][j] == 'X' || board[i][j] == 'O')
                                {
                                        bool iswin = prov(board[i][j], i, j);
                                        if(iswin)
                                        {
                                                winner = "";
                                                  winner += board[i][j];
                                                break;
                                        }
                                }
                        }
                }
 
                printf("Case #%d: ", counter++);
 
                if(winner == "X" || winner == "O") printf("%s won\n", winner.c_str());
                else if(winner == "Draw")
                {
                        if(full) puts("Draw");
                        else puts("Game has not completed");
                }
        }
        return 0;
}