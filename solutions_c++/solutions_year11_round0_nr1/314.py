#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cassert>
using namespace std;

#define psb push_back

int T, n;
string robot;
vector<int> no;

int doit() {

  int cnt = 0;
  int i0 = 1, j0 = 1;
  int p = 0;
  int next0 = 1, next1 = 1;
  for(int i = 0; i < n; i++)
    if (robot[i] == 'O') {next0 = no[i]; break; }
  for(int i = 0; i < n; i++)
    if (robot[i] == 'B') {next1 = no[i]; break; }
  while (p < n) {
    cnt ++;
    bool pushed = false;
    if (robot[p] == 'O' && i0 == no[p]) {
      p ++;
      pushed = true;
      for(int j = p; j < n; j++)
        if (robot[j] == 'O') {next0 = no[j]; break; }
    }
    else {
      if (next0 > i0) i0 ++;
      else if (next0 < i0) i0 --;
    }
    
    if (!pushed && robot[p] == 'B' && j0 == no[p]) {
      p ++;
      pushed = true;
      for(int j = p; j < n; j++)
        if (robot[j] == 'B') {next1 = no[j]; break; }
    }
    else {
      if (next1 > j0) j0 ++;
      else if (next1 < j0) j0 --;
    }
  }
  return cnt;

}

int main() {

  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
  
  scanf("%d\n", &T);
  for(int cT = 0; cT < T; cT++) {
  
    scanf("%d", &n);
    robot = "";
    no.clear();
    for(int i = 0; i < n; i++) {
      char t = getchar();
      while (t == ' ') t = getchar();
      robot += t;
      int tt;
      scanf("%d", &tt);
      no.psb(tt);
    }
    scanf("\n");
    
    int ret = doit();
    printf("Case #%d: %d\n", cT+1, ret);
  
  }
  
  return 0;

}
