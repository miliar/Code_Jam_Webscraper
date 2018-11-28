// Problem A. Password Problem.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#include "stdafx.h"
// END CUT HERE
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;

#define forab(i,a,b) for(int i = (int)(a); i <= (int)(b); i++)
#define forn(i,n) for(int i = 0; i < (int)(n); i++)
// need declare it for vc, vc can not use <typeof> keyword
#define foreach(it,c) for(it = c.begin(); it != c.end(); ++i)

#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

#define N 100005
double p[N];

int main() {
  //freopen("1.in", "r", stdin);
  //freopen("1.out", "w", stdout);

  //freopen("A-small-attempt0.in", "r", stdin);
  //freopen("A-small-attempt0.out", "w", stdout);
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  
  int t;
  cin >> t;
  int a, b;

  for (int cc = 0; cc < t; cc++) {
    cin >> a >> b;
    memset(p, 0, sizeof(p));
    for (int i = 0; i < a; i++) {
      cin >> p[i];
    }
    double res = 0;
    // just press enter
    res = b + 2;
    // backspace a
    double tmp = a + b + 1;
    if (tmp < res) res = tmp;
    // backspace 0 -- a-1
    double pp = 1.0;
    for (int i = 0; i < a; i++) {
      pp *= p[i];
      tmp = pp * (2 * (a - i - 1) + b - a + 1);
      tmp += (1 - pp) * ((2 * (a - i - 1) + b - a + 1) + b + 1);
      if (tmp < res) res = tmp;
    }
    
    //cout << "Case #" << cc << ": " << res << endl;
    printf("Case #%d: %.6f\n", cc+1, res);
  }
  return 0;
}
