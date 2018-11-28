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

int cas, i, j, k, l, ans;
int nCases;
int d, n;
const int maxTeam = 2<<10;
int M[maxTeam];
bool willSee[10][maxTeam];
int cost[10][maxTeam];


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
    for0n(i,10) {
      for0n(j, maxTeam) {
        willSee[i][j] = false;
      }
    }
    int P;
    inFile >> P;
    for0n(i, 1<<P) {
      inFile >> M[i];
    }
    for0n(i, P) {
      int from, to;
      from = 0;
      to = (2<<i)-1;
      for0n(j, 1<<(P - i - 1)) {
        int incost;
        inFile >> incost;
        for(k = from; k <= to; k++) {
          cost[i][k] = incost;
        }
        from = to+1;
        to = from+(2<<i)-1;
      }
    }
    ans = 0;

    for0n(i, P) {
      for0n(j, 1 << P) {
        if (M[j] <= 0) {
          // Have to buy a ticket.
          // For small case all tickets cost 1.
          int lowCost = 1;
          int lowRound = i;
#if 0
          for(k = i; k >= 0; k--) {
            if (lowCost > cost[k][j]) {
              lowCost = cost[k][j];
              lowRound = k;
            }
          }
#endif
          // Mark everyone above that as a game watched.
          int bracket = (2<<lowRound);
          int from = j - (j % bracket);
          int to = from + bracket -1;
          for(k = from; k <= to; k++) {
            M[k]++;
          }
          ans += lowCost;
        }
        M[j]--;
      }
    }
    outFile << "Case #" << cas+1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
