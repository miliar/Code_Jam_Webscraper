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

int i, j, k, l, ans;
int nCases;
uint64_t L, P, C, cur, tests;

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
    inFile >> L >> P >> C;
    ans = tests = 0;
    cur = L;
    while ((cur * C < P)) {
      cur *= C;
      //cout << cur << " ";
      tests++;
    }
    //cout << tests << " " << endl;
    while (tests > 0) {
      tests /= 2;
      ans++;
    }
    
    outFile << "Case #" << i+1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
