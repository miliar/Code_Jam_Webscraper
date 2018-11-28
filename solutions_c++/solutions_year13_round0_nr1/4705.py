#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <cassert>
using namespace std;

typedef long long ll;
static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
bool ISINT(double x){return fabs(x-(int)round(x))<EPS;}
bool ISEQ(double x,double y){return fabs(x-y)<EPS;}
string itos(ll x){stringstream ss;ss<<x;return ss.str();}
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define EREP(i,a,b) for(int i=a;i<=b;i++)
#define erep(i,n) EREP(i,0,n)
#define foreach(itr,c) for(__typeof(c.begin()) itr=c.begin();itr!=c.end();itr++)

#define X_WON 0
#define O_WON 1
#define DRAW 2
#define NOT_COMP 3

string mes[4] = {
  "X won",
  "O won",
  "Draw",
  "Game has not completed",
};
char t[10][10];

int check(int x, int y, int dx, int dy){
  int Ocnt = 0;
  int Xcnt = 0;
  int Tcnt = 0;

  for(int i = 0; i < 4; i++){
    if(t[y][x] == 'T') Tcnt = 1;
    else if(t[y][x] == 'X') Xcnt++;
    else if(t[y][x] == 'O') Ocnt++;

    x += dx;
    y += dy;
  }

  if(Xcnt + Tcnt == 4) return X_WON;
  if(Ocnt + Tcnt == 4) return O_WON;
  return -1;
}

int solve(){
  int tmp = check(0, 0, 1, 1);
  if(tmp != -1) return tmp;

  tmp = check(3, 0, -1, 1);
  if(tmp != -1) return tmp;

  for(int i = 0; i < 4; i++){
    tmp = check(i, 0, 0, 1);
    if(tmp != -1) return tmp;

    tmp = check(0, i, 1, 0);
    if(tmp != -1) return tmp;
  }

  for(int i = 0; i < 4; i++){
    for(int j = 0; j < 4; j++){
      if(t[i][j] == '.') return NOT_COMP;
    }
  }

  return DRAW;
}

int main(void){
  int T;
  cin >> T;

  for(int CASE = 1; CASE <= T; CASE++){
    cout << "Case #" << CASE << ": ";
    for(int i = 0; i < 4; i++){
      cin >> t[i];
    }
    cout << mes[solve()] << endl;
  }
}
