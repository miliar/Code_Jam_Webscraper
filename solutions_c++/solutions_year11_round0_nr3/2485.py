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

int main() {
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);

 int kTest;
 cin >> kTest;

 for(int indexTest = 1; indexTest <= kTest; ++indexTest) {
  int n;
  cin >> n;

  int Res = 0;
  int Sum = 0;
  int Min = 1000000000;

  for(int i = 0; i < n; ++i) {
   int x;
   cin >> x;
   Res ^= x;
   Sum += x;
   Min = min(Min, x);
  }

  Sum -= Min;
  
  if(Res == 0)
   cout << "Case #" << indexTest << ": " << Sum << endl; else
   cout << "Case #" << indexTest << ": " << "NO" << endl;

 }


 return 0;
}

