#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <cmath>
#include <set>
#include <queue>
#include <cstring>
#include <fstream>
using namespace std;
typedef long long LL;

#define INF 2000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define FS first
#define SD second
#define MP make_pair


int main() {
  int T;scanf("%d",&T);
  FORE(test,1,T) {
    int n, s = 0, m = 1000000, x = 0;;
    scanf("%d",&n);
    FOR(i,0,n) {
      int a;scanf("%d",&a);
      if (a < m) m = a;
      s += a;
      x ^= a;
    }
    if (x == 0) {
      printf("Case #%d: %d\n", test, s - m);
    }
    else {
      printf("Case #%d: NO\n", test);
    }
  }

}
