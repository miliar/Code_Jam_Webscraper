#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <fstream>
#include <sstream>
using namespace std;

#define FS(i,a) for(int i=0;a[i];++i)
#define FD(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,a) for(int i=0;i<a;++i)
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define PR2(a,n,m) REP(i,n){REP(j,m)cout<<a[i][j]<<' ';puts("");}
#define MP make_pair
#define CLQ(que) while(!que.empty()) que.pop();
#define CL(m,what) memset(m,what,sizeof(m))
#define READ(a) freopen(a,"r",stdin)
#define WRITE(a) freopen(a,"w",stdout)
#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define checkMin(a,b) (a=min(a,b))
#define checkMax(a,b) (a=max(a,b))
#define sq(a) ((a)*(a))
#define INF 100000000
#define EPS 1e-8
const double pi = acos(-1.0);
int dx[] = {-1, 0, 1, 0, 1, 1, -1, -1}; //up Right down Left
int dy[] = {0, 1, 0, -1, 1, -1, 1, -1};
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int, int> PII;
//------------------------------------------------------------------------------

int gcd(int a, int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}

LL n, d, g;
int pd, pg;
int gpd;
int gpg;

bool check() {
  return d <= g && d <= n && d * pd / 100 <= g * pg / 100;
}

int main() {
#ifndef ONLINE_JUDGE
  //READ("in");
  //WRITE("out");
#endif
  int T;
  int cas = 0;

  cin >> T;
  while (T--) {
    printf("Case #%d: ", ++cas);
    cin >> n >> pd >> pg;
    if (n == 3 && pd == 0 && pg == 0) {
      //puts("----------");
    }
    if (pg == 100) {
      if (pd == 100) {
        puts("Possible");
      } else {
        puts("Broken");
      }
      continue;
    }
    if (pg == 0) {
      if (pd == 0) {
        puts("Possible");
      } else {
        puts("Broken");
      }
      continue;
    }
    if (pd == 0) {
      puts("Possible");
      continue;
    }
    gpd = gcd(pd, 100);
    gpg = gcd(pg, 100);
    
    g = 100 / gpg;
    d = 100 / gpd;
    //cout << n << " " << pd << " " << pg << endl;
//    printf("%d %d\n", gpd, gpg);
//    printf("%lld %lld\n", d, g);
    if (d > n) {
      puts("Broken");
      continue;
    }
    assert(100 % gpg == 0 && 100 % gpd == 0);
    while (!check()) {
      g *= 100 / gpg;
    }
    //printf("%lld %lld\n", d, g);
    puts("Possible");
  }
  return 0;
}