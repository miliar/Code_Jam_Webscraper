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

const int BIG = 1000000000;

pair<char, int> robots[200];

int main() {
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);

 int kTest;
 cin >> kTest;

 for(int indexTest = 1; indexTest <= kTest; ++indexTest) {
  int n;
  cin >> n;
  
  for(int i = 0; i < n; ++i) 
   cin >> robots[i].first >> robots[i].second;

  int finishPosOrange = BIG, finishPosBlue = BIG, curPosOrange = 1, curPosBlue = 1, time = 0;
  
  for(int i = n - 1; i >= 0; --i)
   if(robots[i].first == 'O')
    finishPosOrange = i; else
    finishPosBlue = i;

  while(finishPosOrange != BIG || finishPosBlue != BIG) {
   ++ time;

   bool changeOrange = false, changeBlue = false;

   if(finishPosOrange < finishPosBlue && curPosOrange == robots[finishPosOrange].second) {
    changeOrange = true;
   } else
   if(finishPosBlue < finishPosOrange && curPosBlue == robots[finishPosBlue].second) {
    changeBlue = true;
   }

   if(finishPosOrange != BIG && curPosOrange < robots[finishPosOrange].second) ++ curPosOrange; else
   if(finishPosOrange != BIG && curPosOrange > robots[finishPosOrange].second) -- curPosOrange;

   if(finishPosBlue != BIG && curPosBlue < robots[finishPosBlue].second) ++ curPosBlue; else
   if(finishPosBlue != BIG && curPosBlue > robots[finishPosBlue].second) -- curPosBlue;

   if(changeOrange) {
    int finishPosTemp = BIG;
    for(int i = n - 1; i > finishPosOrange; --i)
     if(robots[i].first == 'O')
      finishPosTemp = i;
    finishPosOrange = finishPosTemp;
   }

   if(changeBlue) {
    int finishPosTemp = BIG;
    for(int i = n - 1; i > finishPosBlue; --i)
     if(robots[i].first == 'B')
      finishPosTemp = i;
    finishPosBlue = finishPosTemp;
   }

  }

  cout << "Case #" << indexTest << ": " << time << endl; 

 }

 return 0;
}

