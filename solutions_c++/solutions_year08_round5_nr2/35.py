#include <algorithm>
#include <bitset>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <ext/hash_set>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
using namespace std;
using namespace __gnu_cxx;
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,v) FOR(i,(int)v.size())
#define BEND(v) v.begin(),v.end()
//#define dump(x) cerr << #x << " = " << (x) << endl;
#define dump(x)
typedef long long ll; typedef long double ld;

int cas = 0;
int dr[] = { 0, -1, 0, 1},
    dc[] = { 1, 0, -1, 0};
struct State {
  int r,c,br,bc,rr,rc,d;
};
bool operator<(const State& a, const State& b) {
  if (a.r != b.r) return a.r<b.r;
  if (a.c != b.c) return a.c<b.c;
  if (a.br != b.br) return a.br<b.br;
  if (a.bc != b.bc) return a.bc<b.bc;
  if (a.rr != b.rr) return a.rr<b.rr;
  if (a.rc != b.rc) return a.rc<b.rc;
  return false;
}
bool operator==(const State& a, const State& b) {
  return a.r == b.r
      && a.c == b.c
      && a.br == b.br
      && a.bc == b.bc
      && a.rr == b.rr
      && a.rc == b.rc;
}
namespace __gnu_cxx {
  template<>
  struct hash<State> {
    size_t operator()(const State& s) const {
      size_t h = 0;
      h = h*47+s.r;
      h = h*47+s.c;
      h = h*47+s.br;
      h = h*47+s.bc;
      h = h*47+s.rr;
      h = h*47+s.rc;
      return h;
    }
  };
}
int R,C;
char grid[32][32];
int gotor[32][32][4];
int gotoc[32][32][4];
void doit() {
  dump("STARTING ******************");
  scanf("%d%d",&R,&C);

  FOR(r,32) FOR(c,32) grid[r][c] = '#';

  int sr=-1,sc=-1,cr=-1,cc=-1;
  FOR(r,R) FOR(c,C) {
    scanf(" %c",&grid[r+1][c+1]);
    if (grid[r+1][c+1] == 'O') {
      sr = r+1;
      sc = c+1;
    }
    if (grid[r+1][c+1] == 'X') {
      cr = r+1;
      cc = c+1;
    }
  }
  assert(sr != -1 && cr != -1);
  assert(grid[sr][sc] == 'O');
  assert(grid[cr][cc] == 'X');

  memset(gotor,-1,sizeof(gotor));
  memset(gotoc,-1,sizeof(gotoc));
  FOR(r,32) FOR(c,32) if (grid[r][c] != '#') {
    FOR(k,4) {
      int r2=r,c2=c;
      while (grid[r2+dr[k]][c2+dc[k]] != '#') {
	r2 += dr[k];
	c2 += dc[k];
      }
      gotor[r][c][k] = r2;
      gotoc[r][c][k] = c2;

      assert(gotor[r][c][k] == r || gotoc[r][c][k] == c);
    }
  }
  dump(gotor[1][1][2]);
  dump(gotoc[1][1][2]);
  dump(cr);
  dump(cc);

  State init;
  init.r = sr;
  init.c = sc;
  init.br = -1;
  init.bc = -1;
  init.rr = -1;
  init.rc = -1;
  init.d = 0;

  hash_set<State> mark;
  deque<State> q;
  q.push_back(init);
  mark.insert(init);

  int ans = -1;

  while (q.size()) {
    State s = q.front();
    q.pop_front();
    assert(grid[s.r][s.c] != '#');
    dump("====");
    dump(s.r);
    dump(s.c);
    dump(s.br);
    dump(s.bc);
    dump(s.rr);
    dump(s.rc);
    dump(s.d);
    if (grid[s.r][s.c] == 'X') {
      ans = s.d;
      break;
    }

    FOR(k,6) {
      int r2=-1,c2=-1;
      if (k < 4) {
	r2 = s.r+dr[k];
	c2 = s.c+dc[k];
      } else if (k == 4) {
	if (s.r!=s.br || s.c != s.bc || s.rr == -1) continue;
	r2 = s.rr;
	c2 = s.rc;
      } else {
        assert(k == 5);
	if (s.r != s.rr || s.c != s.rc || s.br == -1) continue;
	r2 = s.br;
	c2 = s.bc;
      }
      assert(r2 != -1);
      assert(c2 != -1);

      if (grid[r2][c2] != '#') {
	State n = s;
	n.r = r2;
	n.c = c2;
	n.d++;

	if (!mark.count(n)) {
	  mark.insert(n);
	  q.push_back(n);
	}
      }
    }

    FOR(k,2) {
      FOR(d,4) {
	State n = s;

	int xr,xc;
	if (k) {
	  n.br = gotor[s.r][s.c][d];
	  n.bc = gotoc[s.r][s.c][d];
	  xr = n.br;
	  xc = n.bc;
	} else {
	  n.rr = gotor[s.r][s.c][d];
	  n.rc = gotoc[s.r][s.c][d];
	  xr = n.rr;
	  xc = n.rc;
	}
	//dump(s.r); dump(s.c); dump(d);
	assert(xr != -1); assert(xc != -1);
	dump("???");
	dump(s.r);
	dump(s.c);
	dump(xr);
	dump(xc);

	if (!mark.count(n)) {
	  mark.insert(n);
	  q.push_front(n);
	}
      }
    }
  }

  printf("Case #%d: ",++cas);
  if (ans != -1) {
    printf("%d\n",ans);
  } else {
    printf("THE CAKE IS A LIE\n");
  }
  cerr << "ding" << cas << endl;
}
int T;
int main() {
scanf("%d",&T);
FOR(i,T)doit();
}
