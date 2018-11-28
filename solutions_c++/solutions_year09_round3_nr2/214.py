// BEGIN CUT HERE
#include "cout.h"
// END CUT HERE
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <cmath>
#include <queue>
#include <list>
#include <complex>
#include <iomanip>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef long long LL;
typedef complex<double> CMP;
#define Fill(a, b) memset((a), (b), sizeof(a))
#define REP(a, b) for (size_t (a) = 0; (a)<(size_t)(b); ++(a))
#define sz size()
#define Tr(c, i) for(typeof((c).begin()) i= (c).begin(); (i) != (c).end(); ++(i))
#define All(c) (c).begin(), (c).end()
#define Present(c, x) ((c).find(x) != (c).end()) // for Map or Set
#define CPresent(c, x) (find(All(c), x) != end()) // for vector

#include <assert.h>

long long ipow(int a, int b) {
  long long ret = 1LL;
  REP(i, b)
    ret *= a;
  return ret;
}

int main(void)
{
  int T;
  cin >> T;

  REP(i, T) {
    int N;
    cin >> N;
    long long Sx = 0, Sy = 0, Sz = 0, Vx = 0, Vy = 0, Vz = 0;
    REP(j, N) {
      int x, y, z, vx, vy, vz;
      cin >> x >> y >> z >> vx >> vy >> vz;
      Sx += x;
      Sy += y;
      Sz += z;
      Vx += vx;
      Vy += vy;
      Vz += vz;
    }
    double a, b, c;
    long long sumv;
    double result;
    double sucht;
    double minc;
    c = Sx * Sx + Sy * Sy + Sz * Sz;
    b = 2 * (Sx * Vx + Sy * Vy + Sz * Vz);
    sumv = Vx * Vx + Vy * Vy + Vz * Vz;
    a = sumv;
    if (sumv == 0LL) {
      sucht = 0;
      result = sqrt(c) / N;
    } else {
      minc = c - b * b / (4 * a);
      sucht = - b / (2 * a);
      if (sucht >= 0) {
        result = sqrt(minc) / N;
      } else {
        result = sqrt(c) / N;
        sucht = 0;
      }
    }

    cout << "Case #" << (i+1) << ": ";
    cout << fixed << setprecision(7) << result << ' ' << sucht << endl;
    
  }
  return 0;
}



