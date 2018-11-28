#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;



int main(){
  
  char last_line[11]; //Last type on this line
  char win_line[11];  //Assume all lines win until: OH NOES!
  char sum_line[11];  //Turns spent in line
  char board[16];

  int N,i,j,empty,row,col,diag,inc=0;
  cin>>N;

  for(i=1,empty=0;N--;++i,inc=0){
    memset (&last_line, '@', sizeof(last_line));
    memset (&win_line, 1, sizeof(win_line));
    memset (&sum_line, 0, sizeof(sum_line));
    for(j=0;j<16;++j){
      cin>>board[j];

      row = j%4;
      col = (j/4)+4;
      diag = 10;            //Assume no diag
      if(j%3==0) diag = 9;
      if(j%5==0) diag = 8;


      if(board[j] == '.'){
        inc = 1;
        win_line[row] = 0;
        win_line[col] = 0;
        if(diag!=10) win_line[diag] = 0;
      }
;
      if(board[j] != '.'){
        sum_line[row]++;
        sum_line[col]++;
        if(diag!=10) sum_line[diag]++;
      }

      if(board[j] == 'T') continue;

      if(last_line[row] == '@') last_line[row] = board[j];
      if(last_line[col] == '@') last_line[col] = board[j];
      if(diag != 10 && last_line[diag] == '@') last_line[diag] = board[j];

      if(last_line[row] != board[j] && last_line[row] != 'T') win_line[row] = 0;
      if(last_line[col] != board[j] && last_line[col] != 'T') win_line[col] = 0;
      if(diag != 10 && last_line[diag] != board[j] && last_line[diag] != 'T') win_line[diag] = 0;
    }
    printf("Case #%d: ", i);
;
    for(j=0;j<10;++j){
      if(win_line[j]){
        printf("%c won\n", last_line[j]);
        break;
      }
    }
    if(inc && j==10) printf("Game has not completed\n");
    else if(!inc && j==10) printf("Draw\n");
  }
  return 0;
}
