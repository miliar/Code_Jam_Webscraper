#include <algorithm>
#include <bitset>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
using namespace std;
#define FR(i,a,b) for(int i=a;i<b;i++)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,v) FOR(i,(int)v.size())
#define BEND(v) v.begin(),v.end()
#define dump(x) cerr << #x << " = " << (x) << endl;
typedef long long ll; typedef long double ld;

typedef complex<ll> cpx;
#define X real()
#define Y imag()

const int inf = 123456789;
int cas = 0;
int L;
const int o = 3000;
void doit() {
  scanf("%d",&L);

  cpx p;
  cpx dir(0,1);
  vector<cpx> pts;
  FOR(i,L) {
    char buf[128];
    int T;
    scanf(" %s%d",buf,&T);
    
    FOR(j,T) {
      for (char* ps = buf; *ps; ++ps) {
	pts.push_back(p);
	if (*ps == 'F') {
	  p += dir;
	} else if (*ps == 'L') {
	  dir *= cpx(0,1);
	} else if (*ps == 'R') {
	  dir *= cpx(0,-1);
	} else {
	  assert(0);
	}
      }
    }
  }

  int rlb[6001],rub[6001],clb[6001],cub[6001];
  FR(r,-o,o+1) {
    rlb[o+r] = clb[o+r] = inf;
    rub[o+r] = cub[o+r] = -inf;
  }

  int A=0;
  FORI(i,pts) {
    int j = (i+1)%(int)pts.size();
    int r = pts[i].Y, c = pts[i].X;
    rlb[o+r] <?= c;
    rub[o+r] >?= c;
    clb[o+c] <?= r;
    cub[o+c] >?= r;

    p = pts[i];
    cpx q = pts[j];

    A += (conj(p)*q).Y;
  }
  A = abs(A);
  assert(0==A%2);
  A/=2;

  int C = 0;
  FR(r,-o,o+1) FR(c,-o,o+1) {
    int ok = (c<o && clb[o+c] <= r && r < cub[o+c] && clb[o+c+1] <= r && r < cub[o+c+1])
      || (r<o && rlb[o+r] <= c && c < rub[o+r] && rlb[o+r+1] <= c && c < rub[o+r+1]);
    if (ok) {
      C++;
    }
  }

  int ans = C-A;

  printf("Case #%d: %d\n",++cas,ans);
  cerr << "ding" << cas;
}
int T;
int main() {
scanf("%d",&T);
FOR(i,T)doit();
}
