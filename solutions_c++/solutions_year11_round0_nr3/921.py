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


//ofstream debug("debug.txt", fstream::trunc);

//
// Add variables here.
//
int nCases;
int c, i, j, k, l;
uint32_t min_can;
uint32_t sum_tot;
uint32_t xor_tot;


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
    min_can = inf;
    sum_tot = 0;
    xor_tot = 0;
    int N;
    inFile >> N;
    for0n(i, N) {
      uint32_t cur;
      inFile >> cur;
      xor_tot ^= cur;
      sum_tot += cur;
      min_can = min(min_can, cur);
    }

    cout << "Case #" << c + 1 << ": ";
    outFile << "Case #" << c + 1 << ": ";
    if (!xor_tot) {
      cout <<  sum_tot - min_can << endl;
      outFile << sum_tot - min_can << endl;
    } else {
      cout << "NO" << endl;
      outFile << "NO" << endl;
    }
  }

  outFile.close();
  return 0;
}
