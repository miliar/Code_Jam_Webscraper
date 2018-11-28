#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cassert>
using namespace std;
#define psb push_back
#define mpr make_pair
#define infinity 1000000010
#define mineps 1e-8
#define sqr(x) ((x)*(x))
#define MIN(x,y) ((x)<(y)?(x):(y))
#define MAX(x,y) ((x)>(y)?(x):(y))
#define LL long long
#define UC unsigned long
#define UI unsigned int
#define pi 3.14159265358979323846 
inline int cmp(double x) {
  if (fabs(x) < mineps) return 0;
  else if (x < 0) return -1;
  else return 1;       
}
//////////////////////////////////////////////
//Start here

#define maxn 1010

LL T, R, n, kk;
LL a[maxn];
LL nxt[maxn], sum[maxn];
LL ans;
LL totsum;

int main() {
    
  freopen("C-large.in", "rt", stdin);
  freopen("C-large.out", "wt", stdout);
  
  scanf("%lld", &T); 
  for(int tn = 1; tn <= T; tn++) {
          
    scanf("%lld %lld %lld", &R, &kk, &n);
    totsum = 0;
    for(int i = 0; i < n; i++) {
      scanf("%lld", &a[i]);
      totsum += a[i];        
    }
    
    if (totsum <= kk) ans = totsum * R;
    else {
      for(int i = 0; i < n; i++) {
        LL nowsum = 0;
        int j = i;
        while (nowsum + a[j] <= kk) {
          nowsum += a[j++];
          if (j == n) j = 0;      
        }
        nxt[i] = j; sum[i] = nowsum;        
      }
      
      ans = 0;
      int i = 0;
      for(LL k = 0; k < R; k++) {
        ans += sum[i]; i = nxt[i];       
      }     
    }
    
    printf("Case #%d: %lld\n", tn, ans);

  }    
    
}
