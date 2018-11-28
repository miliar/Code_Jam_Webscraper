#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>

using namespace std;
const int MAXN = 20000;
int N;
int pos[MAXN];
int len[MAXN];

int dp[MAXN];
int main()
{
   freopen("A-large.in","r",stdin);
   freopen("A-large_test.out","w",stdout);
   int T;
   scanf("%d",&T);
   for(int tc = 1; tc <= T; tc++) {
      scanf("%d",&N);
      for(int i = 0; i < N; i++) {
         scanf("%d %d",&pos[i],&len[i]);
      }
      int D;
      scanf("%d",&D);
      memset(dp,0,sizeof(dp));

      dp[0] = pos[0];

      for(int i = 1; i < N; i++) {
         for(int j = 0; j < i; j++) {
            if(pos[j]+dp[j]>=pos[i]) {
                  int coverd = pos[j]+dp[j]-pos[i];
                  if(len[i]<coverd) continue;
                  dp[i]=max(dp[i],min(len[i],pos[i]-pos[j]));

            }

         }
      }
      int ok = 0;
      for(int i = 0; i < N; i++) {
         if(pos[i]+dp[i]>=D) {
            ok=1;
         }
      }
      printf("Case #%d: ",tc);
      if(ok) {
         printf("YES");
      }
      else {
         printf("NO");
      }
      printf("\n");

   }
   return 0;
}
