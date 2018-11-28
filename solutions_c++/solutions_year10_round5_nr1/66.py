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

const int MAX = 1<<20;

char is_prime[MAX];
int p10[10]={1};

int d, k;
int seq[12];

long long pow_mod(long long a, long long x, long long p){
  long long res = 1;
  while (x > 0){
    if (x & 1) res = (res * a) % p;
    a = (a * a) % p;
    x >>= 1;
  }
  return res;
}

int calc(long long p){
  for (int i=0; i<k; i++){
    if (seq[i] >= p) return -1;
  }
  long long d32 = (seq[2] + p - seq[1]) % p;
  long long d21 = (seq[1] + p - seq[0]) % p;
  if (d21 != 0){
    long long A = (d32 * pow_mod(d21, p-2, p)) % p;
    long long B = ((seq[1] - A*seq[0]) % p + p) % p;
    for (int i=3; i<k; i++){
      long long nxt = (A * seq[i-1] + B) % p;
      if (nxt != seq[i]) return -1;
    }
    return (int)((A * seq[k-1] + B) % p);
  }
  else if (d32 != 0) return -1;
  else{
    for (int i=3; i<k; i++){
      if (seq[i] != seq[i-1]) return -1;
    }
    return seq[k-1];
  }
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  for (int z=1; z<10; z++){
    p10[z] = p10[z-1] * 10;
  }
  memset(is_prime, 1, sizeof(is_prime));
  for (int i=2; i<MAX; i++){
    if (is_prime[i]){
      for (int j=i+i; j<MAX; j+=i){
        is_prime[j] = 0;
      }
    }
  }
  int tn;
  scanf("%d\n", &tn);
  for(int t=1; t<=tn; t++){
    printf("Case #%d: ", t);
    scanf("%d%d", &d, &k);
    for (int i=0; i<k; i++){
      scanf("%d", &seq[i]);
    }
    if (k == 2 && seq[0] == seq[1]){
      printf("%d\n", seq[0]);
    }
    else if (k < 3) printf("I don't know.\n");
    else{
      int ans = -1, cur;
      for (int p=2; p<=p10[d]; p++){
        if (is_prime[p]){
          cur = calc(p);
          if (cur < 0) continue;
          if (ans == -1 || cur == ans) ans = cur;
          else{
            ans = -1;
            break;
          }
        }
      }
      if (ans < 0) printf("I don't know.\n");
      else printf("%d\n", ans);
    }
    fflush(stdout);
  }
  return 0;
}
