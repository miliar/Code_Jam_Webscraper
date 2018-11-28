#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define MAX_N 10001

int gcd(int a, int b) {
  return b != 0 ? gcd(b, a % b) : a;
}

int n, l, h, v[MAX_N];

bool func(int a, int b) {
  if(a > b) swap(a, b);
  return (b % a) == 0;
}

int main() {
  int t, count = 0;
  scanf("%d", &t);
  
  while(t--) {
    scanf("%d%d%d", &n, &l, &h);
    rep(i, n) scanf("%d", &v[i]);
    
    printf("Case #%d: ", ++count);
    
    bool f = false;
    for(int i=l; i<=h; i++) {
      bool ok = true;
      rep(j, n) {
        if(!func(v[j], i)) ok = false;
      }
      if(ok) { printf("%d\n", i); f = true; break;}
    }
    if(!f) printf("NO\n");
    
  }
  
  return 0;
}
