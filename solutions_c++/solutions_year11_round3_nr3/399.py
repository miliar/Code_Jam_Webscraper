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
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
typedef long long ll;

void getfactor(set<int> &lf, int x) {
  int k = 2;
  while(x > 1) {
    while(x%k == 0) {
      lf.insert(k);
      x /= k;
    }

    k++;
  }

  return;
}

int main() {

  int t, nada[10005];
  cin >> t;
  REP(i,t) {
    int n,l,h;
    set<int> yatta;
    cin >> n >> l >> h;
    REP(j, n) {
      cin >> nada[j];
      //getfactor(yatta, nada[j]);
    }

    int k;
    for(int j=l;j<=h;j++) {
      for(k=0;k<n;k++) {
        if(nada[k]%j!=0 && j%nada[k]!=0)
          break;
      }

      if(k==n) {
        cout << "Case #" << i+1 << ": " << j << "\n";
        goto slese;
      }
    }

    cout << "Case #" << i+1 << ": NO\n";
    slese:;

//    int hasil = 1;
//    for(set<int>::iterator it=yatta.begin(); it!=yatta.end(); it++) {
//      hasil *= *it;
//      if(hasil > h) break;
//    }
//
//    cout << "Case #" << i+1 << ": ";
//    if(hasil > h || hasil < l) {
//      cout << "NO\n";
//    } else {
//      cout << hasil << "\n";
//    }
  }


  return 0;
}

