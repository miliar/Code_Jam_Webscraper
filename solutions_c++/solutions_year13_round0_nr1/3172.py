#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<list>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define GI(x) scanf("%d", &x);
#define FORN(i, n) for(int i = 0; i < n; i++)
#define FOR(i, start, end) for(int i = start; i < end; i++)
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 1000000000
using namespace std;

vector<string> v;

void input() {
  v.clear();
  string s;
  FORN(i, 4) {
    cin >> s;
    v.PB(s);
  }
}

bool check(char c) {
  FORN(i, 4) {
    int num = 0;
    FORN(j, 4) {
      if (v[i][j] == c || v[i][j] == 'T')
        num++;
    }
    if (num == 4)
      return true;
    num = 0;
    FORN(j, 4) {
      if (v[j][i] == c || v[j][i] == 'T')
        num++;
    }
    if (num == 4)
      return true;
  }
  int num = 0;
  FORN(i, 4) {
    if (v[i][i] == c || v[i][i] == 'T')
      num++;
  }
  if (num == 4)
    return true;
  num = 0;
  FORN(i, 4) {
    if (v[i][4-i-1] == c || v[i][4-i-1] == 'T')
      num++;
  }
  if (num == 4)
    return true;
}
int solve() {
  int num_empty = 0;
  FORN(i, 4)
    FORN(j, 4)
      if (v[i][j] == '.')
        num_empty++;
  if (check('X'))
    return 0;
  if (check('O'))
    return 1;
  if (num_empty == 0)
    return 2;
  return 3;

}

int main() {
  int N;
  GI(N);
  FORN(i, N) {
    input();
    int ans = solve();
    printf("Case #%d: ", i+1);
    switch(ans) {
      case 0:
        printf("X won\n");
        break;
      case 1:
        printf("O won\n");
        break;
      case 2:
        printf("Draw\n");
        break;
      case 3:
        printf("Game has not completed\n");
        break;
    }
  }
}
