#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <set>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <stack>
#include <sstream>
#include <climits>
#include <queue>
#include <cctype>

#define mp make_pair

#define rep(i,n) for(int i=0; i<(int)(n); i++)
#define REP(i,s,n) for(int i=(s); i<(int)(n); i++)
#define ALL(c) (c).begin(),(c).end()

//int dx[] = {0,1,0,-1};
//int dy[] = {1,0,-1,0};
int dx[] = {0,1,1,1,0,-1,-1,-1};
int dy[] = {1,1,0,-1,-1,-1,0,1};
const int MAX = 101;
const int INF = 1<<29;

using namespace std;

typedef long long ll;
typedef pair<int,int> P;

char field[4][4];
int flag;
bool empty;

void print(){
   for(int i=0; i<4; i++){
      for(int j=0; j<4; j++){
         cout << field[i][j];
      }
      cout << endl;
   }
}

void dfs(int y, int x, char c){

   for(int i=0; i<8; i++){
      int nx = x + dx[i], ny = y + dy[i];
      int cnt = 1;
      while(nx >= 0 && nx < 4 && ny >= 0 && ny < 4 &&
            (field[ny][nx] == c || field[ny][nx] == 'T')){
         cnt++;
         nx += dx[i];
         ny += dy[i];
      }
      if(cnt == 4){
         if(c == 'X'){
            flag = 1;
            return;
         } else {
            flag = 0;
            return;
         }
      }
   }
   
}
int main(){
   int T;
   cin >> T;

   for(int t=0; t<T; t++){
      empty = false;
      for(int i=0; i<4; i++){
         for(int j=0; j<4; j++){
            cin >> field[i][j];
            if(field[i][j] == '.') empty = true;
         }
      }
      cin.ignore();

      flag = -1;

      for(int i=0; i<4; i++){
         for(int j=0; j<4; j++){
            if(field[i][j] == '.')continue;
            dfs(i,j,field[i][j]);
            if(flag != -1) goto end;
         }
      }
     end:
      cout << "Case #" << t+1 << ": ";   
      if(flag == -1 && empty) cout << "Game has not completed" << endl;
      else if(flag == -1) cout << "Draw" << endl;
      else if(flag == 0) cout << "O won" << endl;
      else cout << "X won" << endl;

   }
   
  return 0;
}
