#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <string>
#include <algorithm>
#include <deque>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <set>
using namespace std;
int board[100][100];
int w,h,r;
void improve(int y, int x, int score){
  if(y>=h)return;
  if(x>=w)return;
  if(board[y][x] == -1)return;
  board[y][x] += score;
  board[y][x] %= 10007;
  return;
}
int main(){
  int cases;
  cin >> cases;
  int temp = 0;
  while(cases--){
    cout << "Case #" << ++temp << ": ";
    cin >> h >> w >> r;
    /*if(temp==72)cout << "y:" << h << " " << "x:" <<w  << "r:" << r << endl; 
      if(temp==72)sleep(1);*/
    for(int i=0;i<h;i++){
      for(int j=0;j<w;j++){
	board[i][j] = 0;
      }
    }
    board[0][0] = 1;
    
    for(int i=0;i<r;i++){
      int y, x;
      cin >> y >> x;
      //   if(temp==72)cout << "y:" << y << " " << "x:" <<x << endl;
      board[y-1][x-1] = -1;
    }
    for(int i=0;i<h;i++){
      for(int j=0;j<w;j++){
	if(board[i][j] != -1){
	  improve(i+1,j+2, board[i][j]);
	  improve(i+2,j+1, board[i][j]);
	}
      }
    }
    cout << board[h-1][w-1] % 10007 << endl;
    
  }
  return 0;
}
