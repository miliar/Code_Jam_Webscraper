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
bool poss;


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
    poss = true;

    uint64_t N;
    int PD, PG;
    inFile >> N >> PD >> PG;

    bool found = false;
    if (N > 100) {
      N = 100;
    }
    for1n(i, N) {
      int ls = PD * i;
      for(j = 0; j <= i; j++) {
        if (j*100 == ls) {
          found = true;
          break;
        }
      }
      if (found) {
        break;
      }
    }
    if (found) {
      int WD = j; // Won today
      int GD = i; // Played today
      int LD = i - j; // Won today
      // Is it possible to find a way to get this win statistic?
      int find = (100 * WD) - (PG * GD);
      cout << j << "/" << i << " " << LD << " " << find << endl;
      // find == (100 * WR) - (PG * GR) where WD <= WR <= GR and GR >= GD
      //
      // The only way it's impossible is if you need a win of 100 
      if ( ((PG == 100 ) && (LD != 0)) || ((PG == 0) && (WD != 0))) {
        poss = false;
      }
    } else {
      // Maybe it's impossible
      poss = false;
    }

    cout << "Case #" << c + 1 << ": " << (poss ? "Possible" : "Broken") << endl;
    outFile << "Case #" << c + 1 << ": " << (poss ? "Possible" : "Broken") << endl;
  }

  outFile.close();
  return 0;
}
