#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;

int main ()
{
    int t, i;
    
    freopen ("A-small.in","r",stdin);
    freopen ("A-small.out","w",stdout);
    
    scanf ("%d\n",&t);
    
    char board[4][4];
    
    for (int trial = 1; trial <= t; trial++)
    {
        for (i=0;i<4;++i)
            scanf ("%c%c%c%c\n", &board[i][0],&board[i][1],&board[i][2],&board[i][3]);
    
    
        char winning_character = '.';
        
        //Scan every row to see if there is a winner    
        for (int row=0; row<4; ++row)
        {
            char first = board[row][0];
            bool winner = true;
            for (int col=1; col<4; ++col)
            {
                if (board[row][col] != first and board[row][col]!= 'T')
                {
                   winner = false;
                   break;                    
                }    
            }   
            if (winner)
            {
               winning_character = first;
               break;           
            } 
        }
        
        if (winning_character != '.')
        {
           printf     ("Case #%d: %c won\n", trial, winning_character);             
        }
        else
        {
            //Scan every column
            for (int col=0; col<4; ++col)
            {
                char first = board[0][col];
                bool winner = true;
                for (int row=1; row<4; ++row)
                {
                    if (board[row][col] != first and board[row][col]!= 'T')
                    {
                       winner = false;
                       break;                    
                    }    
                }   
                if (winner)
                {
                   winning_character = first;
                   break;           
                } 
             }   
             if (winning_character != '.')
             {
                   printf     ("Case #%d: %c won\n", trial, winning_character);               
             }
             else
             {
                   //Check diagonals
                   char first = board[0][0];
                   bool winner = true;
                   for (i=1;i<4;++i)
                   {
                       if (board[i][i]!=first and board[i][i]!='T')
                       {
                          winner = false; break;                       
                       }    
                   }
                   if (winner and first!='.')
                   {
                          printf     ("Case #%d: %c won\n", trial, first);        
                   }
                   else
                   {             
                        first = board[0][3];
                        winner = true;
                        for (i=1;i<4;++i)
                        {
                            if (board[i][4-i-1]!=first and board[i][4-i-1]!='T')
                            {
                               winner = false; break;                           
                            }    
                        }
                        if (winner and first!='.')
                        {
                                  printf     ("Case #%d: %c won\n", trial, first);        
                        }
                        else
                        {
                           //Check if grid is full
                           bool full = true;
                           for (i=0;i<4;++i)
                           {
                               for (int j=0;j<4;++j)
                               {
                                   if (board[i][j]=='.')
                                   {
                                      full = false;
                                      break;                     
                                   }
                               }
                           }  
                           if (full)
                           {
                               printf     ("Case #%d: Draw\n", trial);   
                           }  
                           else
                           {
                               printf     ("Case #%d: Game has not completed\n", trial);  
                           }
                        }
                 }
             }
        }
    }
    return 0;   
}
