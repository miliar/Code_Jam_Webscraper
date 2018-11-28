#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define maxn 1000010
#define LL long long

LL pr[maxn];
int prtop;
bool ispr[maxn];

LL T, n;
LL ans;

void make_primes() {
     
  for(int i = 2; i < maxn; i++)
    ispr[i] = true;
  for(int i = 2; i*i < maxn; i++)
    if (ispr[i]) {
      LL j = i + i;
      while (j < maxn) {
        ispr[j] = false;
        j += i;      
      }             
    }     
  prtop = 0;
  for(int i = 2; i < maxn; i++)
    if (ispr[i]) 
      pr[prtop++] = i;
     
}

inline LL countit(LL x) {
  LL ret = 0;
  LL tn = n;
  while (tn >= x) {
    ret ++;
    tn /= x;      
  }       
  return ret;
}

int main() {
    
  freopen("C-large.in", "rt", stdin);
  freopen("C-large.out", "wt", stdout);
  
  make_primes();
  
  scanf("%lld", &T);
  for(int ctn = 1; ctn <= T; ctn ++) {
          
    cerr << "Test case " << ctn << endl;
          
    scanf("%lld", &n);
    ans = 0;
    for(int i = 0; i < prtop; i++) {
      LL x = pr[i];
      if (x * x > n) break;
      ans += countit(x) - 1;        
    }
    printf("Case #%d: ", ctn);
    if (n == 1) puts("0");
    else printf("%lld\n", ans + 1);
          
  }    
  
  return 0;
    
}
