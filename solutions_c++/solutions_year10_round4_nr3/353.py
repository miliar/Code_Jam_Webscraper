#include <stdio.h>      
#include <ctype.h>
#include <math.h>

#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <stack>
using namespace std;

#define ALL(x) x.begin(), x.end()
#define VAR(a,b) __typeof (b) a = b
#define REP(i,n) for (int _n=(n), i=0; i<_n; ++i)
#define FOR(i,a,b) for (int _b=(b), i=(a); i<=_b; ++i)
#define FORD(i,a,b) for (int _b=(b), i=(a); i>=_b; --i)
#define FORE(i,a) for (VAR(i,a.begin ()); i!=a.end (); ++i) 
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;

const int DBG = 0, INF = int(1e9);

string toString(LL k){stringstream ss;ss << k;string res;ss >> res;return res;}
int toInt(string s){stringstream ss; ss << s; int res; ss >> res; return res;}

const int MAXN = 1000;

int A[2][MAXN][MAXN];

int main() {
  ios_base::sync_with_stdio(0);

  int C;

  scanf("%d", &C);

  REP(k,2) REP(i,MAXN) REP(j,MAXN) 
    A[k][i][j] = 0;

  REP(q,C) {

    int R;

    scanf("%d", &R);

    int left = INF,right = -1,up = INF, down = -1;

    REP(s,R) {

      int a,b,c,d;

      scanf("%d %d %d %d", &a, &b, &c, &d);

      if (a > c)
        swap(a,c);
      if (b > d)
        swap(b,d);

      FOR(i,a,c) FOR(j,b,d)
        A[0][i][j] = 1;
      
      left = min(left, a);
      right = max(right, c);
      up = min(up, b);
      down = max(down, d);

    }

    int life = 0, last = 0, res = 0;

    FOR(i,left,right) FOR(j,up,down)
      life += A[0][i][j];

    while (life) {
      //cout << left << endl;
      int nxt = 1 - last;
      FOR(i,left,right + 1) FOR(j,up,down + 1) {
        if (A[last][i][j] == 0) {
          if (A[last][i - 1][j] && A[last][i][j - 1]) 
            A[nxt][i][j] = 1;
          else
            A[nxt][i][j] = 0;
        }
        else {
          if (!A[last][i - 1][j] && !A[last][i][j - 1])
            A[nxt][i][j] = 0;
          else
            A[nxt][i][j] = 1;
        }
      }
      FOR(i,left,right + 1) FOR(j,up,down + 1)
        A[last][i][j] = 0;
      int cleft = left, cright = right, cup = up, cdown = down;
      life = 0;
      FOR(i,left,right + 1) FOR(j,up,down + 1)
        if (A[nxt][i][j] == 1) {
          cleft = min(cleft, i);
          cright = max(cright, i);
          cup = min(cup, j);
          cdown = max(cdown,j);
          ++life;
        }
      left = cleft; right = cright; up = cup; down = cdown;
      swap(last,nxt);
      ++res;
    }

    printf("Case #%d: %d\n", q + 1, res);

  }

  return 0;
}
