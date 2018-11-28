#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define DEBUG(format, args...) do { fprintf(stderr, format, ## args); fflush(stderr); } while (0)
#define PRINT(format, args...) do { fprintf(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

const int MOD=10000;

const int WELLEN=19;
const char WELCOME[]="welcome to code jam!";

int dp[512][WELLEN+1];

int main() {
  char bf[512];
  int i, j, L, t, T;
  scanf("%d\n", &T);
  for (t=1; t<=T; t++) {
    bf[L=strlen(gets(bf))]='!';
    memset(dp, 0, sizeof dp);
    dp[0][1]=(bf[0]=='w');
    for (i=1; i<=L; i++)
      for (j=1; j<=WELLEN; j++) {
        dp[i][j]=dp[i-1][j];
        if (j==1)
          dp[i][j]+=(bf[i]=='w');
        else
          dp[i][j]+=(bf[i]==WELCOME[j-1])*dp[i-1][j-1];
        dp[i][j]%=MOD;
      }
    PRINT("Case #%d: %04d\n", t, dp[L][WELLEN]);
  }
  return 0;
}
