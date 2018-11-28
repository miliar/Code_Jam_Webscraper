#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;
#define PI 3.14159265358979323846264338327950288

int N;
int a[45][45];
int que[45];
int cvr[45];

void init()
{
    scanf("%d", &N);
    for (int i = 1; i <= N; ++ i)
      for (int j = 1; j <= N; ++ j)
        {
           char c;
           while (1)
           {
              c = getchar();
              if (c == '0' || c == '1') break;
           }
           a[i][j] = c - '0';
        }
}

void work()
{
    memset(cvr, 0, sizeof(cvr));
    for (int i = 1; i <= N; ++ i)
    {
       int pos = 1;
       for (int j = 1; j <= N; ++ j)
         if (a[i][j] == 1) pos = j;
       for (int k = pos; k <= N; ++ k)
         if (!cvr[k])
           {
               cvr[k] = 1;
               que[i] = k;
               break;
           }
    }
    //for (int i = 1; i <= N; ++ i) printf("%d ", que[i]);
    //printf("\n");
    int res = 0;
    for (int i = 1; i < N; ++ i)
      for (int j = i + 1; j <= N; ++ j)
        if (que[i] > que[j]) ++ res;
    printf("%d\n", res);
}

int main()
{
    int caseNo;
    scanf("%d", &caseNo);
    for (int T = 1; T <= caseNo; ++ T)
    {
        printf("Case #%d: ", T);
        init();
        work();
    }
    return 0;
}

