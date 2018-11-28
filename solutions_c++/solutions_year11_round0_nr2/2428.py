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

#define NAME "B-large"
int c, d, n;
char G[256][256];
bool B[256][256];

void solution(int test)
{
   _fill(G, -1);
   _fill(B, 0);
   cin >> c;
   rep(i, c) {
      string s;
      cin >> s;
      if (l(s) != 3) throw 1;
      G[s[0]][s[1]] = G[s[1]][s[0]] = s[2];
   }
   cin >> d;
   rep(i, d) {
      string s;
      cin >> s;
      if (l(s) != 2) throw 1;
      B[s[0]][s[1]] = B[s[1]][s[0]] = true;
   }
   cin >> n;
   string s;
   cin >> s;
   if (l(s) != n) throw 1;
   vector<char> s2;
   s2.push_back(s[0]);
   for (int i = 1; i < n; i++) {
      char ch = s[i];
      while (!s2.empty() && G[s2.back()][ch] != -1) {
         ch = G[s2.back()][ch];
         s2.pop_back();
      }
      s2.pb(ch);
      for (int j = l(s2)-2; j >= 0; j--)
         if (B[s2[j]][s2.back()]) {
            s2.clear();
            break;
         }
   }
   printf("Case #%d: [", test+1);
   for (int i = 0; i < l(s2)-1; i++)
      printf("%c, ", s2[i]);
   if (l(s2) > 0)
      printf("%c", s2[l(s2)-1]);
   printf("]\n");
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
