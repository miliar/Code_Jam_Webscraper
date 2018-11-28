#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
typedef  long long   ll;


#define ALL(x)   (x).begin(),(x).end()
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 1e-9;
const double PI = acos(-1.0);




template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
vector<string> vec;

bool check(int r, int c, int dr, int dc, char ch) {
  REP(i, 4) if (vec[r+dr*i][c+dc*i] != ch && vec[r+dr*i][c+dc*i] != 'T') return
      false;
  return true;
}


bool checkWinner(char c) {
  REP(i, 4) if (check(0, i, 1, 0, c) or check(i, 0, 0, 1, c)) return
    true;
  if (check(0, 0, 1, 1, c) or check(0, 3, 1, -1, c)) return true;
  return false;
}

int countTurns(char c) {
  int res = 0;
  REP(i, 4) REP(j, 4) if (c == vec[i][j]) res++;
  return res;
}

int main() {
  int i,j ,k;
  int casos; scanf("%d", &casos);
  for (int h = 0; h < casos; ++h) {
    while (getchar() != '\n');
    vec.clear();
    for (i = 0; i < 4; ++i) {
      string s; cin >> s; vec.PB(s);
    }
    printf("Case #%d: ", h+1);
    if (checkWinner('X'))
      printf("X won\n");
    else if (checkWinner('O'))
      printf("O won\n");
    else if (countTurns('.'))
      printf("Game has not completed\n");
    else printf("Draw\n");
  }
  return 0;
}
