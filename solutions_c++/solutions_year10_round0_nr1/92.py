#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <functional>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SZ(a) ((int)((a).size()))
#define REPSZ(i,v) REP(i,SZ(v))
#define ALL(a) (a).begin(),(a).end()
typedef long long Int;
template<class T> inline T sq(T x){return x * x;}
template<class T> inline void checkmin(T &a,T b){if(b<a)a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a)a=b;}

int main() {
  int TNO;
  scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
    printf("Case #%d: ", tno);

    int N, K; scanf("%d%d", &N, &K);
    int mask = (1 << N) - 1;
    if( (K & mask) == mask )
      cout << "ON" << endl;
    else
      cout << "OFF" << endl;
  }
}
