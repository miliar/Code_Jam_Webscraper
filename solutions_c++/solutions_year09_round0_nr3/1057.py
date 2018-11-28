#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdio>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

char target[] = "welcome to code jam";
char input[512];
const int LEN = 19;
int dp[20];

int nCases;

int main(){
  cin >> nCases;
  REP(nc, nCases){
    memset(dp, 0, sizeof(dp));
    scanf(" %[a-z ]", input);
    int len = strlen(input);
    REP(i, len){
      char c = input[i];
      REP(j, LEN){
        if(c == target[j]){
          dp[j] += j > 0 ? dp[j-1]: 1;
          if(dp[j] > 9999){
            dp[j] -= 10000;
          }
        }
      }
    }
    printf("Case #%d: %04d\n", nc+1, dp[LEN-1]);
  }
  return 0;
}

