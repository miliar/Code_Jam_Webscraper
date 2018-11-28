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
#include <iomanip>
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
double ans;

int X, S, R, T, N;
int B[1000];
int E[1000];
int w[1000];
//map<int, vector<pair<int, int> > > regions;
map<int, int> regions;


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
    ans = 0.0;
    regions.clear();
    //ZERO(B);
    //ZERO(E);
    //ZERO(w);

    inFile >> X >> S >> R >> T >> N;
    int st = 0;
    int en = 0;
    for0n(i, N) {
      inFile >> B[i] >> E[i] >> w[i];
      en = B[i];
      if (st != en) {
        // add region of walking speed.
        //regions[S].push_back(make_pair(st, en));
        regions[S] += (en - st);
        cout << "walk from " << st << " to " << en << endl;
      }
      // add region of walkway.
      st = B[i];
      en = E[i];
      cout << "path from " << st << " to " << en << ": " << w[i] << endl;
      //regions[w[i]].push_back(make_pair(st, en));
      regions[w[i] + S] += (en - st);
      st = E[i];
    }

    // Check for end walking
    en = X;
    if (st != en) {
      // add region of walking speed.
      //regions[S].push_back(make_pair(st, en));
      regions[S] += (en - st);
      cout << "walk from " << st << " to " << en << endl;
    }

    // iterate over map and run on the slowest lengths.
    map<int, int>::iterator mit = regions.begin();
    double runtime = T;
    double speed, len;
    while (mit != regions.end()) {
      speed = (*mit).first;
      len = (*mit).second;

      if (runtime > 0.0) {
        // Run for as long as poss.
        double rd = (speed + R - S) * runtime;
        if (rd > len) {
          // Run as far as poss, save rest
          double rt = (len / (speed + R - S));
          ans += rt;
          runtime -= rt;
        } else {
          // Two segs. Running and walking.
          double d1 = (speed + R - S) * runtime;
          double d2 = len - d1;
          ans += (d1 / (speed + R - S));
          ans += (d2 / (speed));
          runtime = 0.0;
        }
      } else {
        ans += (len / speed); 
      }
      mit++;
    }

    cout << "Case #" << c + 1 << ": " << fixed << setw(10) << ans << endl;

    outFile << "Case #" << c + 1 << ": " << fixed << setw(10) << ans << endl;
  }

  outFile.close();
  return 0;
}
