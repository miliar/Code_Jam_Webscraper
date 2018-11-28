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
char s[107];
char g[100][100];
double wp[100];
double owp[100];
double oowp[100];

// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

void solution(int test)
{
   scanf("%d\n", &n);
   rep(i, n) {
      gets(s);
      rep(j, n) g[i][j] = s[j];
   }
   fill(wp, wp+n, 0);
   fill(owp, owp+n, 0);
   fill(oowp, oowp+n, 0);
   rep(i, n) {
      int t = 0, w = 0;
      rep(j, n) if (g[i][j] != '.') {
         if (g[i][j] == '1') w++;
         t++;
      }
      wp[i] = w*1./t;
   }
   rep(i, n) { // me
      double tot = 0;
      int cnt = 0;
      rep(j, n) if (g[i][j] != '.') { // op
         cnt++;
         int t = 0, w = 0;
         rep(k, n) { // op2 
            if (k == i) continue;
            if (g[j][k] != '.') {
               if (g[j][k] == '1') w++;
               t++;
            }
         }
         tot += w*1./t;
      }
      owp[i] = tot / cnt;
   }
   rep(i, n) {
      double tot = 0;
      int cnt = 0;
      rep(j, n) if (g[i][j] != '.') {
         tot += owp[j];
         cnt++;
      }
      oowp[i] = tot / cnt;
   }

   printf("Case #%d:\n", test+1);
   rep(i, n) {
      double rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
      printf("%.6lf\n", rpi);
   }
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
