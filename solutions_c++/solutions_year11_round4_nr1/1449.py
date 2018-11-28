#define _CRT_SECURE_NO_WARNINGS
#pragma comment (linker, "/STACK:16777216")
#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
#include <complex>
#include <windows.h>
using namespace std;

///////////////// macros and typedefs ///////////////////
#define rep(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define repd(i, n) for (int i = (n)-1; i >= 0; --i)
#define _fill(a, x) memset((a), (x), sizeof((a)))
#define DEB(k) cerr<<"debug: "#k<<"="<<k<<endl;
#define all(c) (c).begin(), (c).end()
#define mp(a, b) make_pair(a, b)
#define l(c) (int)((c).size())
#define sqr(a) ((a)*(a))
#define inf 0x7f7f7f7f
#define pb push_back
#define ppb pop_back
#define x first
#define y second
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef pair<int,int> pi;

//#define NAME "my"
#define NAME "A-large"

struct Seg {
   int a, b; 
   int w;
   int pos;
};

bool cmp(Seg s1, Seg s2) { return s1.a < s2.a; }
bool cmp_w(Seg s1, Seg s2) { return s1.w < s2.w; }

int X, S, R, T, n;
vector<Seg> s;

void solution(int test)
{
   s.clear();
   cin >> X >> S >> R >> T >> n;
   rep(i, n) {
      int a, b, w;
      scanf("%d %d %d", &a, &b, &w);
      Seg x;
      x.a = a;
      x.b = b;
      x.w = w;
      x.pos = i;
      s.pb(x);
   }
   //if (test+1 != 12) return;
   sort(all(s), cmp);
   rep(i, n) {
      //if (i == 0 && s[i].a == 0) continue;
      //if (i != 0 && s[i-1].b == s[i].a) continue;
      Seg nxt;
      nxt.a = i == 0 ? 0 : s[i-1].b;
      nxt.b = s[i].a;
      nxt.w = 0;
      nxt.pos = -1;
      if (nxt.a < nxt.b) s.pb(nxt);
      if (i == n-1 && s[n-1].b < X) {
         Seg nxt2;
         nxt2.a = s[n-1].b;
         nxt2.b = X;
         nxt2.w = 0;
         nxt2.pos = -1;
         s.pb(nxt2);
      }
   }
   sort(all(s), cmp_w);
   double ret = 0;
   double t = T;
   int SS = 0;
   rep(i, l(s)) {
      //if (i < l(s)-1 && s[i].b != s[i+1].a) throw 1;
      double dist = s[i].b-s[i].a; SS += dist;
      double need_t = dist / (s[i].w + R);
      if (need_t <= t) {
         t -= need_t;
         ret += need_t;
         continue;
      }
      double dists = (s[i].w + R) * t;
      ret += t;
      dist -= dists;
      ret += dist / (s[i].w + S);
      t = 0;
   }
   if (SS != X)
      throw 1;
   //if (s.back().b != X) throw 1;
   printf("Case #%d: %.6lf\n", test+1, ret, t);
   //cerr << test+1 << endl;
}

int main()
{
#ifdef MY_JUDGE
   freopen(NAME".in", "rt", stdin);
   freopen(NAME".out", "wt", stdout);
   int start = GetTickCount();
#endif
   int t;
   cin >> t;
   rep(i, t)
      solution(i);
#ifdef MY_JUDGE
   int finish = GetTickCount();
   cerr << "Time: " << finish - start << endl;
#endif
   return 0;
}
