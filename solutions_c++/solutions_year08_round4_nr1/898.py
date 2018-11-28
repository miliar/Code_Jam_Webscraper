#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;

#define FOR(i,n) for (int i=0;i<n;i++)
#define FORI(i,s) FOR(i,s.size())
#define BEND(x) (x).begin(),(x).end()
#define ll long long

int chan[22222];
int val[22222];
int m;

int evaldp[22222];
int eval(int k) {
 if (k <= (m-1)/2) {
  int ans;
  if (evaldp[k] != -1) return evaldp[k];
  if (val[k]) ans =  eval(k+k) && eval(k+k+1);
  else ans = eval(k+k) || eval(k+k+1);
  return evaldp[k] = ans;
 }
 return val[k];
}

int dp[22222][2];
int doit(int k, int v) {
 //printf("%i: %i\n", k, eval(k));
 if (eval(k) == v) return 0;
 if (dp[k][v] != -1) return dp[k][v];
 if (k > (m-1)/2) {
  if (val[k] == v) return 0;
  return 55555;
 }
 int ans = 55555;
 if (v == val[k]) ans <?= doit(k+k, v) + doit(k+k+1, v);
 else ans <?= doit(k+k, v) <? doit(k+k+1, v);
 if (chan[k]) ans <?= (doit(k+k, v) <? doit(k+k+1, v)) + 1;
 return dp[k][v] = ans;
}

void doit() {
 int v;
 scanf("%i%i", &m, &v);
 FOR(i,(m-1)/2) scanf("%i%i", val+i+1, chan+i+1);
 FOR(i,(m+1)/2) scanf("%i", val+i+(m+1)/2);
 memset(dp,-1,sizeof(dp));
 memset(evaldp,-1,sizeof(evaldp));
 int k = doit(1,v);
 if (k > 11111) printf("IMPOSSIBLE\n");
 else printf("%i\n", k);
}

int main() {
 int c;
 scanf("%i", &c);
 FOR(i,c) {
  printf("Case #%i: ", i+1);
  doit();
 }
}
