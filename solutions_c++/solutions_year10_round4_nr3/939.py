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

int cas, i, j, k, l, ans;
int nCases;
int d, n;
int fx, tx, fy, ty;

bool field[1000][1000];

void dump()
{
  int x, y;
  for(y = 0; y <= ty+1; y++) {
    for(x = 0; x <= tx+1; x++) {
      if (!field[x][y]) {
        cout << ".";
      } else {
        cout << "*";
      }
    }
    cout << endl;
  }
    cout << endl;
  //ty++;
  //tx++;
}

int iterate()
{
  int count = 0;
  int x, y;
  for(x = tx+1; x >= fx-1; x--) {
    for(y = ty+1; y >= fy-1; y--) {
      if (!field[x][y]) {
        if (field[x][y-1] && field[x-1][y]) {
          field[x][y] = true;
          count++;
        }
      } else {
        count++;
        if (!(field[x][y-1] || field[x-1][y])) {
          field[x][y] = false;
          count--;
        }
      }
    }
  }
  //ty++;
  //tx++;
  return count;
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
  for0n(cas,nCases) {
    ans = 0;
    for0n(i, 1000)
      for0n(j, 1000)
        field[i][j] = false;
    fx = fy = 1000;
    tx = ty = 0;
    int numrect;
    inFile >> numrect;
    for0n(k, numrect) {
      int x1, x2, y1, y2;
      inFile >> x1 >> y1 >> x2 >> y2;
      fx = min(fx, x1);
      fy = min(fy, y1);
      tx = max(tx, x2);
      ty = max(ty, y2);
      for(i = x1; i <= x2; i++) {
        for (j = y1; j <= y2; j++) {
          //cout << i << " " << j << endl;
          field[i][j] = true;
        }
      }
    }
    int left;
    do {
      //dump();
      left = iterate();
      ans++;
    } while (left != 0);

    outFile << "Case #" << cas+1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
