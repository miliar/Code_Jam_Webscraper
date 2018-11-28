#include<iostream>
#include<cstdlib>
#include<string>
using namespace std;
int main(void)
{
   int i,j,k;
   int T;
   (cin >> T).get();
   for(i=1;i<=T;i++){
      string input[4],s;
      short table[4][4];
      short symbol_r[2][4],symbol_c[2][4],symbol_x[2][2];
      bool Xwon=0,Owon=0,full=1;
      //
      for(j=0;j<4;j++){
         getline(cin,input[j]);
         for(k=0;k<4;k++){
            switch(input[j][k]){
               case '.':
                  table[j][k]=0;
                  full=0;
                  break;
               case 'X':
                  table[j][k]=1;
                  break;
               case 'O':
                  table[j][k]=2;
                  break;
               case 'T':
                  table[j][k]=3;
                  break;
               default:
                  ;
            }
         }
      }
      getline(cin,s);
      // table established
      for(j=0;j<4;j++){
         symbol_r[0][j]=0;
         symbol_r[1][j]=0;
         symbol_c[0][j]=0;
         symbol_c[1][j]=0;
      }
      for(j=0;j<4 && !Xwon;j++){
         for(k=0;k<4 && !Xwon;k++){
            switch(table[j][k]){
               case 1:
                  symbol_r[0][j]++;
                  break;
               case 2:
                  symbol_r[1][j]++;
                  break;
               case 3:
                  symbol_r[0][j]++;
                  symbol_r[1][j]++;
                  break;
               default:
                  ;
            }
            if(symbol_r[0][j]==4)
               Xwon=1;
            if(symbol_r[1][j]==4)
               Owon=1;
         }
      }
      for(k=0;k<4 && !Xwon;k++){
         for(j=0;j<4 && !Xwon;j++){
            switch(table[j][k]){
               case 1:
                  symbol_c[0][k]++;
                  break;
               case 2:
                  symbol_c[1][k]++;
                  break;
               case 3:
                  symbol_c[0][k]++;
                  symbol_c[1][k]++;
                  break;
               default:
                  ;
            }
            if(symbol_c[0][k]==4)
               Xwon=1;
            if(symbol_c[1][k]==4)
               Owon=1;
         }
      }
      for(j=0;j<2;j++){
         for(k=0;k<2;k++){
            symbol_x[j][k]=0;
         }
      }
      for(k=0;k<4 && !Xwon;k++){
         switch(table[k][k]){
            case 1:
               symbol_x[0][0]++;
               break;
            case 2:
               symbol_x[1][0]++;
               break;
            case 3:
               symbol_x[0][0]++;
               symbol_x[1][0]++;
               break;
            default:
               ;
         }
         switch(table[k][3-k]){
            case 1:
               symbol_x[0][1]++;
               break;
            case 2:
               symbol_x[1][1]++;
               break;
            case 3:
               symbol_x[0][1]++;
               symbol_x[1][1]++;
               break;
            default:
               ;
         }
         if(symbol_x[0][0]==4)
            Xwon=1;
         if(symbol_x[1][0]==4)
            Owon=1;
         if(symbol_x[0][1]==4)
            Xwon=1;
         if(symbol_x[1][1]==4)
            Owon=1;
      }
      
      //
      cout << "Case #" << i << ": ";
      if(Xwon)
         cout << "X won" << endl;
      else if(Owon)
         cout << "O won" << endl;
      else if(full)
         cout << "Draw" << endl;
      else
         cout << "Game has not completed" << endl;
   }
   return 0;
}
