#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

const char * WELCOME = "welcome to code jam";
int N;
char buf[1024];
int dp[512][32];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &N);
    getchar();
    int i, j, k;
    for(int tt = 1; tt <= N; tt++)
    {
            gets(buf);
            int len = strlen(buf);
            memset(dp, 0, sizeof(dp));
            
            for(i = 0; i < len; i++)
            {
                  for(j = 0; j < 19; j++)
                  {
                        if(buf[i] == WELCOME[j])
                        {
                                  if(j == 0)
                                      dp[i][j] = 1;
                                      else
                                                             {
                                      for(k = 0; k < i; k++)
                                      {
                                            dp[i][j] = (dp[i][j] + dp[k][j - 1]) % 10000;
                                      }
                                  }
                        }
                  }
            }
            
            /*for(i = 0; i < len; i++)
            {
                  printf("(%d,%d)\n", i, 0);
                  for(j = 0; j < 19; j++)
                  printf("%d ", dp[i][j]);
                  puts("");
                  }*/
            int ret = 0;
            for(i = 18; i < len; i++)
                  ret = (ret + dp[i][18]) % 10000;
            printf("Case #%d: %04d\n", tt, ret);
            
    }
              
    return 0;
}
