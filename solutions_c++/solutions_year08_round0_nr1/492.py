#include <stdio.h>
#include <string.h>

#define NAME_LEN 200
#define min(a,b) ((a) < (b) ? (a) : (b))

int main()
{
  int cs=1, n, i, j, s, q, sol, solp;
  char *eng[100];
  size_t len[100];
  char *query;
  size_t q_len;
  int dp[100][1001];

  memset(eng, 0, sizeof(eng));
  memset(len, 0, sizeof(len));
  q_len = 0;
  query = NULL;

  scanf("%d\n", &n);
  for (;cs <= n; cs++)
  {
    scanf("%d\n", &s);
    for (i=0;i<s;i++)
      getline(eng+i,len+i,stdin);
    scanf("%d\n", &q);
    memset(dp, 0, sizeof(dp));
    sol = 0;
    for (i=0;i<q;i++)
    {
      getline(&query, &q_len, stdin);
      for (j=0;j<s;j++)
      {
        bool match = strcmp(query, eng[j]) == 0;
        if (i > 0 && !match)
          dp[j][i] = min(dp[j][i-1], sol+1);
        if (match)
        {
          int t = -1;
          for (int k=0; k<s; k++)
          {
            if (k == j) continue;
            if (t == -1) t = dp[k][i-1];
            t = min(t, dp[k][i-1]);
          }
          dp[j][i] = t + 1;
        }

        if (j==0)
          solp = dp[j][i];
        else
          solp = min(solp, dp[j][i]);
      }
      sol = solp;
    }
    printf("Case #%d: %d\n", cs, sol);
  }

  return 0;
}
