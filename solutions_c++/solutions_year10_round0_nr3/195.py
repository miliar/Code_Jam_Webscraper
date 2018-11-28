#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

const int MAX = 2048;

int r, k, n;
int g[MAX];
int nxt[MAX];
int ptime[MAX];
long long cost[MAX];
long long pcost[MAX];

void build_graph(){
  for (int i=0; i<n; i++){
    long long csum = 0;
    int j;
    for (j=i; j<i+n; j++){
      if (csum + g[j] > k) break;
      csum += g[j];
    }
    cost[i] = csum;
    nxt[i] = j % n;
  }
} 

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    scanf("%d%d%d", &r, &k, &n);
    memset(ptime, 0, sizeof(ptime));
    memset(cost, 0, sizeof(pcost));
    for (int i=0; i<n; i++){
      scanf("%d", &g[i]);
      g[n + i] = g[i];
    }
    build_graph();
    long long ans = 0;
    int v = 0;
    bool used = false;
    for (int i=1; i<=r; i++){
      ans += cost[v];
      ptime[v] = i;
      pcost[v] = ans;
      v = nxt[v];
      if (ptime[v] > 0 && !used){
        int clen = i+1-ptime[v];
        long long ccost = ans+cost[v]-pcost[v];
        int times = (r - i) / clen;
        ans += times * ccost;
        i += times * clen;
        used = true;
      }
    }
    printf("Case #%d: %I64d\n", t, ans);
  }
  return 0;
}
