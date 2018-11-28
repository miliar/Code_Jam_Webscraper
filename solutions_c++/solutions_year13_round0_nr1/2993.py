#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

char map[10][10];

void openFile(){
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
}

int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[8] = {1, 1, 0,-1,-1, -1,  0,  1};

bool in_map(int x, int y){
  if(0<=x && x <4 && 0<=y && y<4)return true;
  return false;
}


bool check_win(int x, int y, int d, char ch){
  for(int i = 0; i < 4; i++){
    if(i != 0){
      x += dx[d];
      y += dy[d];
    }
    if( in_map(x, y) && (map[x][y]==ch || map[x][y] == 'T')){
    }
    else return false;
  }
  return true;
}

int main(){
  openFile();
  int ncase;
  int n, c;
  int no = 0;
  cin >> ncase;
  gets(map[0]);
  while(ncase > no){
    no++;
    for(int i = 0; i < 4; i++){
      gets(map[i]);
      //puts(map[i]);
    }
    if(no != ncase)
      gets(map[4]);

    int i = 0;
    bool ret = false;
    for(i = 0; i < 4; i++){
      for(int j = 0; j < 4; j++){
        for(int k = 0; k < 8; k++){
          ret = check_win(i, j, k, 'X');
          if(ret){break;}
        }
        if(ret)break;
      }
      if(ret)break;
    }
    if(ret){ cout << "Case #" << no << ": X won" << endl;}
    else{
      int blank = 0;
      for(i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
          for(int k = 0; k < 8; k++){
            ret = check_win(i, j, k, 'O');
            if(map[i][j] == '.')blank++;
            if(ret){break;}
          }
          if(ret)break;
        }
        if(ret)break;
      }
      if(ret){ cout << "Case #" << no << ": O won" << endl;}
      else{
        if(blank > 0){cout << "Case #" << no << ": Game has not completed" << endl;}
        else {cout << "Case #" << no << ": Draw" << endl;}
      }
    }
  }
  return 0;
}
