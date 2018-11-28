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
int d, n;
int A[1000], B[1000], N;

uint64_t subprob[500][500];

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
    inFile >> N;

    for0n(j,N) {
      inFile >> A[j] >> B[j];
    }
    
    ans = 0;
    for0n(j,N) {
      for(k = j+1; k < N; k++) {
        if ((A[k] > A[j]) && (B[k] < B[j]))
          ans++;
        if ((A[k] < A[j]) && (B[k] > B[j]))
          ans++;
      }
    }

    outFile << "Case #" << i+1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
