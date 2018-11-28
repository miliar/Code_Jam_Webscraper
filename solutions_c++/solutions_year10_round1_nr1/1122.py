#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <string>
#include <queue>

#define _DEBUG_MODE_

#ifdef _DEBUG_MODE_
#define db(X) cerr << "* DEBUG [L" << __LINE__ << "]: " << #X << " = " << X << endl;
#define db_arr(X) cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<sizeof(X)/sizeof(X[0]); __i__++) cerr << X[__i__] << " "; cerr << endl;
#define db_arrM(X, M) cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<M; __i__++) cerr << X[__i__] << " "; cerr << endl;
#define db_arrMN(X, M, N) cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=M; __i__<N; __i__++) cerr << X[__i__] << " "; cerr << endl;
#else
#define db(X)
#define db_arr(X)
#define db_arrM(X, M)
#define db_arrMN(X, M, N)
#endif

#define For(i, n) for(i=0;i<(n);i++)
#define ForL(i, m, n) for(i=(m);i<(n);i++)

#define Clear(X) memset( (X), 0, sizeof( (X) ) )
#define Fill(X) memset( (X), -1, sizeof( (X) ) )

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef unsigned long ulong;

void _main();

int main() {
  // COUNTER CODE STARTS HERE

  int cases, i;

  cin >> cases;

  For (i, cases) {
    printf("Case #%d: ", i+1);
    _main();
    cout << endl;
  }

  // COUNTER CODE ENDS HERE

  return 0;
}

// ACTUAL CODE STARTS BELOW

char board[100][100];
char rt[100][100];
int n, k;
int dir[4][2] = {{0, 1}, {1, 0}, {1, 1}, {1, -1}};
bool flag_blue, flag_red;

void check() {
  int i, j, s, d, x, y;

  For (i, n) {
    For (j, n) {
      char p = rt[i][j];
      if (p == '.') continue;

      For (d, 4) {
	for (s=1; s<k; s++) {
	  x = i + dir[d][0]*s;
	  y = j + dir[d][1]*s;

	  // db(x); db(y); db(s);
	  if ( x<0 || x>=n || y<0 || y>=n || rt[x][y] != p ) {
	      break;
	    }
	}
	  
	  if (s == k) {
	    if (p == 'B') flag_blue = true;
	    if (p == 'R') flag_red = true;
	  }
	}
      }
    }
  }

  void gravity() {
    for (int col = 0; col < n; col++) {
      int j = n-1;
      int i = j;
      for (; i>=0 && j>=0; j--) {
	rt[i][col] = rt[j][col];
	if (rt[i][col] != '.') {
	  i--;
	}
      }

      while (i >= 0) {
	rt[i--][col] = '.';
      }
    }
  }

  void _main() {
    cin >> n >> k;
    string line;
    int i, j;

    For (i, n) {
      cin >> line;

      For (j, n) {
	board[i][j] = line[j];
      }
      board[i][j] = 0;
    }

    flag_blue = false;
    flag_red = false;

    memcpy(rt, board, sizeof(board));

    // gravity(); check();
    
    // Left
    For (i, n) {
      For (j, n) {
	rt[i][j] = board[n-j-1][i];
      }
    }

    gravity(); check();

    if (flag_red && flag_blue) cout << "Both";
    else if (flag_red) cout << "Red";
    else if (flag_blue) cout << "Blue";
    else cout << "Neither";
    
  }
