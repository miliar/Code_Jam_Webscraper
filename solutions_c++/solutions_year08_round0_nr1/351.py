#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
using namespace std;

#define FOR(i,n) for (int i=0;i<n;i++)
#define FORI(i,s) FOR(i,(signed)s.size())

int dp[1024][128];
vector<string> sea, que;
int doit2(int q, int e) {
 if (q==que.size()) return 0;
 if (dp[q][e] != -1) return dp[q][e];
 int ans = 66666;
 if (que[q] == sea[e]) {
  FORI(i,sea) if (que[q] != sea[i]) ans <?= 1+doit2(q+1, i);
 }
 else ans <?= doit2(q+1, e);
 return dp[q][e] = ans;
}

void doit() {
 int ns, nq;
 scanf("%i ", &ns);
 sea.clear(); que.clear();
 while(ns--) {
  char foo[512];
  gets(foo); sea.push_back(foo);
 }
 scanf("%i ", &nq);
 while(nq--) {
  char foo[512];
  gets(foo); que.push_back(foo);
 }
 memset(dp,-1,sizeof(dp));
 int ans = 6666666;
 FORI(i,sea) ans <?= doit2(0,i);
 printf("%i\n", ans);
}

int main() {
 int cases;
 scanf("%i", &cases);
 FOR(i,cases) {
  printf("Case #%i: ", i+1);
  doit();
 }
}
