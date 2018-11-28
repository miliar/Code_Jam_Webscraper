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
using namespace std;
typedef long long LL;
#define INF 2000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define X first
#define Y second
#define MP make_pair
#define FF fflush(stdout);


int main() {
  int T;scanf("%d",&T);
  FORE(test,1,T) {
    int n, ret = 0;
    scanf("%d",&n);
    FOR(i,0,n) {
      int a;scanf("%d",&a);
      if (a != i + 1) ret++;
    }
    printf("Case #%d: %d\n", test, ret);


  }

}
