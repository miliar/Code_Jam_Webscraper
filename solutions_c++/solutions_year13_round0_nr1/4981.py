#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

string tic[4];
string res[4] = {"X won",
                 "O won",
                 "Draw",
                 "Game has not completed"};

bool isPlayerWon(char P){
  bool f = 1;
  int tCnt = 0;

  for(int i = 0; i < 4; i++){
    f = 1;
    tCnt = 0;
    for(int j = 0; j < 4 && f; j++){
      if(!(tic[i][j] == P || tic[i][j] == 'T'))
        f = 0;
      if(tic[i][j] == 'T')
        tCnt++;
    }
    if(f && tCnt <= 1) return 1;

    f = 1;
    tCnt = 0;
    for(int j = 0; j < 4 && f; j++){
      if(!(tic[j][i] == P || tic[j][i] == 'T'))
        f = 0;
      if(tic[j][i] == 'T')
        tCnt++;
    }
    if(f && tCnt <= 1) return 1;
  }

  f = 1;
  tCnt = 0;
  for(int i = 0; i < 4 && f; i++){
    if(!(tic[i][i] == P || tic[i][i] == 'T'))
      f = 0;
    if(tic[i][i] == 'T')
      tCnt++;
  }
  if(f && tCnt <= 1)
    return 1;

  
  f = 1;
  tCnt = 0;
  for(int i = 0; i < 4 && f; i++){
    if(!(tic[i][3 - i] == P || tic[i][3 - i] == 'T'))
      f = 0;
    if(tic[i][3 - i] == 'T')
      tCnt++;
  }
  if(f && tCnt <= 1)
    return 1;
  return  0;
}

// 0:X won, 1:O won, 2: Draw, 3: Game has...
int ans(){
  if(isPlayerWon('X')) return 0;
  if(isPlayerWon('O')) return 1;
  int cnt = 0;
  for(int i = 0; i < 4; i++)
    for(int j = 0; j < 4; j++)
      if(tic[i][j] == '.')
        cnt++;
  if(cnt) return 3;
  return 2;
}


int main(){
  int t;
  cin >> t;

  for(int i = 0; i < t; i++){
    for(int j = 0; j < 4; j++)
      cin >> tic[j];

    cout << "Case #" << i + 1 << ": " << res[ans()] << endl;
  }
  return 0;
}
