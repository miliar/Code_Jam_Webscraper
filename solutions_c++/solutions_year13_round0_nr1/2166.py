#include<iostream>
#include<string>
using namespace std;

#include<fstream>
ifstream fin ("A-large.in");
ofstream fout ("out.txt");
#define cin fin 
#define cout fout

int main (){
  int t;
  cin>>t;
  int t_pos_x = -1;
  int t_pos_y = -1;
  string board [5];
  char winner = '0';
  int completed = 1;
  for (int num_t = 0; num_t < t;++num_t){
    winner = '0';
    t_pos_x = t_pos_y = -1;
    completed = 1;

    for (int i=0;i<4;++i){
      cin>>board[i];
      for (int j=0;j<4;++j){
	if (board[i][j] == 'T'){t_pos_x = i;t_pos_y = j;}
	if (board[i][j] == '.')completed = 0;
      }
    }

    if (t_pos_x != -1)board[t_pos_x][t_pos_y] = 'O';
    for (int i=0;i<4;++i){
      if ((board[i][0] == board[i][1])&&(board[i][2] == board[i][1])&&(board[i][3] == board[i][1])){if (board[i][0] != '.')winner = board[i][0];}
    }
    for (int i=0;i<4;++i){
      if ((board[0][i] == board[1][i])&&(board[2][i] == board[1][i])&&(board[3][i] == board[1][i])){if (board[0][i] != '.')winner = board[0][i];}
    }
    if ((board[0][0] == board[1][1])&&(board[2][2] == board[1][1])&&(board[3][3] == board[1][1])){if (board[0][0] != '.')winner = board[0][0];}
    if ((board[0][3] == board[1][2])&&(board[0][3] == board[2][1])&&(board[0][3] == board[3][0])){if (board[0][3] != '.')winner = board[0][3];}

    if (t_pos_x != -1)board[t_pos_x][t_pos_y] = 'X';
    for (int i=0;i<4;++i){
      if ((board[i][0] == board[i][1])&&(board[i][2] == board[i][1])&&(board[i][3] == board[i][1])){if (board[i][0] != '.')winner = board[i][0];}
    }
    for (int i=0;i<4;++i){
      if ((board[0][i] == board[1][i])&&(board[2][i] == board[1][i])&&(board[3][i] == board[1][i])){if (board[0][i] != '.')winner = board[0][i];}
    }
    if ((board[0][0] == board[1][1])&&(board[2][2] == board[1][1])&&(board[3][3] == board[1][1])){if (board[0][0] != '.')winner = board[0][0];}
    if ((board[0][3] == board[1][2])&&(board[0][3] == board[2][1])&&(board[0][3] == board[3][0])){if (board[0][3] != '.')winner = board[0][3];}

    if (winner != '0'){
      cout<<"Case #"<<num_t+1 <<": "<<winner<<" won\n";
    }
    else {
      if (completed == 0)
	cout<<"Case #"<<num_t+1 <<": Game has not completed\n";
      else 
	cout<<"Case #"<<num_t+1 <<": Draw\n";
    }
  }
  return 0;
}
