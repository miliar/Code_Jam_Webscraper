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

vector<int> bbut;
vector<int> obut;
vector<pii> steps;

//
// Add variables here.
//
int nCases;
int c, i, j, k, l;
int ans;

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
    int bloc = 1;
    int oloc = 1;
    ans = 0;
    bbut.clear();
    obut.clear();
    steps.clear();

    int buttons;

    inFile >> buttons;
    for0n(i, buttons) {
      char color;
      int pos;
      inFile >> color >> pos;
      
      if (color == 'B') {
        bbut.push_back(pos);
        steps.push_back(make_pair(true, pos));
      } else {
        obut.push_back(pos);
        steps.push_back(make_pair(false, pos));
      }
    }
    bbut.push_back(inf);
    obut.push_back(inf);

    vector<int>::iterator bit = bbut.begin();
    vector<int>::iterator oit = obut.begin();
    vector<pii>::iterator sit = steps.begin();
    int bdist = abs(bloc - *bit);
    int odist = abs(oloc - *oit);

    while (sit != steps.end()) {
      int time = min(bdist, odist);
      if (time != 0) {
        bdist -= time;
        odist -= time;
        cout << time << endl;
        ans += time;
      } else {
        if ((bdist == 0) && ((*sit).first)) {
          // Push blue button
          ans++;
          sit++;
          bloc = *bit;
          bit++;
          bdist = abs(bloc - *bit);

          odist--;
          if (odist < 0) {
            odist = 0;
          }
        } else if ((odist == 0) && !((*sit).first)) {
          // Push orange button
          ans++;
          sit++;
          oloc = *oit;
          oit++;
          odist = abs(oloc - *oit);

          bdist--;
          if (bdist < 0) {
            bdist = 0;
          }
        } else {
          // One guy is waiting. Increment time by the longer and set
          // both distances to 0.
          time = max(bdist, odist);
          bdist = odist = 0;
          cout << time << endl;
          ans += time;
        }
      }
    }

    cout << "Case #" << c + 1 << ": " << ans << endl;

    outFile << "Case #" << c + 1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
