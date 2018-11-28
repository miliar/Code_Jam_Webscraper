#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int TC;char board[4][4];
    cin>>TC;
    for (int tc=1;tc<=TC;tc++){
        for(int r=0;r<4;r++){
                cin>>board[r];
        }
        //For each row
        int X=0, O=0, T=0, won=0; bool dot =  false;
        for(int r=0;r<4;r++){
                X=O=T=0;
                for(int col=0;col<4;col++){
                        switch(board[r][col]){
                              case 'X' : X++; break;
                              case 'O' : O++; break;
                              case 'T' : T++; break;     
                              case '.' : dot = true; break;
                        }
                }
                if (X+T == 4){
                   won=1;break;}
                else if (O+T == 4){
                   won=2;break;}
        }
        if (won == 1){
           printf("Case #%d: X won\n", tc);continue;}
        else if (won == 2){
             printf("Case #%d: O won\n", tc);continue;}
        //For each column
        for(int c=0;c<4;c++){
                X=O=T=0;
                for(int row=0;row<4;row++){
                        switch(board[row][c]){
                              case 'X' : X++; break;
                              case 'O' : O++; break;
                              case 'T' : T++; break;     
                              case '.' : dot = true; break;
                        }
                }
                if (X+T == 4){
                   won=1;break;}
                else if (O+T == 4){
                   won=2;break;}
        }
        if (won == 1){
           printf("Case #%d: X won\n", tc);continue;}
        else if (won == 2){
             printf("Case #%d: O won\n", tc);continue;}
             
        //For each diagonal
        X=O=T=0;
        for(int r=0,c=0;r<4 && c<4;r++, c++){
                switch(board[r][c]){
                              case 'X' : X++; break;
                              case 'O' : O++; break;
                              case 'T' : T++; break;     
                              case '.' : dot = true; break;
                }
        }
        if (X+T==4){
           printf("Case #%d: X won\n", tc);continue;}
        else if (O+T==4){
             printf("Case #%d: O won\n", tc);continue;}
             
        X=O=T=0;
        for(int r=0,c=3;r<4 && c>=0;r++, c--){
                switch(board[r][c]){
                              case 'X' : X++; break;
                              case 'O' : O++; break;
                              case 'T' : T++; break;     
                              case '.' : dot = true; break;
                }
        }
        if (X+T==4){
           printf("Case #%d: X won\n", tc);continue;}
        else if (O+T==4){
             printf("Case #%d: O won\n", tc);continue;}
        
        //Draw if no dot else draw
        if (dot) printf("Case #%d: Game has not completed\n", tc);
        else printf("Case #%d: Draw\n", tc);
    }
}
