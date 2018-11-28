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

#define SZ 10
#define NAME "C-small-attempt0"
int n, m;
int a[SZ];
int b[SZ];
bool g[SZ][SZ];
vector<vi> rooms;
int R;
int Ret[SZ];
int ret[SZ];
bool used[SZ];

void go(int k, int mx) {
   if (k == n) {
      rep(i, l(rooms)) {
         vi& v = rooms[i];
         _fill(used, 0);
         rep(j, l(v))
            used[ret[ v[j] ]] = true;
         rep(j, mx)
            if (!used[j])
               goto nxt;
      }
      R = mx;
      rep(i, n) Ret[i] = ret[i];
      nxt:;
      return;
   }
   rep(i, mx) {
      ret[k] = i;
      go(k+1, mx);
   }
}

void solution(int test)
{
   rooms.clear();
   _fill(g, 0);
   cin >> n >> m;
   rep(i, m) cin >> a[i];
   rep(i, m) cin >> b[i];
   rep(i, m) {
      a[i]--, b[i]--;
      g[a[i]][b[i]] = g[b[i]][a[i]] = true;
   }
   rep(i, n)
      g[i][(i+1)%n] = g[(i+1)%n][i] = true;
   vi v;
   R = 1;
   rep(i, n) Ret[i] = 0;
   rep(mask, 1<<n) {
      v.clear();
      rep(j, n)
         if ((mask>>j)&1) v.pb(j);
      int M = l(v);
      if (M < 3) goto nxt;
      rep(i, M) {
         int v1 = v[i];
         int v2 = v[(i+1)%M];
         if (!g[v1][v2])
            goto nxt;
      }
      rep(i, M) {
         for (int j = i+1; j < M; j++) {
            if (i == j) continue;
            if (i == (j-1)%M) continue;
            if (i == (j+1)%M) continue;
            if (g[v[i]][v[j]])
               goto nxt;
         }
      }
      rooms.pb(v);
      nxt:;
   }
   if (l(rooms) != m+1)
      throw 1;
   for (int i = 2; i < n; i++) {
      go(0, i);
      if (R != i) break;
   }
   //fprintf(stderr, "Case #%d: %d\n", test+1, R);
   printf("Case #%d: %d\n", test+1, R);
   printf("%d", Ret[0]+1);
   for (int i = 1; i < n; i++) printf(" %d", Ret[i]+1);
   puts("");
}

int main()
{
#ifdef MY_JUDGE
   freopen(NAME".in", "rt", stdin);
   freopen(NAME".out", "wt", stdout);
   int start = GetTickCount();
#endif
   int t;
   scanf("%d\n", &t);
   rep(i, t)
      solution(i);
#ifdef MY_JUDGE
   int finish = GetTickCount();
   cerr << "Time: " << finish - start << endl;
#endif
   return 0;
}
