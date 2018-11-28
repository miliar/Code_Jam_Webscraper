#include <stdio.h>
#include <math.h>
#include <string.h>

int c[9][2] = {{0,0}, {0,1}, {0,2},
                {1,0}, {1,1}, {1,2},
                {2,0}, {2,1}, {2,2}};

int main()
{
  int N, n, i, j, cs=1, k, x, y;
  long long A, B, C, D, M;
  long long p[100000][2];
  long long ans, t;
  long long pair[3][3];

  scanf("%d", &N);
  
  for (cs=1;cs<=N;cs++)
  {
    scanf("%d %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, p[0], p[0]+1, &M);

    memset(pair, 0, sizeof(pair));

    //i=0;
    //printf("%d %d\n", p[i][0], p[i][1]);
    for (i=1; i<n; i++)
    {
      p[i][0] = (A * p[i-1][0] + B) % M;
      p[i][1] = (C * p[i-1][1] + D) % M;
      
      //printf("%d %d\n", p[i][0], p[i][1]);
    }

    for (i=0;i<n;i++)
      pair[(p[i][0]%3)][(p[i][1]%3)]++;
    
    ans = 0;
    for (i=0; i<9; i++)
      for (j=i+1; j<9; j++)
        for (k=j+1; k<9; k++)
        {
          x = c[i][0] + c[j][0] + c[k][0];
          y = c[i][1] + c[j][1] + c[k][1];

          if (x%3==0 && y%3==0)
          {
            ans += 
            (pair[c[i][0]][c[i][1]] * pair[c[j][0]][c[j][1]] * pair[c[k][0]][c[k][1]]);
            //printf("Step 1: %d,%d,%d -> %lld\n", i,j,k, ans);
          }
        }

    /* Not possible:

    for (i=0; i<9; i++)
      for (j=i+1; j<9; j++)
      {
        x = 2*c[i][0] + c[j][0];
        y = 2*c[i][1] + c[j][1];

        if (x%3==0 && y%3==0)
        {
          t = pair[c[i][0]][c[i][1]];
          ans += ((t * (t-1))/2) * pair[c[j][0]][c[j][1]];
          printf("Step 2: %d,%d -> %lld\n", i,j, ans);
        }
      }
    */

    for (i=0; i<9; i++)
    {
      t = pair[c[i][0]][c[i][1]];
      long long six = 6;
      ans += ((t * (t-1) * (t-2)) / six);
      //printf("Step 3: %d -> %lld (size: %lld)\n", i, ans, pair[c[i][0]][c[i][1]]);
    }
    
    printf("Case #%d: %lld\n", cs, ans);
  }

  return 0;
}
