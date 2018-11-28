#include <string.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
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

uint32_t my32;
int  altArr[100][100];
int  basinArr[100][100];
int  flowDir[100][100];
int  nextBasin;
char basinLetter[26];
char nextLetter;

uint64_t i, j, k, l, ans;
int nCases;
int sx, sy;
vector<uint64_t> xvec;
vector<uint64_t> yvec;

// 0 = sink
// 1 = North
// 2 = West
// 3 = East
// 4 = South
int flowTo(int x, int y) {
  int choice = 0;
  int curLow = altArr[x][y];

  if (y != sy-1) 
    if ((altArr[x][y+1] < curLow) ||
        ((altArr[x][y+1] == curLow) && (choice != 0))){
      choice = 4;
      curLow = altArr[x][y+1];
    }
  if (x != sx-1) 
    if ((altArr[x+1][y] < curLow) ||
        ((altArr[x+1][y] == curLow) && (choice != 0))){
      choice = 3;
      curLow = altArr[x+1][y];
    }
  if (x != 0) 
    if ((altArr[x-1][y] < curLow) ||
        ((altArr[x-1][y] == curLow) && (choice != 0))){
      choice = 2;
      curLow = altArr[x-1][y];
    }
  if (y != 0) 
    if ((altArr[x][y-1] < curLow) ||
        ((altArr[x][y-1] == curLow) && (choice != 0))){
      choice = 1;
      curLow = altArr[x][y-1];
    }

  flowDir[x][y] = choice;
  return choice;
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
  //for0n(i, 1) {
  for0n(i, nCases) {
    memset(altArr, 0, sizeof(altArr));
    memset(basinArr, 0, sizeof(basinArr));
    memset(flowDir, 0, sizeof(basinArr));
    memset(basinLetter, (char)0, sizeof(basinLetter));
    nextBasin = 1;
    nextLetter = 'a';
    ans = 0;

    inFile >> sy >> sx ;
    //cout << sx << " " << sy << endl;
    // Read map
    for0n(j, sx*sy) {
      inFile >> altArr[j%sx][j/sx];
    }

    int min = inf, mx = -1, my = -1; 
    for0n(j, sx*sy) {
      if (flowTo(j%sx, j/sx) == 0) {
        //cout << "Sink @ " << j%sx << ", " << j/sx << endl;
        basinArr[j%sx][j/sx] = nextBasin++;
      }
    }
#if 0
    for (int y = 0; y < sy; y++) {
      for (int x = 0; x < sx; x++) {
        cout << flowDir[x][y] << " ";
      }
      cout << endl;
    }
      cout << endl;
#endif


    bool done = false;
    int iterations = 0;
    while (done == false) {
      iterations++;
      done = true;
      for0n(j, sx*sy) {
        int x = j%sx;
        int y = j/sx;

        if (basinArr[x][y])
          continue;

// 1 = North
// 2 = West
// 3 = East
// 4 = South
        int newBasin = 0;
        switch (flowDir[x][y]) {
          case 0:
            continue;
          case 1:
            newBasin = basinArr[x][y-1];
            break;
          case 2:
            newBasin = basinArr[x-1][y];
            break;
          case 3:
            newBasin = basinArr[x+1][y];
            break;
          case 4:
            newBasin = basinArr[x][y+1];
            break;
        }
        if (newBasin) {
          basinArr[x][y] = newBasin;
        } else {
          // Need to do it again.
          done = false;
        }
      }
#if 0
    for (int y = 0; y < sy; y++) {
      for (int x = 0; x < sx; x++) {
        cout << basinArr[x][y] << " ";
      }
      cout << endl;
    }
#endif
    }

    for (int y = 0; y < sy; y++) {
      for (int x = 0; x < sx; x++) {
        if (basinLetter[basinArr[x][y] - 1] == 0) {
          basinLetter[basinArr[x][y] - 1] = nextLetter++;
        }
      }
    }
    outFile << "Case #" << i+1 << ":" << endl;
    cout << "Case #" << i+1 << " " << "Iterations: " << iterations << endl;
    for (int y = 0; y < sy; y++) {
      for (int x = 0; x < sx; x++) {
        //cout << basinLetter[basinArr[x][y] - 1] << " ";
        outFile << basinLetter[basinArr[x][y] - 1] << " ";
      }
      //cout << endl;
      outFile << endl;
    }
    //cout << endl;
    //outFile << "Case #" << i+1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
