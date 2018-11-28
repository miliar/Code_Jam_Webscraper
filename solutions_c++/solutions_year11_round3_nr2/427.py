//#define debug#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ(v) ((long long)(v).size())
#define FOR(i,a,b) for(long long i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(long long i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
typedef long long ll;

long long jarak[1000010], total[1000010], tk;

int main() {

  int t;
  cin >> t;
  REP(i, t) {
    long long l,tt,n,c;
    bool belum = true;
    cin >> l >> tt >> n >> c;
    jarak[0] = total[0] = 0;
    tk = 0;
    REP(j,c) {
      cin >> jarak[j+1];
      jarak[j+1] *= 2;
      total[j+1] = total[j] + jarak[j+1];
      if(total[j+1] >= tt && belum) {
        jarak[n+1] = total[j+1] - tt;
        tk = j+1;
        belum = false;
      }
    }

    FOR(j, c, n+1) {
      jarak[j] = jarak[(j-1)%c+1];
      total[j] = total[j-1] + jarak[j];
    }

    sort(&jarak[tk+1],&jarak[n+2]);
    long long hehe = total[n];
    long long j = n+1;
    REP(k, l) {
      hehe -= jarak[j]/2;
      j--;
    }
    cout << "Case #" << i+1 << ": " << hehe << "\n";
  }

  return 0;
}

