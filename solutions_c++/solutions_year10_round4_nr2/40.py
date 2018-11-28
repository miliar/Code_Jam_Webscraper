#define _CRT_SECURE_NO_DEPRECATE
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

const int MAXP = 12;

int p, pp;
int ms[1<<MAXP];
long long dp[MAXP][1<<MAXP][MAXP];

void relax(long long &x, long long val){
  if (x > val) x = val;
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn;
  scanf("%d", &tn);
  for (int t=1; t<=tn; t++){
    printf("Case #%d: ", t);
    scanf("%d", &p);
    pp = 1<<p;
    memset(dp, 0x3f, sizeof(dp));
    for (int i=0; i<pp; i++){
      scanf("%d", &ms[i]);
      dp[0][i][ms[i]] = 0;
    }
    for (int i=1; i<=p; i++){
      for (int j=0; j<(1<<(p-i)); j++){
        int ccost;
        scanf("%d", &ccost);
        for (int l=0; l<=p; l++){
          for (int r=0; r<=p; r++){
            int x = min(l, r);
            long long nval = dp[i-1][2*j][l] + dp[i-1][2*j+1][r];
            relax(dp[i][j][x], nval + ccost);
            if (x > 0){
              relax(dp[i][j][x-1], nval);
            }
          }
        }
      }
    }
    long long bres = (1LL << 60);
    for (int i=0; i<=p; i++){
      relax(bres, dp[p][0][i]);
    }
    printf("%I64d\n", bres);
  }
  return 0;
}
