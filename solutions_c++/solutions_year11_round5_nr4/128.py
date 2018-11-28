#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <cassert>
using namespace std;

#define LL long long
#define psb push_back

int T, n;
string a;
string ans;
vector<int> pos;

void checkit(LL now) {
  LL lft = 1, rft = (LL)(2 * sqrt(now));
  while (lft < rft - 1) {
    LL mid = (lft + rft) >> 1;
    if (mid * mid == now) {
      ans = a;
      return;        
    } 
    else if (mid * mid < now) lft = mid;
    else rft = mid;
  }     
  if (lft * lft == now) ans = a;
  if (rft * rft == now) ans = a;
}

void searchit(int p, LL now) {
  if (p == pos.size()) checkit(now);
  else {
    a[a.length() - pos[p] - 1] = '0';
   // printf("pos[p] = %d, a = %s\n", pos[p], a.c_str());
    searchit(p+1, now);
    a[a.length() - pos[p] - 1] = '1';
    searchit(p+1, now + ((LL)1 << pos[p]));
    a[a.length() - pos[p] - 1] = '0';
  }     
}

int main() {
    
  freopen("D-small.in", "rt", stdin);
  freopen("D-small.out", "wt", stdout);
  
  scanf("%d\n", &T);
  for(int ctn = 1; ctn <= T; ctn ++) {
          
    cerr << "ctn = " << ctn << endl;
          
    char t[200]; memset(t,0,sizeof(t));
    gets(t);
    a = t;
    pos.clear(); 
    LL now = 0;
    for(int i = 0; i < a.length(); i++) {
      if (a[i] != '?') {
        if (a[i] == '1')          
          now += (LL)1 << (a.length()-i-1);
      }
      else pos.psb(a.length() - i - 1);
    } 
    
    ans = "";
    searchit(0, now);
    printf("Case #%d: %s\n", ctn, ans.c_str());
          
  }
  
  return 0;
    
}
