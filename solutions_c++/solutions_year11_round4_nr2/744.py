#include <string.h>
#include <stdint.h>
#include <cstdio>
#include <cstdlib>
#include <ctype.h>
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
#define ZERO(arr) for(int CNT=0;CNT<sizeof(arr);CNT++){arr[CNT]=0;}

const int MAX = 1000000;
const int inf = 2100000000;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

int move[4][2] = { {0, 1} , {1, 0} , {0, -1} , {-1, 0} };

//ofstream debug("debug.txt", fstream::trunc);

//
// Add variables here.
//
int nCases;
int c, i, j, k, l;
int ans;
int R, C, D;
int w[500][500];

int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

  ifstream inFile(argv[1]);
  ofstream outFile("output.txt", fstream::trunc);

  inFile >> nCases;
  cout << nCases << " cases." << endl;
  for0n(c,nCases) {
    ans = 0;
    inFile >> R >> C >> D;
    for0n(i, R) {
      for0n(j, C) {
        char inchar;
        inFile >> inchar;
        w[i][j] = inchar - '0';
      }
    }

    ans = min(R, C);
    //cout << "Max size is: " << ans << endl;

    bool found = false;
    for (; ans >= 3 && !found; --ans) {
      //cout << "Try ans= " << ans << endl;
      bool even = true;
      int lbi, ubi, lbj, ubj;
      if (ans & 1) {
        // Edges are odd number
        even = false;
      }
      lbi = 0;
      ubi = R - ans;
      lbj = 0;
      ubj = C - ans;
      for(i = lbi; i <= ubi && !found; ++i) {
        for(j = lbj; j <= ubj && !found; ++j) {
          int totalx = 0;
          int totaly = 0;
          int cx = (2*i + ans);
          int cy = (2*j + ans);
          //cout << "- " << i << ", " << j << endl;
          //cout << "- " << cx << ", " << cy << endl;
          for (k = i; k < i+ans; ++k) {
            for(l = j; l < j+ans; ++l) {
              if (((k==i) || (k == i + ans - 1)) && ((l == j) || (l ==j+ans-1))) {
                continue;
              }
              totalx += ((2*k - cx + 1) * (D + w[k][l]));
              totaly += ((2*l - cy + 1) * (D + w[k][l]));
              //cout << totalx << ":" << totaly << endl;
            }
          }
          if ((totalx == 0) && (totaly == 0)) {
            found = true;
          }
        }
      }
    }
    if (found) {
      cout << "Case #" << c + 1 << ": " << ans + 1 << endl;
      outFile << "Case #" << c + 1 << ": " << ans + 1 << endl;
    } else {
      cout << "Case #" << c + 1 << ": IMPOSSIBLE" << endl;
      outFile << "Case #" << c + 1 << ": IMPOSSIBLE" << endl;
    }
  }

  outFile.close();
  return 0;
}
