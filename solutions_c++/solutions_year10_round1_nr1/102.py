#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <functional>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SZ(a) ((int)((a).size()))
#define REPSZ(i,v) REP(i,SZ(v))
#define ALL(a) (a).begin(),(a).end()
typedef long long Int;
template<class T> inline T sq(T x){return x * x;}
template<class T> inline void checkmin(T &a,T b){if(b<a)a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a)a=b;}

string table[55];

void rotate(int N) {
  string buf[N];
  REP(i, N) buf[i] = table[i];

  REP(i, N) REP(j, N) {
    table[i][j] = buf[N - 1 - j][i];
  }
}

void gravity(int N) {
  REP(c, N) {
    for(int r = N - 1; r >= 0; r--) {
      if( table[r][c] != '.' ) {
        int i = r;
        while(i + 1 < N && table[i+1][c] == '.' ) {
          swap(table[i][c], table[i+1][c]);
          i++;
        }
      }
    }
  }
}

bool valid(int x, int y, int N) {
  return 0 <= x && x < N && 0 <= y && y < N;
}

int win(int N, int K, int color) {
  REP(r, N) {
    for(int c = 0; c < N; c++) {
      int con = 0;
      if( table[r][c]== color ) {
        while( c < N && table[r][c] == color) {
          c++;
          con++;
        }
      }
      if( con >= K ) return 1;
    }
  }

  REP(c, N) {
    for(int r = 0; r < N; r++) {
      int con = 0;
      if( table[r][c]== color ) {
        while( r < N && table[r][c] == color) {
          r++;
          con++;
        }
      }
      if( con >= K ) return 1;
    }
  }

  REP(sr, N) REP(sc, N) {
    if( table[sr][sc] == color ) {
      {
        int dr = 1;
        int dc = 1;
        int r = sr - dr;
        int c = sc - dc;
        if( valid( r, c, N ) && table[r][c] == color ) continue;
        r = sr;
        c = sc;
        int con = 0;
        while( valid(r, c, N) && table[r][c] == color) {
          r += dr;
          c += dc;
          con++;
        }
        if( con >= K ) return 1;
      }

      {
        int dr = 1;
        int dc = -1;
        int r = sr - dr;
        int c = sc - dc;
        if( valid( r, c, N ) && table[r][c] == color ) continue;
        r = sr;
        c = sc;
        int con = 0;
        while( valid(r, c, N) && table[r][c] == color) {
          r += dr;
          c += dc;
          con++;
        }
        if( con >= K ) return 1;
      }
    }
  }
  return 0;
}

int main() {
  int TNO;
  scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
    printf("Case #%d: ", tno);
    int N, K; cin >> N >> K;

    REP(i, N) {
      cin >> table[i];
    }

    rotate(N);
    gravity(N);

//     REP(i,N)cout << table[i] << endl;

    int R = win(N, K, 'R');
    int B = win(N, K, 'B');

    string res;
    if( R && B ) {
      res = "Both";
    } else if( R ) {
      res = "Red";
    } else if( B ) {
      res = "Blue";
    } else {
      res = "Neither";
    }
    cout << res << endl;
  }

  return 0;
}
