#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define sz(a)  int((a).size())
#define pb  push_back
#define FOR(var,from,to) for(int var=(from);var<=(to);var++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define found(s,e)  ((s).find(e)!=(s).end())

//#include "../cout.h"

vector<char> grav(string s){
  int n=sz(s), a=n-1;
  vector<char> res(n,'.');
  for (int i=n-1;i>=0;i--){
    if (s[i] != '.') res[a--] = s[i];
  }
  return res;
}
main(){
  int T; cin >> T;
  
  rep(t,T){
    int N,K; cin >> N >> K;
    vector<vector<char> > board(N,vector<char>(N)), rot(N,vector<char>(N));    
    rep(r,N){
      string buf; cin >> buf;
      vector<char> gbuf = grav(buf);
      rep(c,N){
        board[r][c] = gbuf[c];
      }
      ///cout << gbuf << endl;
    }

    char rb[2] = { 'R','B' };
    bool gd[2] = { false,false };
    rep(z,2) {
      char ch = rb[z];
      rep(i,N){
        int a=0;
        rep(j,N){
          int x=i, y=j;
          if (board[y][x]==ch) a++; else a=0;
          if (a == K) gd[z]=true;
        }
        a=0;
        rep(j,N){
          int x=j, y=i;
          if (board[y][x]==ch) a++; else a=0;
          if (a == K) gd[z]=true;
        }
      }
      for(int i=-(N-1); i<=(N-1); i++){
        //cout << ch << "<3>: ";
        int a=0;
        int sx=0, sy=i;
        rep(j,N){
          int x=sx+j, y=sy+j; if (y<0 || N<=y) continue;
          //printf(" (%d,%d)", x,y);
          if (board[y][x]==ch) a++; else a=0;
          if (a == K) gd[z]=true;
        }
        
        a=0;
        sx=0, sy=i+(N-1);
        rep(j,N){
          int x=sx+j, y=sy-j; if (y<0 || N<=y) continue;
          if (board[y][x]==ch) a++; else a=0;
          if (a == K) gd[z]=true;
        }
      }
    }

    cout << "Case #" << (t+1) << ": ";
    if (gd[0]) {
      if (gd[1]) cout << "Both" << endl;
      else cout << "Red" << endl;
    } else {
      if (gd[1]) cout << "Blue" << endl;
      else cout << "Neither" << endl;
    }
  }
  return 0;
}
