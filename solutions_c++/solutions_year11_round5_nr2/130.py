#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;

#define maxn 10010
#define psb push_back

int n, T, limit;
int cnt[maxn], tcnt[maxn];
int tail[maxn];
vector<int> a;

bool doit() {
     
  memset(tail,0,sizeof(tail));
  memcpy(cnt, tcnt, sizeof(cnt));
  for(int i = 1; i <= 10000; i++)
    while (cnt[i] > 0) {
      if (tail[i-1] > 0) {
        tail[i-1] --;
        tail[i] ++;
        cnt[i] --;              
      }           
      else {
        for(int j = i; j < i + limit; j ++)
          if (cnt[j] == 0) return false;
          else {
            cnt[j] --;     
          }     
        tail[i+limit-1] ++;  
      }
    }
  return true;
     
}

int main() {
    
  freopen("B-large.in", "rt", stdin);
  freopen("B-large.out", "wt", stdout);
  
  scanf("%d\n", &T);
  for(int ctn = 1; ctn <= T; ctn ++) {
          
    cerr << "ctn = " << ctn << endl;
          
    a.clear();
    memset(cnt,0,sizeof(cnt));
    int t;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
      scanf("%d", &t);
      a.psb(t);
      cnt[t] ++;        
    }
    
    if (n == 0) {
      printf("Case #%d: %d\n", ctn, 0);
      continue;      
    }
    
    memcpy(tcnt, cnt, sizeof(cnt));
    
    sort(a.begin(), a.end());
    
    int lft = 0, rft = 1000 + 1;
    while (lft < rft-1) {
      limit = (lft + rft) >> 1;
      bool success = doit();
      if (success) lft = limit; else rft = limit;      
    }
    
    printf("Case #%d: %d\n", ctn, lft);
          
  }
  
  return 0;
    
}
