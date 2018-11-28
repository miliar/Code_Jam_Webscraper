#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>

using namespace std;

#define MaxN 200
int mx[4] = {-1,0,0,1};
int my[4] = {0,-1,1,0};
int f[MaxN][MaxN],a[MaxN][MaxN];
int n,m,tot;

void init()
{
    tot = 0;
    memset(f,0,sizeof(f));
    scanf("%d%d", &n , &m);
    for (int i = 1; i <= n ; i++)
      for (int j = 1; j <= m ; j++)
         scanf("%d", &a[i][j]);
}

void dfs(int i,int j)
{
    int l = -1 , u = a[i][j];
    for (int k = 0; k < 4 ; k++)
    {
        int t1 = i + mx[k];
        int t2 = j + my[k];
        if (t1 < 1 || t2 < 1 || t1 > n || t2 > m) continue;
        if (a[t1][t2] >= u) continue;
        l = k;
        u = a[t1][t2];
    }
    if (l != -1)
    {
        int t1 = i + mx[l];
        int t2 = j + my[l];
        if (!f[t1][t2]) dfs(t1,t2);
        f[i][j] = f[t1][t2];
    } else f[i][j] = ++tot;
}

int main()
{
//    freopen("test.in","r",stdin);
//    freopen("test.out","w",stdout);
    int Case;
    scanf("%d", &Case); 
    for (int i = 1; i <= Case ; i++)
    {
        printf("Case #%d:\n",i);
        init();
        for (int i = 1; i <= n ; i++)
          for (int j = 1; j <= m ; j++)
             if (!f[i][j]) dfs(i,j);
        for (int i = 1; i <= n ; i++)
        {
            for (int j = 1; j < m ; j++) printf("%c ",'a' + f[i][j] - 1);
            printf("%c\n", 'a' + f[i][m] - 1);
        }
    }
    return 0;
}

