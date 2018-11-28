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
#include <iomanip>
#include <assert.h>
#include <list>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef long long ll;

#define ITE(v) typeof(v.begin())
#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORIT(it,v) for(ITE(v) it = v.begin(); it != v.end(); it++)
#define ALL(v) v.begin(), v.end()
#define SZ(v) int(v.size())
#define pb push_back
#define SQR(a) ((a)*(a))

#define INF 0x3f3f3f3f
#define EPS (1e-9)

inline int cmp(double a, double b = 0.0) {
  if (fabs(a-b) <= EPS) return 0;
  if (a < b) return -1;
  return 1;
}



int s,r,x,t,n;

int beg[1002],end[1002],vel[1002];
int id[1002];

bool cmpp(int a, int b) {
  return vel[a] < vel[b];
}

int main() {
  int ncases;
  scanf("%d",&ncases);
  FOR(ccases,ncases) {
    printf("Case #%d: ",ccases+1);
    scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
    int sum = 0;
    FOR(i,n) {
      scanf("%d %d %d",&beg[i],&end[i],&vel[i]);
      id[i] = i;
      sum += end[i]-beg[i];
    }
    beg[n] = 0;
    end[n] = x-sum;
    vel[n] = 0;
    id[n] = n;
    n++;
    sort(id,id+n,cmpp);
    double res = 0;
    double tt = t;
    FOR(ii,n) {
      int i = id[ii];
      double dx = end[i]-beg[i];
      double dt = dx/(vel[i]+r);
      double at = min(dt,tt);
      tt -= at;
      double rdx = at*(vel[i]+r);
      double ndt = (dx-rdx)/(vel[i]+s);
      res += at + ndt;
    }
    printf("%.7lf\n",res);
  }
  return 0;
}
