//Ulf LundstrÅˆm

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
const enum {SIMPLE, FOR, WHILE} mode = FOR;

#define ever (;;)
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

bool solve(int P) {
  int T,NA,NB;
  scanf("%d%d%d",&T,&NA,&NB);
  vi aReady,aDep,bReady,bDep;
  for (int i = 0; i < NA; ++i) {
    int h,m;
    scanf("%d:%d",&h,&m);
    aDep.push_back(60*h+m);
    scanf("%d:%d",&h,&m);
    bReady.push_back(60*h+m+T);
  }
  for (int i = 0; i < NB; ++i) {
    int h,m;
    scanf("%d:%d",&h,&m);
    bDep.push_back(60*h+m);
    scanf("%d:%d",&h,&m);
    aReady.push_back(60*h+m+T);
  }
  printf("Case #%d:",P+1);
  sort(aReady.begin(),aReady.end());
  aReady.push_back(1000000);
  sort(aDep.begin(),aDep.end());
  sort(bReady.begin(),bReady.end());
  bReady.push_back(1000000);
  sort(bDep.begin(),bDep.end());
  
  int n=0,m=0,id=0,ir=0;
  while (id < (int)aDep.size()) {
    if (aDep[id] < aReady[ir]) {
      ++n;
      m = max(n,m);
      ++id;
    } else {
      --n;
      ++ir;
    }
  }
  printf(" %d",m);
  n=0,m=0,id=0,ir=0;
  while (id < (int)bDep.size()) {
    if (bDep[id] < bReady[ir]) {
      ++n;
      m = max(n,m);
      ++id;
    } else {
      --n;
      ++ir;
    }
  }
  printf(" %d\n",m);
  return true;
}

int main() {
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%i", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
