#include<iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef long double LD;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

char C[4][4];

//0, 1 , 2: nikto, X, O
int check(char C[4]){
  int po = 0;
  int pt = 0;
  int px = 0;
  FOR(j,4){
    if (C[j] == 'T') pt++;
    if (C[j] == 'X') px++;
    if (C[j] == 'O') po++;
  }
  if (px + pt == 4) return 1;
  if (po + pt == 4) return 2;
  return 0;
}

void outx(int x){
  printf("Case #%d: X won\n", x);
}

void outo(int x){
  printf("Case #%d: O won\n", x);
}

void solve(int tt){
  FOR(i,4) scanf("%s ", C[i]);
  FOR(i,4){
    int t = check(C[i]);
    if (t > 0){
      if (t == 1) outx(tt+1);
      else outo(tt+1);
      return;
    }
  }
  FOR(i,4){
    char P[4];
    FOR(j,4) P[j] = C[j][i];
    int t = check(P);
    if (t > 0){
      if (t == 1) outx(tt+1);
      else outo(tt+1);
      return;
    }
  }

  char P[4];
  FOR(i,4) P[i] = C[i][i];
  int t = check(P);
  if (t > 0){
    if (t == 1) outx(tt+1);
    else outo(tt+1);
    return;
  }

  FOR(i,4) P[i] = C[i][3-i];
  t = check(P);
  if (t > 0){
    if (t == 1) outx(tt+1);
    else outo(tt+1);
    return;
  }

  int p = 0;
  FOR(i,4)FOR(j,4) if (C[i][j] == '.') p++;
  if (p == 0) printf("Case #%d: Draw\n", tt+1);
  else printf("Case #%d: Game has not completed\n", tt+1);

}

int main(){
  int TT;
  scanf("%d ", &TT);
  for(int tt = 0; tt < TT; tt++){
    solve(tt);
  }
}
