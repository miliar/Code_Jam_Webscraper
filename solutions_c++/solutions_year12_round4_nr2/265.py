#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FORZ(i,b) FOR(i,0,(b))
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

struct rect {
  int xl, xh, yl, yh;
  rect(int xl, int xh, int yl, int yh): xl(xl), xh(xh), yl(yl), yh(yh) { }
};

struct node {
  rect rt;
  node* l;
  node* r;
  bool ont, onb, onl, onr;
  node(rect rt, bool ont, bool onb, bool onl, bool onr): rt(rt), l(NULL), r(NULL),
    ont(ont), onb(onb), onl(onl), onr(onr) { }
  ~node() { delete l; delete r; }
};

int N,W,L;
int r[1000];
pii ri[1000];
int x[1000];
int y[1000];

bool place(int i, node* n) {
  if (n->l != NULL) {
    if (place(i, n->l)) return true;
    if (place(i, n->r)) return true;
    return false;
  }
  int w = n->rt.xh - n->rt.xl,
    h = n->rt.yh - n->rt.yl;
  int mw = n->onl ? r[i] : 2*r[i];
  int mh = n->ont ? r[i] : 2*r[i];
  int w2 = n->onr ? w + r[i] : w;
  int h2 = n->onb ? h + r[i] : h;
  if (mw > w2 || mh > h2) return false;
  x[i] = n->rt.xl + (n->onl ? 0 : r[i]);
  y[i] = n->rt.yl + (n->ont ? 0 : r[i]);
  if (w <= mw) {
    n->rt.yl += mh;
    n->ont = false;
  } else if (h <= mh) {
    n->rt.xl += mw;
    n->onl = false;
  } else if (h > w) {
    n->l = new node(rect(n->rt.xl+mw, n->rt.xh, n->rt.yl, n->rt.yl+mh), n->ont, false, false, n->onr);
    n->r = new node(rect(n->rt.xl, n->rt.xh, n->rt.yl+mh, n->rt.yh), false, n->onb, n->onl, n->onr);
  } else {
    n->l = new node(rect(n->rt.xl, n->rt.xl+mw, n->rt.yl+mh, n->rt.yh), false, n->onb, n->onl, false);
    n->r = new node(rect(n->rt.xl+mw, n->rt.xh, n->rt.yl, n->rt.yh), n->ont, n->onb, false, n->onr);    
  }
  return true;
}

int main() {
  int tt;
  cin >> tt;
  FOR(t,1,tt+1) {
    printf("Case #%d: ", t);
    cin >> N >> W >> L;
    FORZ(i,N) { cin >> r[i]; ri[i] = make_pair(r[i],i); }
    sort(ri,ri+N,greater<pii>());
    node root(rect(0,W,0,L), true, true, true, true);
    FORZ(i,N) {
      bool b = place(ri[i].second, &root);
      assert(b);
    }
    FORZ(i,N) {
      assert(x[i] >= 0);
      assert(x[i] <= W);
      assert(y[i] >= 0);
      assert(y[i] <= L);
      FOR(j,i+1,N) {
        int dx = x[i] - x[j], dy = y[i] - y[j];
        assert((ll)dx*dx + (ll)dy*dy >= (ll)(r[i]+r[j])*(r[i]+r[j]));
      }
    }
    bool first=true;
    FORZ(i,N) {
      if (!first) cout << " ";
      first=false;
      cout << x[i] << " " << y[i];
    }
    cout << endl;
  }
  return 0;
}
