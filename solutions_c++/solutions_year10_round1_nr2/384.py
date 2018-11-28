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

#define INF 0x3f3f3f3f
#define EPS (1e-8)

inline int cmp(double a, double b = 0.0) {
  if (fabs(a-b) <= EPS) return 0;
  if (a < b) return -1;
  return 1;
}

int d,i,m,n;
int vec[110];

int pd[110][260];

#define MAXV 255

int fix(int a, int b) {
  return (m != 0 ? i*((abs(a-b)+m-1)/m) : i*abs(a-b));
}

int go(int p, int v) {
  int &r = pd[p][v];
  if (r != -1) return r;
  r = d*(p+1) + i;
  if (p) r = min(r,go(p-1,v) + d);
  if (m == 0) {
    r = min(r,abs(v-vec[p]) + (p == 0 ? 0 : go(p-1,v)));
    //cout << vec[p] << " " << v << " " << r << endl;
    return r;
  }
  FOR(j,MAXV+1) {
    int left = max(0,j-m);
    int right = min(MAXV,j+m);
    int minv = INF;
    if (p) while (left <= right) minv = min(minv,go(p-1,left++));
    else minv = 0;
    r = min(r,minv + abs(j-vec[p]) + (m != 0 ? i*((abs(v-j)+m-1)/m) : i*abs(v-j)));
  }
  return r;
}

int main() {
  int ntest;
  scanf("%d",&ntest);
  int kk = 1;
  while (ntest--) {
    memset(pd,-1,sizeof(pd));
    printf("Case #%d: ",kk++);
    scanf("%d %d %d %d",&d,&i,&m,&n);
    FOR(i,n) {
      scanf("%d",&vec[i]);
    }
    int best = d*n;
    FOR(i,MAXV+1) {
      best = min(best,go(n-1,i));
    }
    cout << best << endl;
  }  
  return 0;
}
