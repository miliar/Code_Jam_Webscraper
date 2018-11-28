#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#define INF 1000000000000LL

typedef long long int64;
typedef unsigned long long qword;
using namespace std;

/* Problem: Google Code Jam Qualification Round 2013
 *          Problem A. Tic-Tac-Toe-Tomek
 * URL: https://code.google.com/codejam/contest/2270488/dashboard#s=p0
 */



int main() {
   int s,t,x,y,i,j;
   string board[5];
   int game[5][5];
   string empty;
   cin>>t;
   getline (cin,empty);
   for(s=1; s<=t; s++) {
      for (i=0; i<4; i++) {
         getline (cin,board[i]);
      }
      if (s != t){
         getline (cin,empty);
      }
      bool canDraw = true;
      for (i=0; i<4; i++) {
         for (j=0; j<4; j++) {
            //cout<<board[i][j];
            if (board[i][j] == 'X') {
               game[i][j] = 1;
            } else if (board[i][j] == 'O') {
               game[i][j] = -1;
            } else if (board[i][j] == 'T') {
               game[i][j] = 3;
            } else if (board[i][j] == '.') {
               game[i][j] = 0;
               canDraw = false;
            }
         }
         //cout<<endl;
      }
      int temp;
      int win = 0;
      /* 1: X win
       * -1: O win
       * 0: draw or Game not complete
       * */
      bool tIsPresent;
      for (i=0; i<4; i++) { //check row
         temp = 0;
         tIsPresent = false;
         for (j=0; j<4; j++) {
            if (game[i][j] == 3) {
               tIsPresent = true;
            } else {
               temp+=game[i][j];
            }
         }
         if (tIsPresent) {
            if (temp == 3) {
               win = 1;
            } else if (temp == -3) {
               win = -1;
            }
         } else {
            if (temp == 4) {
               win = 1;
            } else if (temp == -4) {
               win = -1;
            }
         }
      }
      for (i=0; i<4; i++) { //check column
         temp = 0;
         tIsPresent = false;
         for (j=0; j<4; j++) {
            if (game[j][i] == 3) {
               tIsPresent = true;
            } else {
               temp+=game[j][i];
            }
         }
         if (tIsPresent) {
            if (temp == 3) {
               win = 1;
            } else if (temp == -3) {
               win = -1;
            }
         } else {
            if (temp == 4) {
               win = 1;
            } else if (temp == -4) {
               win = -1;
            }
         }
      }
      //check diagonal 1
      temp = 0;
      for (i=0; i<4; i++) {
         tIsPresent = false;
         if (game[i][i] == 3) {
            tIsPresent = true;
         } else {
            temp+=game[i][i];
         }
      }
      if (tIsPresent) {
         if (temp == 3) {
            win = 1;
         } else if (temp == -3) {
            win = -1;
         }
      } else {
         if (temp == 4) {
            win = 1;
         } else if (temp == -4) {
            win = -1;
         }
      }
      //check diagonal 2
      temp = 0;
      for (i=0; i<4; i++) {
         tIsPresent = false;
         if (game[i][3-i] == 3) {
            tIsPresent = true;
         } else {
            temp+=game[i][3-i];
         }
      }
      if (tIsPresent) {
         if (temp == 3) {
            win = 1;
         } else if (temp == -3) {
            win = -1;
         }
      } else {
         if (temp == 4) {
            win = 1;
         } else if (temp == -4) {
            win = -1;
         }
      }
      
      cout<<"Case #"<<s<<": ";
      if (win == 1) {
         cout<<"X won";
      } else if (win == -1) {
         cout<<"O won";
      } else if (win == 0) {
         if (canDraw) {
            cout<<"Draw";
         } else {
            cout<<"Game has not completed";
         }
      }
      cout<<endl;
   }
   return 0;
}
