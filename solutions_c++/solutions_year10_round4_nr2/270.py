#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <fstream>
#include <numeric>
#include <limits.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;

#define ITE(v) typeof(v.begin())
#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORIT(it,v) for(ITE(v) it = v.begin(); it != v.end(); it++)
#define ALL(v) v.begin(), v.end()
#define SZ(v) int(v.size())
#define pb push_back
#define SQR(a) ((a)*(a))
#define OK(y,x) (y >= 0 && y < n && x >= 0 && x < m)

#define INF (1LL<<50)
#define EPS (1e-8)

inline int cmp(double a, double b = 0.0) {
  if (fabs(a-b) <= EPS) return 0;
  if (a < b) return -1;
  return 1;
}


int v[2000];
//int high[2000][2000];
ll memo[2000][2000][11];
ll price[2000][2000];

ll go(int l, int d, int cnt) {
  ll &r = memo[l][d][cnt];
  if (r != -1) return r;
  //cout << "A " << l << " " << d << endl;
  r = 0;
  if (l == d) {
    if (cnt < v[d]) return r = INF;
    return r = 0;
  }
  //nao compra
  ll t1 = 0;
  t1 += go(l,(l+d)/2,cnt);
  t1 += go((l+d)/2+1,d,cnt);
  if (t1 > INF) t1 = INF;
  //compra
  ll t2 = price[l][d];
  t2 += go(l,(l+d)/2,cnt+1);
  t2 += go((l+d)/2+1,d,cnt+1);
  if (t2 > INF) t2 = INF;
  return r = min(t1,t2);
}


int main() {
  int ntests;
  scanf("%d",&ntests);
  FOR(kk,ntests) {
    memset(memo,-1,sizeof(memo));
    printf("Case #%d: ",kk+1);
    int p;
    scanf("%d",&p);
    int n = 1<<p;
    FOR(i,n) {
      scanf("%d",&v[i]);
      v[i] = p-v[i];
    }
    // FOR(i,n) {
    //   for (int j = i; j < n; j++) {
    //     if (j == i) high[i][j] = v[i];
    //     else high[i][j] = max(high[i][j-1],v[j]);
    //     //cout << i << " " << j << " " << high[i][j] << endl;
    //   }
    // }
    int mul = 2;
    FOR(i,p) {
      FOR(j,1<<(p-i-1)) {
        scanf("%lld",&price[mul*j][mul*j+mul-1]);
        //cout << mul*j << " " << mul*j+mul-1 << endl;
      }
      mul *= 2;
    }
    printf("%lld\n",go(0,n-1,0));
  }  
  return 0;
}
