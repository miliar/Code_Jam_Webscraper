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

int B[2000];
int E[2000];
int w[2000];


double count(int S, int walk_speed, int run_speed, double& left) {
  double tim = (double)S/(double)(run_speed);
  if (left > tim) {
    left -= tim;
    return tim;
  }
  else {
    double ret = left;
    tim = ((double)S-left*(double)run_speed)/(double)walk_speed;
    left = 0.0;
    ret += tim;
    return ret;
  }
}

pair<int, pair<int,int> > seg[10000];
int main() {
  int t;scanf("%d",&t);
  FORE(test,1,t) {
    int x,s,r,n,t;scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
    FOR(i,0,n) {
      scanf("%d%d%d",&seg[i].SD.FS,&seg[i].SD.SD,&seg[i].FS);
      B[i] = seg[i].SD.FS;
      E[i] = seg[i].SD.SD;
    }
    int k = n;
    int cur = 0;
    int p = 0;
    while (p<x) {
      int target;
      if (cur < n && p == B[cur]) {
        target = E[cur];
        cur++;
      }
      else {
        if (cur == n) target = x;
        else target = B[cur];
        seg[k].SD.FS = p;
        seg[k].SD.SD = target;
        seg[k++].FS = 0;
      }
      p = target;
    }
    sort(seg, seg+k);
    double ret =0.0;
    double left = t;
    FOR(i,0,k) {
      ret += count(seg[i].SD.SD-seg[i].SD.FS, seg[i].FS + s, seg[i].FS + r, left);
    }

    printf("Case #%d: %.10lf\n", test,ret);
  }


}
