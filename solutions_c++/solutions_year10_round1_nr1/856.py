#include <string.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include <fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())

#define for0n(i,n) for(i=0;i<n;i++)
#define for1n(i,n) for(i=1;i<=n;i++)
#define forn(i,j,n) for(i=j;i<n;i++)

const int inf = 2100000000;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

int i, j, k, l, d, ans;
char *ansString;
int nCases;
int N, K;
bool bWin, rWin;

char board[51][51];
int maxm[51][51][2][4];

int value (int x, int y, int c, int dir) {
  if ((x < 0) || (x >= N) || (y < 0) || (y >= N)) {
    return 0;
  }
  if (c == 0) {
    if (board[x][y] == 'R')
      return 0;
  }else if (c == 1) {
    if (board[x][y] == 'B')
      return 0;
  }

  if (maxm[x][y][c][dir] >= 0) {
    return maxm[x][y][c][dir];
  }
  // Otherwise get the max of the 4 directions.
  int big = 0;
  switch (d) {
    case 0:
      big = max(0, value(x-1, y-1,c, 0));
      break;
    case 1:
      big = max(0, value(x, y-1,c, 1));
      break;
    case 2:
      big = max(0, value(x+1, y-1,c, 2));
      break;
    case 3:
      big = max(0, value(x+1, y,c, 3));
      break;
  }
  maxm[x][y][c][dir] = 1 + big;
  return (1 + big);
}

int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

  fstream inFile(argv[1], fstream::in);
  fstream outFile("output.txt", fstream::out);

  inFile >> nCases;
  cout << nCases << endl;
  for0n(i,nCases) {

    bWin = rWin = false;
    for0n(j, 51)
      for0n(k, 51){
        board[j][k] = 0;
        for0n(l,2)
          for0n(d,4)
            maxm[j][k][l][d] = -1;
      }

    inFile >> N >> K;
    for0n(j, N)
      for0n(k, N)
        inFile >> board[j][k];

#if 0
    for0n(j, N) {
      for0n(k, N) 
        cout << board[j][k];
      cout << endl;
    }
    cout << endl;
#endif

    for0n(j, N) {
      int pieces=0;
      char line[51];
      for0n(k,N) {
        if (board[j][k] != '.') {
          line[pieces] = board[j][k];
          pieces++;
        }
      }
      int counter = 0;
      for0n(k,N-pieces) {
        board[j][counter++] = '.';
      }
      for0n(k,pieces) {
        board[j][counter++] = line[k];
      }
    }

#if 0
    for0n(j, N) {
      for0n(k, N) 
        cout << board[j][k];
      cout << endl;
    }
    cout << endl;
#endif

    for0n(j, N) {
      for0n(k, N) {
        if (board[j][k] == '.') {
          for0n(d,4) {
            maxm[j][k][0][d] = 0;
            maxm[j][k][1][d] = 0; // Empty so neither line.
          }
        } else if (board[j][k] == 'R') {
          for0n(d,4) {
            maxm[j][k][0][d] = 0;
          }
        } else {
          for0n(d,4) {
            maxm[j][k][1][d] = 0;
          }
        }
      }
    }
    for0n(j, N) {
      for (k = N-1; k>=0; k--) {
        for0n(d,4) {
          if (value(j,k,0,d) >= K) {
            bWin = true;
          }
        }
        for0n(d,4) {
          if (value(j,k,1,d) >= K) {
            rWin = true;
          }
        }
      }
    }
#if 0

    for0n(j, N) {
      for0n(k, N) 
        cout << maxm[j][k][0];
      cout << endl;
    }
    for0n(j, N) {
      for0n(k, N) 
        cout << maxm[j][k][1];
      cout << endl;
    }
    cout << endl;
#endif

    if (bWin && rWin) {
      ansString = "Both";
    } else if (bWin) {
      ansString = "Blue";
    } else if (rWin) {
      ansString = "Red";
    } else {
      ansString = "Neither";
    }
    outFile << "Case #" << i+1 << ": " << ansString << endl;
  }

  outFile.close();
  return 0;
}
