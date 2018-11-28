#define _USE_MATH_DEFINES
#define INF 0x3f3f3f3f
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <limits>
#include <map>
#include <string>
#include <cstring>
#include <set>
#include <deque>
#include <bitset>
#include <list>
#include <cctype>
#include <utility>
 
using namespace std;
 
typedef long long ll;
typedef pair <int,int> P;
typedef pair <int,P > PP;
 
const int tx[] = {0,1,0,-1};
const int ty[] = {-1,0,1,0};

int col_search(char stage[4][4]);
int row_search(char stage[4][4]);
int diag_search(char stage[4][4]);

int search(char stage[4][4]){
  int flag = 0;
  flag |= col_search(stage);
  flag |= row_search(stage);
  flag |= diag_search(stage);
  
  return flag;
}

int col_search(char stage[4][4]){
  int res = 0; // 0:

  for(int y=0;y<4;y++){
    int t_num = 0;
    int x_num = 0;
    int o_num = 0;
    for(int x=0;x<4;x++){
      if(stage[y][x] == 'T') t_num++;
      if(stage[y][x] == 'X') x_num++;
      if(stage[y][x] == 'O') o_num++;
    }

    if(t_num >= 2) continue;

    if(t_num + x_num == 4) res |= (1<<0);
    if(t_num + o_num == 4) res |= (1<<1);
  }

  return res;
}

int row_search(char stage[4][4]){
  int res = 0; 

  for(int x=0;x<4;x++){
    int t_num = 0;
    int x_num = 0;
    int o_num = 0;
    for(int y=0;y<4;y++){
      if(stage[y][x] == 'T') t_num++;
      if(stage[y][x] == 'X') x_num++;
      if(stage[y][x] == 'O') o_num++;
    }

    if(t_num >= 2) continue;

    if(t_num + x_num == 4) res |= (1<<0);
    if(t_num + o_num == 4) res |= (1<<1);
  }

  return res;
}

int diag_search(char stage[4][4]){
  int res = 0;

  int t_num = 0;
  int x_num = 0;
  int o_num = 0;

  for(int y=0,x=0;y<4 && x< 4;y++,x++){
    if(stage[y][x] == 'T') t_num++;
    if(stage[y][x] == 'X') x_num++;
    if(stage[y][x] == 'O') o_num++;
  }

  if(t_num <= 1 && t_num + x_num == 4) res |= (1<<0);
  if(t_num <= 1 && t_num + o_num == 4) res |= (1<<1);

  t_num = 0;
  x_num = 0;
  o_num = 0;

  for(int y=0,x=3;y<4 && x>=0;y++,x--){
    if(stage[y][x] == 'T') t_num++;
    if(stage[y][x] == 'X') x_num++;
    if(stage[y][x] == 'O') o_num++;
  }

  if(t_num <= 1 && t_num + x_num == 4) res |= (1<<0);
  if(t_num <= 1 && t_num + o_num == 4) res |= (1<<1);

  return res;
}


int main(){
  int T;
  while(~scanf("%d",&T)){
    for(int test_num=0;test_num<T;test_num++){

      char stage[4][4];

      bool filled_stage = true;
      for(int y=0;y<4;y++){
	char buf[8];
	scanf("%s",buf);
	for(int x=0;x<4;x++){
	  stage[y][x] = buf[x];
	  if(buf[x] == '.') filled_stage = false;
	}
      }

      printf("Case #%d: ",test_num+1);
      int flag = search(stage);
      if(flag == 0 && filled_stage){
	printf("%s","Draw");
      }

      else if(flag == 0 && !filled_stage){
	printf("%s","Game has not completed");
      }
      else if(flag & (1<<0)){
	printf("%s","X won");
      }

      else if(flag & (1<<1)){
	printf("%s","O won");
      }

      printf("\n");
    }
  }
}
