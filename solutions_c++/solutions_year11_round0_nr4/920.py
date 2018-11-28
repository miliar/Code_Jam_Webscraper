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

int move[4][2] = { {-1, 0} , {1, 0} , {0, -1} , {0, 1} };

uint32_t ncr[1000][1000];
void make_ncr()
{
  int x, y;
  for0n(x, 1000) {
    for0n(y, x) {
      ncr[x][y] = 0;
    }
    ncr[x][x] = 1;
    ncr[x][0] = 1;
    ncr[x][1] = x;
  }

  for(x = 3; x < 1000; x++) {
    for(y = 2; y < x ; y++) {
      ncr[x][y] = ncr[x-1][y] + ncr[x-1][y-1];
    }
  }
}

//
// Add variables here.
//
int nCases;
int c, i, j, k, l;
double solved[1000];
double ans;

double prob(int x, int y) 
{
  cout << "prob " << x << ", " << y << endl;
  double ret = double(ncr[x][y]);
  cout << "- ncr " << ret << endl;
  

  int count;
  for(count = 1; count < x - y; count++) {
    ret *= double(count);
  }
  for(count = 1; count <= x; count++) {
    ret /= double(count);
  }
  cout << "- ret " << ret << endl;
  return ret;
}

void solve(int mismatch)
{
  double ex = 1.0;
  cout << "Solving " << mismatch << ": " << endl;

  int count;
  for(count = 2; count < mismatch; count++) {
    double toadd = (solved[count] * prob(mismatch, mismatch - count));
    cout << count << " solved " << solved[count] << endl;
    cout << count << " adds " << toadd << endl;
    ex += toadd;
  }
  cout << endl;

  double div = 1.0;
  div -= prob(mismatch, 0);
  cout << "ex / div " << ex << "/" << div << endl;
  ex /= div;

  solved[mismatch] = ex;
  cout << "final " << ": " << ex << endl;
}

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

  make_ncr();
#if 0
  for0n(i, 1000) {
    solved[i] = 0.0;
  }
  solved[2] = 2.0; // Reasonable base case, but could be done in algorithm...
  for(i = 3; i < 5; i++) {
    solve(i); // Get the rest.
  }
#endif

  for0n(c,nCases) {
    ans = 0.0;

    int N;
    inFile >> N;
    for1n(i, N) {
      // Ok, this is a little silly. But what can you expect from a 4-armed
      // man with thousands of fingers?
      int cur;
      inFile >> cur;
      if (cur != i) {
        ans += 1.0;
      }
    }

    cout << "Case #" << c + 1 << ": " << fixed << ans << endl;

    outFile << "Case #" << c + 1 << ": " << fixed << ans << endl;
  }

  outFile.close();
  return 0;
}
