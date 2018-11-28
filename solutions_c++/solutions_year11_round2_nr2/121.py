#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
#include <cstring>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define FS first
#define SD second
#define MP make_pair
#define eps 1e-7

LL X[1000100];
int n;
LL d;

bool check(LL m) {
  if(n==1) return true;
  LL gran = X[0] - m + d;
  FOR(i, 1, n) {
    if (X[i] < gran) {
      LL a = gran-X[i];
      if (a<=m) {
        gran += d;
      }
      else {
        return false;
      }
    }
    else {
      LL a = X[i]-gran;
      if (a<=m) {
        gran += d;
      }
      else {
        gran = X[i] + d - m;
      }

    }
  }
  return true;
}

int main() {
  int t;scanf("%d",&t);
  FORE(test,1,t) {
    int c;scanf("%d%lld",&c,&d);
    d = d*2;
    n = 0;
    FOR(i,0,c) {
      int p,v;scanf("%d%d",&p,&v);
      FOR(j,0,v) {
        X[n++] = 2*p;
      }
    }
    LL left = 0, right = 1000000000000000000ll;
    LL best = right;

    while(left<=right) {
      LL mid = (left+right)/2;
      if (check(mid)) {
        best = mid;
        right = mid - 1;
      }
      else {
        left = mid + 1;
      }
    }
    printf("Case #%d: %lf\n", test, best/2.0);
  }

}
