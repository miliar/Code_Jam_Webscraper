#include <iostream>
using namespace std;

#define X 0
#define O 1

bool loadBoard(char b[][4]);
bool findRows(char b[][4], int &winner);
bool findCols(char b[][4], int &winner);
bool rightDiag(char b[][4], int &winner);
bool leftDiag(char b[][4], int &winner);

int main() {
   int n;
   char b[4][4];
   bool complete;
   bool done;
   int winner;

   cin >> n;
   for( int i=0; i<n; i++ ) {
      winner = 2;
      complete = loadBoard(b);
      done = findRows(b, winner);
      if(!done)
         done = findCols(b, winner);
      if(!done)
         done = rightDiag(b, winner);
      //cout <<"Done?:" <<  done << endl;
      if(!done)
         done = leftDiag(b, winner);
      
      cout << "Case #" << i+1 << ": ";
      if(!done && complete)
         cout << "Draw";
      else if(winner == 0)
         cout << "X won";
      else if(winner == 1)
         cout << "O won";
      else if(!done && !complete)
         cout << "Game has not completed";
      cout << endl;
         
   }
   return 0;
}

bool loadBoard(char b[][4]) {
   bool complete = true;
   for(int i=0; i<4; i++){
      for(int j=0; j<4; j++) {
         cin >> b[i][j];
         if(b[i][j] == '.')
            complete = false;
      }
   }
   return complete;
}

bool findCols(char b[][4], int &winner){
   bool done = false;
   int xCnt, oCnt;
   for(int j=0; j<4 && !done; j++) {
      xCnt=oCnt=0;
      for(int i=0; i<4; i++) {
         if(b[i][j] == 'X')
            xCnt++;
         else if(b[i][j] == 'O')
            oCnt++;
         else if(b[i][j] == 'T'){
            xCnt++;
            oCnt++;
         }
      }
      if(xCnt == 4 || oCnt == 4){
         done = true;
      }
   }
   if(xCnt == 4)
      winner = X;
   else if(oCnt == 4)
      winner = O;
   return done;
}

bool findRows(char b[][4], int &winner){
   bool done = false;
   int xCnt, oCnt;
   for(int i=0; i<4 && !done; i++) {
      xCnt=oCnt=0;
      for(int j=0; j<4; j++) {
         if(b[i][j] == 'X')
            xCnt++;
         else if(b[i][j] == 'O')
            oCnt++;
         else if(b[i][j] == 'T'){
            xCnt++;
            oCnt++;
         }
      }
      if(xCnt == 4 || oCnt == 4){
         done = true;
      }
   }
   if(xCnt == 4)
      winner = X;
   else if(oCnt == 4)
      winner = O;
   return done;

}
bool rightDiag(char b[][4], int &winner) {
   bool done = false;
   int xCnt = 0, oCnt=0;
   for(int i=0; i<4; i++) {
      if(b[i][i] == 'X')
         xCnt++;
      else if(b[i][i] == 'O')
         oCnt++;
      else if(b[i][i] == 'T') {
         xCnt++;
         oCnt++;
      }
   }
   //cout << xCnt << " " << oCnt << endl;
   if(xCnt == 4) {
      done = true;
      //cout << "IN IF - Done: " << done << endl;;
      winner = X;
   } else if(oCnt == 4) {
      done = true;
      winner = O;
   }
   return done;
}

bool leftDiag(char b[][4], int &winner){
   bool done = false;
   int xCnt=0, oCnt=0;
   for(int i=0; i<4; i++) {
      if(b[i][3-i] == 'X')
         xCnt++;
      else if(b[i][3-i] == 'O')
         oCnt++;
      else if(b[i][3-i] == 'T') {
         xCnt++;
         oCnt++;
      }
   }
   //cout << "DIAG: " << xCnt << " " << oCnt << endl;
   if(xCnt == 4) {
      done == true;
      winner = X;
   } else if(oCnt == 4) {
      done = true;
      winner = O;
   }
   return done;
}

