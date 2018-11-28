/**********************************************************************
Author: Jun
Created Time:  2009/9/3 14:49:08
File Name: GCJ\a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxn = 15 * 5000 + 1000;

int edge[maxn][26], num[maxn];
char s[20000];
bool ok[20][26];
int n, m, l, ans, tot, len;

void addnode()
{
    for (int i = 0; i < 26; i ++)
        edge[tot][i] = -1;
    num[tot] = 0;
}

void insert(int now, int i)
{
    if (i == len)
    {
        num[now] ++;
        return;
    }
    if (edge[now][s[i] - 'a'] == -1)
    {
        tot ++;
        edge[now][s[i] - 'a'] = tot;
        addnode();
    }
    insert(edge[now][s[i] - 'a'], i + 1);
}

void dfs(int now, int dep)
{
    if (dep == l)
    {
        if (num[now] > 0)
            ans ++;
        return;
    }
    for (int i = 0; i < 26; i ++)
        if (ok[dep][i] && edge[now][i] != -1)
            dfs(edge[now][i], dep + 1);
}

void work()
{
    scanf("%s", s);
    memset(ok, 0, sizeof(ok));
    int j = 0;
    for (int i = 0; i < l; i ++)
    {
        if (s[j] >= 'a' && s[j] <= 'z')
        {
            ok[i][s[j] - 'a'] = true;
            j ++;
            continue;
        }
        j ++;
        while (s[j] != ')')
        {
            ok[i][s[j] - 'a'] = true; 
            j ++;
        }
        j ++;
    }
    ans = 0;
    dfs(0, 0); 
    printf("%d\n", ans);
}

int main()
{
    freopen("a.out", "w", stdout);
    while (scanf("%d%d%d", &l, &m, &n) != EOF)
    {
        tot = 0;
        addnode();
        for (int i = 0; i < m; i ++)
        {
            scanf("%s", s);
            len = strlen(s);
            insert(0, 0);
        }
        int case_num = 0;
        for (int i = 0; i < n; i ++)
        {
            case_num ++;
            printf("Case #%d: ", case_num);
            work();
        }
    }
    return 0;
}

