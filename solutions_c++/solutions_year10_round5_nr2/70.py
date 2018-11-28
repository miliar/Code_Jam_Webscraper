#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

inline int gcd(int a, int b){
  return (b == 0) ? a : gcd(b, a % b);
}

const int MAX = 100000;

int n;
long long L;
int bs[128];
int dp[MAX];

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn;
  scanf("%d\n", &tn);
  for(int t=1; t<=tn; t++){
    printf("Case #%d: ", t);
    scanf("%I64d%d", &L, &n);
    int g;
    scanf("%d", &bs[0]);
    g = bs[0];
    for (int i=1; i<n; i++){
      scanf("%d", &bs[i]);
      g = gcd(g, bs[i]);
    }
    if (L % g > 0){
      printf("IMPOSSIBLE\n");
    }
    else{
      L /= g;
      for (int i=0; i<n; i++) bs[i] /= g;
      sort(bs, bs + n);
      memset(dp, 0x3f, sizeof(dp));
      dp[0] = 0;
      for (int i=0; i<MAX; i++){
        if (dp[i] == 0x3f3f3f3f) continue;
        for (int j=0; (j<n) && (i + bs[j] < MAX); j++){
          int ni = i + bs[j];
          if (dp[ni] > dp[i] + 1) dp[ni] = dp[i] + 1;
        }
      }
      long long l = 0, r = L / bs[n-1];
      while (l < r){
        long long q = (l + r) / 2;
        if (L - bs[n-1] * q >= MAX) l = q + 1;
        else r = q;
      }
      long long ans = l;
      L -= bs[n-1] * l;
      printf("%I64d\n", ans + dp[L]);
    }
  }
  return 0;
}
