#include <iostream>
#include <fstream>
using namespace std;/*
XOXT
XXOO
OXOX
XXOO
     */
char check_win(string board[4],char player, bool second_player){
     for (int rows=0;rows<4;rows++){
         if ((board[rows][0]==player || board[0][0]=='T') && (board[rows][1]==player || board[rows][1]=='T') && (board[rows][2]==player || board[rows][2]=='T') && (board[rows][3]==player || board[rows][3]=='T') ){return player;}
     }
     for (int columns=0;columns<4;columns++){
         if ((board[0][columns]==player || board[0][columns]=='T') && (board[1][columns]==player || board[1][columns]=='T') && (board[2][columns]==player || board[2][columns]=='T') && (board[3][columns]==player || board[3][columns]=='T') ){return player;}
     }

     if ((board[0][0]==player || board[0][0]=='T') && (board[1][1]==player || board[1][1]=='T') && (board[2][2]==player || board[2][2]=='T') && (board[3][3]==player || board[3][3]=='T') ){return player;}
     if ((board[0][3]==player || board[0][3]=='T') && (board[1][2]==player || board[1][2]=='T') && (board[2][1]==player || board[2][1]=='T') && (board[3][0]==player || board[3][0]=='T') ){return player;}

if (second_player==false){
   return check_win(board,'O',true);                          
}

  for (int i=0;i<4;i++){
      for (int j=0;j<4;j++){
          if (board[i][j]=='.'){return 'N';}
          }
      }
      return 'D';
}

int main(){
    std::ifstream in("code jam tateti.txt");
    std::ofstream out("code jam tateti salida.txt");
int a,b,c,d,e,f,i,quantity;
string str;
in>>    quantity;
for( i=0;i<quantity;i++){
        string board[4];        
        for (int j=0;j<4;j++){
            in>>board[j];
        }        
char result=check_win(board,'X',false);
switch (result){
       case 'X':
            out << "Case #"<<(i+1)<<": X won\n";
       break;
       case 'O':
            out << "Case #"<<(i+1)<<": O won\n";
       break;
       case 'D':
            out << "Case #"<<(i+1)<<": Draw\n";
       break;
       case 'N':
            out << "Case #"<<(i+1)<<": Game has not completed\n";
       break;
       }


}

//system("pause");
    
    
    }
