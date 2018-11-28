#include <iostream>
#include <cstdio>

using namespace std;

int t;
int cases =1;
char map[4][4];

int main(){
  scanf("%d ",&t);
  while(t--){
    bool complete = true;
    char winner='c';
    bool won = false;
    for(int i=0;i<4;i++) for(int j=0;j<4;j++){
      scanf("%c ",&map[i][j]);
      if(map[i][j]=='.') complete = false;
    }
    //rows
    for(int i=0;i<4;i++){
      int p =0;
      char c = map[i][p];
      if(c=='.') continue;
      while(c=='T'){
        if(c=='.') break;
        p++;
        c=map[i][p];
      }
      p++;
      while(p<4){
        if(c==map[i][p]||map[i][p]=='T') p++; else break;
      }
      if(p==4&&c!='.'){
        won = true;
        winner = c;
      }
    }
    //column
    for(int i=0;i<4;i++){
      int p =0;
      char c = map[p][i];
      if(c=='.') continue;
      while(c=='T'){
        if(c=='.') break;
        p++;
        c=map[p][i];
      }
      p++;
      while(p<4){
        if(c==map[p][i]||map[p][i]=='T') p++; else break;
      }
      if(p==4&&c!='.'){
        won = true;
        winner = c;
      }
    }
    //2 diagonals
    {
      int p =0;
      char c = map[p][p];
      while(c=='T'){
        if(c=='.') break;
        p++;
        c=map[p][p];
      }
      p++;
      while(p<4){
        if(c==map[p][p]||map[p][p]=='T') p++; else break;
      }
      if(p==4&&c!='.'){
        won = true;
        winner = c;
      }
    }
    {
      int p =0;
      char c = map[p][3-p];
      while(c=='T'){
        if(c=='.') break;
        p++;
        c=map[p][3-p];
      }
      p++;
      while(p<4){
        if(c==map[p][3-p]||map[p][3-p]=='T') p++; else break;
      }
      if(p==4&&c!='.'){
        won = true;
        winner = c;
      }
    }
    if(won){
      printf("Case #%d: %c won\n",cases,winner);
    }else if(complete){
      printf("Case #%d: Draw\n",cases);
    }else{
      printf("Case #%d: Game has not completed\n",cases);
    }cases ++;
  }

  return 0;
}
