#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
#define maxA (2000008)
#define maxN (102)
#define maxQ (6000008)

using namespace std;

struct qTpye
{
    int x,y,t;
} q[maxQ];

int ans,upB,ti,tn,n,i,j,x,ot[maxN],bt[maxN],f[maxN][maxN][maxN],hash[maxN][maxN][maxN];
char ch;

void spfa()
{
    int i,j,k,fr,re,x,y,t,u,v,tt,dx,dy;
    for (i = 1; i <= upB; i++)
        for (j = 1; j <= upB; j++)
            for (k = 0; k <= n; k++)
            {
                f[i][j][k] = maxA;
                hash[i][j][k] = 0;
            }

    fr = 0; re = 1;
    f[1][1][0] = 0;
    hash[1][1][0] = 1;
    q[1].x = 1; q[1].y = 1; q[1].t = 0;
    while (fr != re)
    {
        x = q[(fr + 1) % maxQ].x; y = q[(fr + 1) % maxQ].y; t = q[(fr + 1) % maxQ].t;
        for (dx = -1; dx <= 1; dx++)
            for (dy = -1; dy <= 1; dy++)
            {
                u = x + dx; v = y + dy;
                if (u > upB || u < 1 || v > upB || v < 1) continue;

                if (dx != 0 || dy != 0)
                {
                    if (f[u][v][t] > f[x][y][t] + 1)
                    {
                        f[u][v][t] = f[x][y][t] + 1;
                        if (hash[u][v][t] == 0)
                        {
                            hash[u][v][t] = 1;
                            re = (re + 1) % maxQ;
                            q[re].x = u; q[re].y = v; q[re].t = t;
                        }
                    }
                }
                if (t < n)
                {
                    if ((dx == 0 && ot[t+1] == x) || (dy == 0 && bt[t+1] == y))
                    {
                        if (f[u][v][t+1] > f[x][y][t] + 1)
                        {
                            f[u][v][t+1] = f[x][y][t] + 1;
                            if (hash[u][v][t+1] == 0)
                            {
                                hash[u][v][t+1] = 1;
                                re = (re + 1) % maxQ;
                                q[re].x = u; q[re].y = v; q[re].t = t+1;
                            }
                        }
                    }
                }
            }
        hash[x][y][t] = 0;
        fr = (fr + 1) % maxQ;
    }
}

void findAns()
{
    ans = maxA;
    for (i = 1; i <= upB; i++)
        for (j = 1; j <= upB; j++)
            if (f[i][j][n] < ans) ans = f[i][j][n];
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tn);
    for (ti = 1; ti <= tn; ti++)
    {
        memset(ot,0,sizeof(ot));
        memset(bt,0,sizeof(bt));
        scanf("%d",&n);
        upB = 1;
        for (i = 1; i <= n; i++)
        {
            scanf(" %c %d",&ch,&x);
            if (ch == 'O') ot[i] = x;
            else if (ch == 'B') bt[i] = x;
            if (upB < x) upB = x;
        }
        scanf("\n");
        spfa();
        findAns();
        printf("Case #%d: %d\n",ti,ans);
    }
}
