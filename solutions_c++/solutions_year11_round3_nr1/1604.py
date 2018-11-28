#include<iostream>
#include<cstdio>
using namespace std;

#define REP(i,i0,in) for(int i=(i0); i<(in); i++)

int R,C;
char TILE[50][50];

void mark(int x, int y){
  int count=0;
  REP(dy,0,2){
    REP(dx,0,2){
      if (TILE[y+dy][x+dx] == '#') {
	count++;
      }
    }
  }
  if (count < 4){
    return;
  }
  TILE[y][x] = '/';
  TILE[y][x+1] = '\\';
  TILE[y+1][x] = '\\';
  TILE[y+1][x+1] = '/';
}

bool compute(){
  REP(y,0,R-1){
    REP(x,0,C-1){
      if (TILE[y][x] == '#') {
	mark(x,y);
      }
    }
  }
  
  REP(y,0,R){
    REP(x,0,C){
      if (TILE[y][x] == '#') {
	return false;
      }
    }
  }
  return true;
}

int main(){
  int T;
  cin >> T;
  REP(t,1,T+1){
    cin >> R >> C;
    REP(y,0,R){
      REP(x,0,C){
	cin >> TILE[y][x];
      }
    }
    bool possible = compute();
    printf("Case #%d:\n", t);
    if (!possible){
      printf("Impossible\n");
      continue;
    }
    REP(y,0,R){
      REP(x,0,C){
	cout << TILE[y][x];
      }
      cout << endl;
    }
  }
  return 0;
}
