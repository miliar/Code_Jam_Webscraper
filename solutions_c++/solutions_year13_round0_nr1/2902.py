#include <iostream> //Standard input/output
#include <fstream> //File input/output
#include <cstdlib> //C library
#include <cmath> //Math library
#include <algorithm> //Some algorithms like sorting
#include <vector> //Vectors (Array lists)
#include <string> //Strings

using namespace std; //Used the standard class

ifstream fin ("tictactoe.in");
ofstream fout ("tictactoe.out");

int main ()
{
   int T;
   fin >> T;
   for(int cas = 1; cas<=T; cas++){
      char board[16];
      int count = 0;
      //cout << cas << endl;
      for(int i = 0; i<16; i++){
         fin >> board[i];
         if(board[i]!='.') count++;
         //cout << board[i];
         //if(i%4==3) cout << endl;
      }
      int won = -1;
      for(int i = 0; i<16; i+=4){
         int O = 0, X = 0, T = 0;
         for(int j = 0; j<4; j++)
            switch(board[i+j]){
               case 'O':
                  O++;
                  break;
               case 'X':
                  X++;
                  break;
               case 'T':  
                  T++;
                  break;          
            }
         if(O==4 || O==3 && T==1){
            won = 0; 
            break;
         }
         if(X==4 || X==3 && T==1){
            won = 1; 
            break;
         }
      }   
      for(int i = 0; i<4; i++){
         int O = 0, X = 0, T = 0;
         for(int j = 0; j<16; j+=4)
            switch(board[i+j]){
               case 'O':
                  O++;
                  break;
               case 'X':
                  X++;
                  break;
               case 'T':  
                  T++;
                  break;          
            }
         if(O==4 || O==3 && T==1){
            won = 0; 
            break;
         }
         if(X==4 || X==3 && T==1){
            won = 1; 
            break;
         }
      }   
      int O = 0, X = 0, T = 0;
      for(int j = 0; j<16; j+=5)
         switch(board[j]){
            case 'O':
               O++;
               break;
            case 'X':
               X++;
               break;
            case 'T':  
               T++;
               break;          
         }
      if(O==4 || O==3 && T==1){
         won = 0; 
      }
      if(X==4 || X==3 && T==1){
         won = 1; 
      }
      O = 0; X = 0; T = 0;
      for(int j = 3; j<13; j+=3)
         switch(board[j]){
            case 'O':
               O++;
               break;
            case 'X':
               X++;
               break;
            case 'T':  
               T++;
               break;          
         }
      if(O==4 || O==3 && T==1){
         won = 0; 
      }
      if(X==4 || X==3 && T==1){
         won = 1; 
      }
      switch(won){
         case -1:
            if(count!=16) fout << "Case #" << cas << ": Game has not completed\n";
            else fout << "Case #" << cas << ": Draw\n";
            break;
         case 0: fout << "Case #" << cas << ": O won\n"; 
            break;
         case 1: fout << "Case #" << cas << ": X won\n"; 
            break;
      }
   }
   return 0;
}