#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

struct part {
  int x,y,w,l;
  long long area;
  part(int x, int y, int w, int l) : x(x), y(y), w(w), l(l) {
    area = w;
    area *=l;
  }
};

int n,W,L;
pair <int,int> r[1111];
int resx[1111], resy[1111];

void solve(int testcase) {
  printf("Case #%d: ", testcase);
  eprintf("Case #%d: ", testcase);
  scanf("%d%d%d", &n, &W, &L);
  for (int i=0; i<n; ++i) {
    scanf("%d",&r[i].fi);
    r[i].se=i;
  }
  vector <part> p;
  p.pb(part(0,0,W,L));
  sort(r,r+n);
  reverse(r,r+n);
  for (int i=0; i<n; ++i) {
    int t=r[i].fi;
    int k=-1, left=-1;
    int ii=r[i].se;
    for (int j=0; j<sz(p); ++j) {
      int ww = 2*t, ll = 2*t;
      if (p[j].x == 0) ww = t;
      if (p[j].y == 0) ll = t;
      if ((p[j].x == 0 || ww <= p[j].w) && 
          (p[j].y == 0 || ll <= p[j].l)) {
        long long aa = ww;
        aa *= ll;
        if (k == -1 || left>p[j].area - aa) {
          k=j;
          left=p[j].area-aa;
        }
      }
    }
    if (k == -1) {
      cerr << "TESTCASE " << testcase << " FAILED" << endl;
      assert(false);
    }
    part cur = p[k];
    swap(p[k], p[sz(p)-1]);
    p.pop_back();

    int ww = t*2, ll = 2*t;
    if (cur.x == 0) ww = t;
    if (cur.y == 0) ll = t;

    resx[ii] = cur.x + ww - t;
    resy[ii] = cur.y + ll - t;

    if (cur.w < cur.l) {
      if (cur.l-ll > 0) 
        p.pb(part(cur.x, cur.y+ll, cur.w, cur.l-ll));
      if (cur.w-ww > 0)
        p.pb(part(cur.x+ww, cur.y, cur.w-ww, ll));
    } else {
      if (cur.l-ll > 0)
        p.pb(part(cur.x, cur.y+ll, ww, cur.l-ll));
      if (cur.w-ww > 0)
        p.pb(part(cur.x+ww, cur.y, cur.w-ww, cur.l));
    }
  }
  for (int i=0; i<n; ++i)
    printf("%d %d%c", resx[i], resy[i], " \n"[i+1==n]);
  for (int i=0; i<n; ++i)
    eprintf("%d %d%c", resx[i], resy[i], " \n"[i+1==n]);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; ++i)
    solve(i);
  return 0;
}
