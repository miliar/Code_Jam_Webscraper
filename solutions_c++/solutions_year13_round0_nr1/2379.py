#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <ctime>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
#define sz(X) ((int)(X).size())
#define FOREACH(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define IN(_lower,_variable,_higher) (((_lower)<=(_variable)) && ((_variable)<=(_higher)))
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORU(v,p,k) for(int v=p;v<k;++v)
#define FORD(v,p,k) for(int v=(p)-1;v>=k;--v)
#define FORLLU(v,p,k) for(LL v=p;v<k;++v)
#define FORLLD(v,p,k) for(LL v=(p)-1;v>=k;--v)
template<class T> vector<T> tokenize_to(const string &str) { vector<T> r; T x; istringstream is(str); while (is >> x) r.push_back(x); return r; }
#define junik(X) {sort( (X).begin(), (X).end() ); (X).erase( unique( (X).begin(), (X).end() ), (X).end() ); }

char a[5][5];
char p[2];

bool check (int x, int y, char c) {
  return a[x][y] == c || a[x][y]=='T';  
}

int solve() {

  for(int i=0;i<4;++i) {
    scanf(" %s", a[i]);
  }
  bool full = true;
  
  for(int i=0;i<4;++i) for(int j=0;j<4;++j) if (a[i][j]=='.') full = false;
  
  for(int i=0;i<4;++i) {    
    for(int k=0;k<2;++k) {
      bool good=true;
      for(int j=0;j<4;++j) {      
        if (!check(i, j, p[k])) { good=false; break;}        
      }
      if (good) return k;
      good=true;
      for(int j=0;j<4;++j) {      
        if (!check(j, i, p[k])) { good=false; break;}        
      }
      if (good) return k;      
    }
  }
  for(int k=0;k<2;++k) {
    bool good= true;
    for(int i=0;i<4;++i) {
      if (!check(i,i, p[k])) { good=false; break;}
    }
    if (good) return k;
    good= true;
    for(int i=0;i<4;++i) {
      if (!check(i, 3-i, p[k])) { good=false; break;}
    }
    if (good) return k;
    
  }
  
  if (full) return 2;
  return 3;
}


int main() {


  int n=0;
  p[0]='X';
  p[1]='O';
  
  vector<string> vs;
  vs.push_back("X won");
  vs.push_back("O won");
  vs.push_back("Draw");
  vs.push_back("Game has not completed");
  
  scanf(" %d", &n);
  
  for(int i=0;i<n;++i) {
    int ret = solve();
    cout << "Case #" << i+1<<": " << vs[ret] << endl;
    
  }

  return 0;

}