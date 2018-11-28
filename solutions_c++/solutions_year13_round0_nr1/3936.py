#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int main() {
 const int s=4;
 char board[s][s];
 bool dots;
 bool over;
 int xsq;
 int osq;

 int ntc;
 scanf("%d\n",&ntc);
 for(int tc=0;tc<ntc;tc++) {
   dots=false;
   over=false;
   xsq=0;
   osq=0;

   //read the board
   for(int i=0;i<s;i++) {
     for(int j=0;j<s;j++) {
       scanf("%c",&board[i][j]);
       if(!dots && board[i][j]=='.') {
         dots=true; // at least 1 empty square
       }
     }
     scanf("\n");
   }

   //check if game over
   for(int i=0;i<s;i++) {
     // horizontal
     if((board[i][0]=='X' || board[i][0]=='T') && (board[i][1]=='X' || board[i][1]=='T')) {
       xsq=2;
       osq=0;
       for(int j=2;j<=3;j++) {
         if(board[i][j]=='X' || board[i][j]=='T') xsq++;
       }
       if(xsq==4) {
         over=true;
         break;
       }
     } 
     if((board[i][0]=='O' || board[i][0]=='T') && (board[i][1]=='O' || board[i][1]=='T')) {
       xsq=0;
       osq=2;
       for(int j=2;j<=3;j++) {
         if(board[i][j]=='O' || board[i][j]=='T') osq++;
       }
       if(osq==4) {
         over=true;
         break;
       }
     }
     // vertical
     if((board[0][i]=='X' || board[0][i]=='T') && (board[1][i]=='X' || board[1][i]=='T')) {
       xsq=2;
       osq=0;
       for(int j=2;j<=3;j++) {
         if(board[j][i]=='X' || board[j][i]=='T') xsq++;
       }
       if(xsq==4) {
         over=true;
         break;
       }
     } 
     if((board[0][i]=='O' || board[0][i]=='T') && (board[1][i]=='O' || board[1][i]=='T')) {
       xsq=0;
       osq=2;
       for(int j=2;j<=3;j++) {
         if(board[j][i]=='O' || board[j][i]=='T') osq++;
       }
       if(osq==4) {
         over=true;
         break;
       }
     }
   }
   if(!over) {
     // diagonal
     if( (board[0][0]=='X' || board[0][0]=='T') && (board[1][1]=='X' || board[1][1]=='T') && (board[2][2]=='X' || board[2][2]=='T') && (board[3][3]=='X' || board[3][3]=='T')) {
       xsq=4;
       osq=0;
       over=true;
     } else if( (board[0][3]=='X' || board[0][3]=='T') && (board[1][2]=='X' || board[1][2]=='T') && (board[2][1]=='X' || board[2][1]=='T') && (board[3][0]=='X' || board[3][0]=='T')) {
       xsq=4;
       osq=0;
       over=true;
     } else if( (board[0][0]=='O' || board[0][0]=='T') && (board[1][1]=='O' || board[1][1]=='T') && (board[2][2]=='O' || board[2][2]=='T') && (board[3][3]=='O' || board[3][3]=='T')) {
       osq=4;
       xsq=0;
       over=true;
     } else if( (board[0][3]=='O' || board[0][3]=='T') && (board[1][2]=='O' || board[1][2]=='T') && (board[2][1]=='O' || board[2][1]=='T') && (board[3][0]=='O' || board[3][0]=='T')) {
       osq=4;
       xsq=0;
       over=true;
     }
   }
   printf("Case #%d: ",tc+1);
   if(over) {
     if(xsq==4) printf("X won\n");
     else printf("O won\n");
   } else {
     if(dots) printf("Game has not completed\n");
     else printf("Draw\n");
   }

   scanf("\n");
 }
 return 0;
}
