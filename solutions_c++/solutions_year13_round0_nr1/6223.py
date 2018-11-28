#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<deque>
#include<queue>
#include<complex>
#include<string>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<cstdlib>

using namespace std;

#define REP(i,a,n) for(int i = a ; i < n ; i++)
#define rep(i,n) REP(i,0,n)

typedef long long ll;
char m[10][10];

bool check(char c){
  // yoko
  rep(i,4){
    if(m[i][0] != c)continue;
    bool f = true;
    rep(j,4){
      if(m[i][0] != m[i][j]){
        f = false;
        break;
      }
    }
    if(f) return true;
  }
  
  // tate
  rep(i,4){
    if(m[0][i] != c)continue;
    bool f = true;
    rep(j,4){
      if(m[0][i] != m[j][i]){
        f = false;
        break;
      }
    }
    if(f) return true;
  }

  // naname
  if(m[0][0] == c && c == m[1][1]
     && c == m[2][2] && c == m[3][3]) return true;
  
  if(m[0][3] == c && c == m[1][2]
     && c == m[2][1] && c == m[3][0]) return true;
  return false;
}

bool isEnd(){
  rep(i,4){
    rep(j,4){
      if(m[i][j] == '.') return false;
    }
  }
  return true;
}

int main(){
  int t;
  cin>>t;
  string state[] = {"X won","O won","Draw","Game has not completed"};
  rep(i,t){
    int tx = -1;
    int ty = -1;
    rep(j,4){
      cin>>m[j];
      rep(k,4){
        if(m[j][k] == 'T'){
          tx = k;
          ty = j;
        }
      }
    }
    int res = 2;
    // X
    if(tx != -1){
      m[ty][tx] = 'X';
    }
    if(check('X')) res = 0;
    // O
    if(tx != -1){
      m[ty][tx] = 'O';
    }
    if(check('O')) res = 1;
    if(res == 2 && !isEnd()){
      res = 3;
    }
   
    cout<<"Case #"<<i+1<<": "<<state[res]<<endl;
  }
}
