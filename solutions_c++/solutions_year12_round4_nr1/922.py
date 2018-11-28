#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <iomanip>

using namespace std;

#define BIG
string PROBLEM = "A" ;

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))
#define REP(i, n) for (int i = 0 ; i < (n) ; i ++)
#define FOR(i, s, n) for (int i = (s) ; i < (n) ; i ++)

typedef long long int64 ;
typedef vector<int> vint ;


#ifdef BIG
ifstream in((PROBLEM + "-large.in").c_str()) ; ofstream out((PROBLEM + "-large.out").c_str()) ;
#endif

#ifndef BIG
ifstream in((PROBLEM + "-small.in").c_str()) ; ofstream out((PROBLEM + "-small.out").c_str()) ;
#endif

int n, length, d [20001], l [20001], dp [20001] ;

int main() {
  ios_base::sync_with_stdio(false) ;

  int numTests ;
  in >> numTests ;
  for (int test = 1 ; test <= numTests ; test ++) {
    in >> n ;
    for (int i = 0 ; i < n ; i ++) { in >> d [i] >> l [i] ; dp [i] = 0 ; }
    in >> length ;
    dp [0] = min(d [0], l [0]) ;
    bool ok = false ;
    int dis ;
    for (int i = 0 ; i < n && !ok ; i ++) {
      if (dp [i] == 0) continue ;
      for (int j = i + 1 ; j < n ; j ++) {
        dis = d [j] - d [i] ;
        if (dp [i] < dis) break ;
        dp [j] = max(dp [j], min(dis, l [j])) ;
      }
      ok = (d [i] + dp [i]) >= length ;
    }

    out << "Case #" << test << ": " << (ok ? "YES" : "NO") << endl ;
  }

  in.close() ;
  out.close() ;

  return 0;
}
