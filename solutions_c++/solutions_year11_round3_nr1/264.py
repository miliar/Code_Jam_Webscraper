#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cctype>
using namespace std;

#define sz(a)  int((a).size())
#define pb  push_back
#define popcount  __builtin_popcount
#define rep(var,n)  for(int var=0,lim=(n);var<lim;var++)
#define all(c)  (c).begin(),(c).end()
#define rall(c)  (c).rbegin(),(c).rend()
#define tr(c,i)  for(__typeof__((c).begin()) i=(c).begin(),till=(c).end(); i!=till; i++)
#define found(s,e)  ((s).find(e)!=(s).end())

int main(){
  int T;cin>>T;
  rep(t,T){
    int R,C; cin>>R>>C;
    vector<vector<char> > m(R+1,vector<char>(C+1, '.'));
    
    rep(r,R){
      string s; cin>>s;
      rep(c,C) m[r][c] = s[c];
    }

    rep(r,R) rep(c,C) {
      if (m[r][c] == '#' && m[r+1][c] == '#' && m[r][c+1] == '#' && m[r+1][c+1] == '#') {
        m[r][c] = m[r+1][c+1] = '/';
        m[r+1][c] = m[r][c+1] = '\\';
      }
    }
 
    bool ok=true;
    rep(r,R) rep(c,C) { if (m[r][c]=='#') { ok=false; break; } }

    printf("Case #%d:\n", 1+t);
    if (ok) {
      rep(r,R) {
        rep(c,C) {
          putchar(m[r][c]);
        }
        putchar('\n');
      }
    } else {
      printf("Impossible\n");
    }
  }
  return 0;
}
