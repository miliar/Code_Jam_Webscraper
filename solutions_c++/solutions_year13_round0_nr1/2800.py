#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <ctime>

#define pb push_back
#define mp make_pair
#define PI 3.1415926535897932384626433832795
#define ALL(x) x.begin(), x.end()
#define F first
#define S second
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,-1,sizeof(x))
#define pw(x) (1ull<<(x))

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

int a[5][5];

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  for (int o=0;o<t;o++) {
    cout << "Case #" << o+1 << ": ";
    int s = 0;
    for (int i=0;i<4;i++) for (int j=0;j<4;j++) {
      char c = 0;
      while (c!='O' && c!='X' && c!='T' && c!='.') c = getchar();
      if (c=='.') a[i][j] = 0;
      else if (c=='X') a[i][j] = 1;
      else if (c=='O') a[i][j] = 2;
      else a[i][j] = 3;
      if (a[i][j]==0) s=1;
    }
    
    bool end = false;
    for (int i=0;i<4 && !end;i++) {
      bool ok = true;
      int mi = INF;
      for (int j=0;j<4;j++) mi = min(mi, a[i][j]);
      if (mi==0) ok = false;
      for (int j=0;j<4;j++) if (a[i][j]!=mi && a[i][j]!=3) ok = false;
      if (ok) {
        end = true;
        if (mi==1) cout << "X won\n"; else cout << "O won\n";
      }
    }
    for (int j=0;j<4 && !end;j++) {
      bool ok = true;
      int mi = INF;
      for (int i=0;i<4;i++) mi = min(mi, a[i][j]);
      if (mi==0) ok = false;
      for (int i=0;i<4;i++) if (a[i][j]!=mi && a[i][j]!=3) ok = false;
      if (ok) {
        end = true;
        if (mi==1) cout << "X won\n"; else cout << "O won\n";
      }
    }
    if (!end) {
      bool ok = true;
      int mi = INF;
      for (int j=0;j<4;j++) mi = min(mi, a[j][j]);
      if (mi==0) ok = false;
      for (int j=0;j<4;j++) if (a[j][j]!=mi && a[j][j]!=3) ok = false;
      if (ok) {
        end = true;
        if (mi==1) cout << "X won\n"; else cout << "O won\n";
      }
    }
    if (!end) {
      bool ok = true;
      int mi = INF;
      for (int j=0;j<4;j++) mi = min(mi, a[j][3-j]);
      if (mi==0) ok = false;
      for (int j=0;j<4;j++) if (a[j][3-j]!=mi && a[j][3-j]!=3) ok = false;
      if (ok) {
        end = true;
        if (mi==1) cout << "X won\n"; else cout << "O won\n";
      }
    }
    if (s && !end) {
      cout << "Game has not completed\n";
      continue;
    }
    else if (!end) cout << "Draw\n";
  }
  return 0;
}
