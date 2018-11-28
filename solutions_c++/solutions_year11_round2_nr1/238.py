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

long double wp[200], owp[200], oowp[200], wp2[200];

int main() {
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);

 int kt;
 cin >> kt;
 for(int zz = 1; zz <= kt; ++zz) {
  int n;
  cin >> n;
  vector<string> team(n);
  for(int i = 0; i < n; ++i)
   cin >> team[i];
  
  // wp
  for(int i = 0; i < n; ++i) {
   long double win = 0;
   long double all = 0;
   for(int j = 0; j < n; ++j)
    if(team[i][j] == '1') 
     { win += 1, all += 1; } else
    if(team[i][j] == '0')
     { all += 1; }
    if(all == 0) all = 1;
    wp[i] = win / all;
  }
  
  // owp
  for(int i = 0; i < n; ++i) {

   // wp2
   for(int ii = 0; ii < n; ++ii) {
    long double win2 = 0;
    long double all2 = 0;
    for(int jj = 0; jj < n; ++jj)
     if(jj != i) {
     if(team[ii][jj] == '1') 
     { win2 += 1, all2 += 1; } else
     if(team[ii][jj] == '0')
     { all2 += 1; }
     }
     if(all2 == 0) all2 = 1;
     wp2[ii] = win2 / all2;
   }
   
   long double all = 0;
   long double val = 0;
   for(int j = 0; j < n; ++j)
    if(team[i][j] != '.') {
     all += 1;
     val += wp2[j];
    }
   if(all == 0) all = 1;
   owp[i] = val / all;
  }

  // oowp
  for(int i = 0; i < n; ++i) {
   long double all = 0;
   long double val = 0;
   for(int j = 0; j < n; ++j)
    if(team[i][j] != '.') {
     all += 1;
     val += owp[j];
    }
    if(all == 0) all = 1;
    oowp[i] = val / all;
  } 

  cout << "Case #" << zz << ":" << endl;
  for(int i = 0; i < n; ++i) {
   long double rpi = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
   cout << fixed << setprecision(7) << rpi << endl;
  }
 }

 return 0;
}

