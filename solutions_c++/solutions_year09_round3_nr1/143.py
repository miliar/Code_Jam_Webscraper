/**********************************************************************
Author: Jun
Created Time:  2009/9/13 17:11:29
File Name: a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxn = 100;

int a[maxn], vis[maxn];
char s[maxn];

void work()
{
    scanf("%s", s);
    int n = strlen(s);
    if (n == 1)
    {
        printf("1\n");
        return;
    }
    for (int i = 0; i < n; i ++)
    {
        if (s[i] >= '0' && s[i] <= '9')
            a[i] = s[i] - '0';
        if (s[i] >= 'a' && s[i] <= 'z')
            a[i] = s[i] - 'a' + 11;
    }
    int tot = 0;    
    memset(vis, -1, sizeof(vis));
    for (int i = 0; i < n; i ++)
    {
        if (vis[a[i]] != -1)
            a[i] = vis[a[i]];
        else {
            if (i == 0)
                vis[a[i]] = 1;
            else {
                if (tot == 1)
                    vis[a[i]] = 0;
                else vis[a[i]] = tot;
            }
            a[i] = vis[a[i]];
            tot ++;
        }
    }
    if (tot == 1) tot ++;    
    long long ans = 0;
    for (int i = 0; i < n; i ++)
        ans = ans * tot + a[i];
    printf("%I64d\n", ans);
}

int main()
{
    freopen("a.out", "w", stdout);
    int case_num;
    scanf("%d", &case_num);
    for (int i = 0; i < case_num; i ++)
    {
        printf("Case #%d: ", i + 1);
        work();
    }
    return 0;
}

