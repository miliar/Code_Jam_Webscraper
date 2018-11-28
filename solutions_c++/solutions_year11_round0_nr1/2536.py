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

#define NAME "A-large"

int n;
vector<pi> v;

void solution(int test)
{
   cin >> n;
   v.clear();
   rep(i, n) {
      char c;
      int k;
      cin >> c >> k;
      v.pb(pi(c == 'B', k));
   }
   int time = 0;
   int k1 = 1, k2 = 1;
   for (int i = 0; i < n; ) {
      int nxt1 = -1, nxt2 = -1;
      for (int j = i; j < n; j++)
         if (v[j].x == 0 && nxt1 == -1) nxt1 = v[j].y; else
         if (v[j].x == 1 && nxt2 == -1) nxt2 = v[j].y;
      if (v[i].x == 0) {
         if (v[i].y != nxt1) throw 1;
         if (k1 == v[i].y) i++;
         else if (k1 < v[i].y) k1++;
         else k1--;
         if (nxt2 != -1 && k2 < nxt2) k2++;
         else if (nxt2 != -1 && k2 > nxt2) k2--;
      }
      else {
         if (v[i].y != nxt2) throw 1;
         if (k2 == v[i].y) i++;
         else if (k2 < v[i].y) k2++;
         else k2--;
         if (nxt1 != -1 && k1 < nxt1) k1++;
         else if (nxt1 != -1 && k1 > nxt1) k1--;
      }
      time++;
   }
   printf("Case #%d: %d\n", test+1, time);
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
