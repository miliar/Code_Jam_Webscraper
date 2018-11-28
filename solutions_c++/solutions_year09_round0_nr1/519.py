/**********************************************************************
Author: Sherlock
Created Time:  2009-9-3 13:57:17
File Name: 
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int   maxint  =   0x7FFFFFFF;
const int   maxSize =   15 * 5000 + 100;

int             n, m, l, total, ans, len;
int             edge[maxSize][30], tree[maxSize];
bool            hash[5000 + 10];
char            s[15 * 30];

void            add_node()
{
    tree[total] = -1;
    for (int i = 0; i < 26; i ++)
        edge[total][i] = -1;
    total ++;
    return ;
}

void            insert_trie(int now, int k, int t)
{
    if (k == l)
    {
        tree[now] = t;
        return ;
    }
    if (edge[now][s[k] - 'a'] == -1)
    {
        edge[now][s[k] - 'a'] = total;
        add_node();
    }
    insert_trie(edge[now][s[k] - 'a'], k + 1, t);
}

void            init()
{
    total = 0;
    add_node();
    for (int i = 0; i < n; i ++)
    {
        scanf("%s", s);
        insert_trie(0, 0, i);
    }
}

void            make(int now, int k)
{
    if (k >= len)
    {
        if (tree[now] != -1)
        {
            if (! hash[tree[now]])
                ans ++;
            hash[tree[now]] = true;
        }
        return ;
    }
    int op = k, ed = k + 1, next = k + 1;
    if (s[k] == '(')
    {
        op ++;
        for (int i = k + 1; i < len; i ++)
            if (s[i] == ')')
            {
                ed = i;
                next = i + 1;
                break;
            }
    }
    for (int i = op; i < ed; i ++)
        if (edge[now][s[i] - 'a'] != -1)
            make(edge[now][s[i] - 'a'], next);
}

void            solve()
{
    for (int i = 0; i < m; i ++)
    {
        scanf("%s", s);
        len = strlen(s);
        ans = 0;
        memset(hash, false, sizeof(hash));
        make(0, 0);
        printf("Case #%d: %d\n", i + 1, ans);
    }
}

int             main()
{
    freopen("A.out", "w", stdout);
    while (scanf("%d%d%d", &l, &n, &m) != -1)
    {
        init();
        solve();
    }
    return 0;
}

