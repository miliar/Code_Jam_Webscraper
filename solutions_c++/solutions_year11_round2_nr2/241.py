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

int np, d;
int p[1000], col[1000], pos[1000], man[1000];
const long double eps = 1e-7;

bool can(long double time) {
 for(int i = 0; i < np; ++i)
  pos[i] = p[i], man[i] = col[i];

 long double last = 2000000000;
 last = last * last;
 last = -last;
 for(int i = 0; i < np; ++i)
  for(int j = 0; j < man[i]; ++j) {
   long double pp = last + d;
   if(pos[i] >= pp) {
    if(pos[i] - time <= pp + eps) last = pp; else
     last = pos[i] - time;
   } else {
    if(pos[i] + time >= pp) last = pp; else 
     return false;
   }
  }
 return true;
}

int main() {
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);

 int kt;
 cin >> kt;
 for(int zz = 1; zz <= kt; ++zz) {
  
  cin >> np >> d;
  for(int i = 0; i < np; ++i)
   cin >> p[i] >> col[i];

  long double left = 0, right = 2000000000;
  right = right * right;
  for(int i = 0; i < 100; ++i) 
   if(can((left + right) / 2.0))
    right = (left + right) / 2.0; else
    left = (left + right) / 2.0;

  cout << "Case #" << zz << ": ";
  cout << fixed << setprecision(7) << ((left + right) / 2.0) << endl;
 
 }

 return 0;
}

