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

int N, M;
int yes[105][105];
int a[105][30];
int cvr[105], links[105];

void init()
{
    scanf("%d%d", &N, &M);
    for (int i = 1; i <= N; ++ i)
    {
        for (int j = 1; j <= M; ++ j)
          scanf("%d", &a[i][j]);
    }
    for (int i = 1; i <= N; ++ i)
      for (int j = 1; j <= N; ++ j)
        { 
           yes[i][j] = 1;
           for (int k = 1; k <= M; ++ k)
             if (a[i][k] >= a[j][k]) { yes[i][j] = 0; break; }
        }
};

int dfs(int i)
{
    for (int j = 1; j <= N; ++ j)
      if (!cvr[j] && yes[i][j])
        {
            cvr[j] = 1;
            int q = links[j];
            links[j] = i;
            if (q == 0 || dfs(q)) return 1;
            links[j] = q;
        }
    return 0;
}

int matching()
{
    memset(links, 0, sizeof(links));
    int res = 0;
    for (int i = 1; i <= N; ++ i)
    {
        memset(cvr, 0, sizeof(cvr));
        res += dfs(i);
    }
    return res;
}

void work()
{
    printf("%d\n", N - matching());
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
