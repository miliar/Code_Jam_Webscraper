/**********************************************************************
Author: Jun
Created Time:  2009/9/12 9:25:53
File Name: 
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxn = 100000;

bool vis[maxn + 100], ok[maxn + 100], v[maxn + 100], okk[20][maxn];
int a[100];
char s[100];

void prepare(int num)
{
    bool pd;
    memset(vis, 0, sizeof(vis));
    memset(ok, 0, sizeof(ok));
    for (int i = 2; i <= maxn; i ++)
    {
        if (ok[i]) okk[num][i] = true;
        if (ok[i] || vis[i]) continue;
        int t = i;
        vis[t] = true;
        while (1)
        {
            int tmp = t;
            t = 0;
            while (tmp != 0)
            {
                t += (tmp % num) * (tmp % num);
                tmp /= num;
            }
            if (t == 1 || ok[t])
            {
                pd = true;
                break;
            }
            if (vis[t])
            {
                pd = false;
                break;
            }
            vis[t] = true;
        }
        if (pd) 
        {
            ok[i] = true;
            vis[i] = false;
            t = i;
            while (1)
            {
                int tmp = t;
                t = 0;
                while (tmp != 0)
                {
                    t += (tmp % num) * (tmp % num);
                    tmp /= num;
                }
                if (pd)
                {
                    if (ok[t] || t == 1) break;
                    vis[t] = false;
                    ok[t] = true;
                }
            }
            okk[num][i] = true;
        }
    }
}

void work()
{
    gets(s);
    int n = 0, len = strlen(s), i = 0;
    while (i < len)
    {
        if (s[i] >= '0' && s[i] <= '9')
        {
            a[n] = 0;
            while (s[i] >= '0' && s[i] <= '9' && i < len)
            {
                a[n] = a[n] * 10 + s[i] - '0';
                i ++;
            }
            n ++;
        }
        else i ++;
    }
    for (int i = 2; i <= maxn; i ++)
    {
        bool pd = true;
        for (int j = 0; j < n; j ++)
            if (!okk[a[j]][i]) 
            {
                pd = false;
                break;
            }
        if (pd)
        {
            printf("%d\n", i);
            break;
        }
    }
}
int main()
{
    freopen("a.out", "w", stdout);
    memset(okk, 0, sizeof(okk));
    for (int i = 2; i <= 10; i ++)
       prepare(i);
    int case_num;
    scanf("%d", &case_num);
    gets(s);
    for (int i = 0; i < case_num; i ++)
    {
        printf("Case #%d: ", i + 1);
        work();
    }
    return 0;
}

