#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <cstring>

using namespace std;

typedef long long          ll;
typedef vector<int>        vi;
typedef pair<int, int>     ii;
typedef vector<ii>         vii;
typedef set<int>           si;
typedef map<string, int>   msi;

//#define for(i, a, b) \
//  for(int i = int(a); i <= int(b); i++)
//#define Rvi(c, it) \
//  for(vi::iterator it = (c).begin(); it != (c).end(); it++)
//#define Rvii(c, it) \
//  for(vii::iterator it = (c).begin(); it != (c).end(); it++)
//#define Rmsi(c, it) \
//  for(msi::iterator it = (c).begin(); it != (c).end(); it++)

int main() {
  int t, tc=0;
  scanf("%d", &t);

  while(t--) {
    tc++;
    string T[4];

    for(int i=0; i<4; i++)
      cin >> T[i];

    char win = '.';

    int f[4][4];
    memset(f, 0, sizeof(f));
    int c[4][4];
    memset(c, 0, sizeof(c));
    int d1[4];
    memset(d1, 0, sizeof(d1));
    int d2[4];
    memset(d2, 0, sizeof(d2));

    for(int i=0; i<4; i++) {
      for(int j=0; j<4; j++) {
	if(T[i][j] == 'X') f[i][0]++;
	if(T[i][j] == 'O') f[i][1]++;
	if(T[i][j] == 'T') {
	  f[i][0]++;
	  f[i][1]++;
	  f[i][2]++;
	}
	if(T[i][j] == '.') f[i][3]++;
      }
    }

    for(int j=0; j<4; j++) {
      for(int i=0; i<4; i++) {
	if(T[i][j] == 'X') c[j][0]++;
	if(T[i][j] == 'O') c[j][1]++;
	if(T[i][j] == 'T') {
	  c[j][0]++;
	  c[j][1]++;
	  c[j][2]++;
	}
	if(T[i][j] == '.') c[j][3]++;
      }
    }

    for(int i=0; i<4; i++) {
	if(T[i][i] == 'X') d1[0]++;
	if(T[i][i] == 'O') d1[1]++;
	if(T[i][i] == 'T') {
	  d1[0]++;
	  d1[1]++;
	  d1[2]++;
	}
	if(T[i][i] == '.') d1[3]++;

	if(T[i][3-i] == 'X') d2[0]++;
	if(T[i][3-i] == 'O') d2[1]++;
	if(T[i][3-i] == 'T') {
	  d2[0]++;
	  d2[1]++;
	  d2[2]++;
	}
	if(T[i][3-i] == '.') d2[3]++;
    }

    for(int i=0; i<4; i++) {
      if(f[i][0] == 4 || c[i][0] == 4 || d1[0] == 4 || d2[0] == 4) {
	win = 'X';
	break;
      }

      if(f[i][1] == 4 || c[i][1] == 4 || d1[1] == 4 || d2[1] == 4) {
	win = 'O';
	break;
      }
    }

    if(win == 'X' || win == 'O') {
      printf("Case #%d: %c won\n", tc, win);
    } else {

      for(int i=0; i<4; i++) {
	if(f[i][0]+f[i][3] == 4 || c[i][0]+f[i][3] == 4 || d1[0]+f[i][3] == 4 || d2[0]+f[i][3] == 4) {
	  win = 'a';
	  break;
	}

	if(f[i][1]+f[i][3] == 4 || c[i][1]+f[i][3] == 4 || d1[1]+f[i][3] == 4 || d2[1]+f[i][3] == 4) {
	  win = 'a';
	  break;
	}
      } 

      if(win == '.')
	printf("Case #%d: Draw\n", tc);
      else
	printf("Case #%d: Game has not completed\n", tc);
    }
  }

  return 0;
}
