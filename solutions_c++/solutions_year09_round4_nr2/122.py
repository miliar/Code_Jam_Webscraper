#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <cmath>
#include <numeric>
#include <bitset>
#include <stack>

using namespace std;
 
int dr[]={0,1,0,-1,1,1,-1,-1};
int dc[]={1,0,-1,0,1,-1,1,-1};
#define zmax(a,b) (((a)>(b))?(a):(b))
#define zmin(a,b) (((a)>(b))?(b):(a))
#define zabs(a) (((a)>=0)?(a):(-(a)))
#define iif(c,t,f) ((c)?(t):(f))
template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

string g[50];
int R, C, F;
int memo[53][53][53];

int solve(int, int, int);

int fall(int r, int c) {
  int d = 1;
  int i;
  for(i = r + 1; i + 1 < R; i++) {
    if(g[i + 1][c] == '#') {
      break;
    }
    d++;
  }
  if(d > F) return 1000000000;
  if(i + 1 == R) return 0;

  int a = c, b = c + 1;
  while(a > 0 && g[i][a - 1] == '.' && g[i + 1][a] == '#') a--;
  while(b < C && g[i][b] == '.' && g[i + 1][b - 1] == '#') b++;
//cout << a << ", " << b << ", " << i << endl;
  return solve(i, a, b);
}

int solve(int r, int a, int b) {
  if(r == R) return 1000000000;
  if(r + 1 == R) return 0;
  int & ref = memo[r][a][b];
  if(ref != -1) return ref;
  bool lft = g[r + 1][a] == '.';
  bool rht = g[r + 1][b - 1] == '.';

  ref = 1000000000;
  if(lft) {
    ref = min(ref, fall(r, a));
  }
  if(rht) {
    ref = min(ref, fall(r, b - 1));
  }
  if(b - a - lft - rht > 1) {
    for(int i = a; i < b; i++) {
      ref = min(ref, 1 + fall(r, i));
    }
    if(r + 2 < R) for(int oi = a; oi < b; oi++) {
      for(int oj = oi + 2; oj <= b; oj++) {
        int i = oi, j = oj;
        if(i == a + 1 && lft) i = a;
        if(j == b - 1 && rht) j = b;
        if(i == a && j == b) continue;
        if(!(i != a && g[r + 2][oi] == '#' || j != b && g[r + 2][oj - 1] == '#')) continue;

        bool ok = true;
        for(int k = oi + 1; k + 1 < oj; k++) ok = g[r + 2][k] == '#';
        if(!ok) continue;

        int cost = j - i;
        if(i == a && lft) cost--;
        if(j == b && rht) cost--;
        ref = min(ref, cost + solve(r + 1, oi, oj));
      }
    }
  }
//cout << r << ", " << a << ", " << b << ", " << ref << ", " << lft << ", " << rht << endl;
  return ref;
}

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    cin >> R >> C >> F;
    for(int i = 0; i < R; i++) cin >> g[i];
    memset(memo, -1, sizeof(memo));
    int w = g[0].find('#');
    if(w == -1) w = C;
    int ww = g[1].find('.');
    if(ww != -1) w = min(w, ww + 1);
    int result = solve(0, 0, w);

    cout << "Case #" << t << ": ";
    if(result == 1000000000) cout << "No" << endl;
    else cout << "Yes " << result << endl;
  }
  

  return 0;
}
