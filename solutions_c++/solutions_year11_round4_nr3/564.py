#include <functional>
#include <algorithm>
#include <utility>
#include <cassert>
#include <cmath>
#include <ctime>

#include <numeric>
#include <iomanip>
#include <complex>
#include <float.h>
#include <cfloat>

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <cstdio>

#include <cstring>
#include <string>

#include <iterator>
#include <vector>
#include <bitset>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define foreach(it, v, type) for( type::iterator it = v.begin(); it != v.end() ; it++)
#define forn(i, st, en) for(int i = (int)(st); i <= (int)(en); i++)
#define ford(i, en, st) for(int i = (int)(en); i >= (int)(st); i--)
#define zero(a, w) memset(a, w, sizeof(a))
#define all(a) a.begin(), a.end()
#define sz(a) a.size()

#define msg(x) cout << #x << " = " << x << endl;
const int n = 1010;

bool was[1001000];

int main() {
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 
 int t;
 cin >> t;

 for (int tt = 1; tt <= t; ++tt) {

 long long n;
 scanf("%lld", &n);

 int ans = 0;
 
 int n2 = min((long long)sqrt(n+0.0) + 5, n);


 memset(was, true, sizeof(was));

 for(int i = 2; i * i <= n2; ++i) {
  int j = i * i;
  while(j <= n2) {
   was[j] = false;
   j += i;
  }
 }

 for(int i = 2; i <= n2; ++i)
  if(was[i]) {
   int col = 0;
   long long x = i;
   while(x <= n) {
    x *= (long long)i;
    ++ col;
   }
   ans += col - 1;
  }

  if(n == 1) ans = -1;

  printf("Case #%d: %d\n", tt, ans + 1);
}
 return 0;

}

