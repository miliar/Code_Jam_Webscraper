/**********************************************************************
Author: Sherlock
Created Time:  2009-9-13 0:18:58
File Name: A.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

const int   maxint  =   0x7FFFFFFF;
const int   maxSize =   100 + 10;

int         total, num;
int         son[maxSize][2], g[maxSize];
char        buf[1000];
double      ans, p[maxSize];

string      s;

vector  <int>       list;
map <string, int>   hash;

void            build(int l, int r)
{
    //printf("%d %d\n", l, r);
    int now = total;
    son[now][0] = son[now][1] = -1;
    total ++;
    int i = l;
    while (i < r && (s[i] < '0' || s[i] > '9'))
        i ++;
    p[now] = s[i] - '0';
    double t = 0.1;
    i ++;
    if (s[i] == '.')
    {
        i ++;
        for (; i < r && s[i] >= '0' && s[i] <= '9'; i ++)
        {
            p[now] += t * (s[i] - '0');
            t *= 0.1;
        }
    }
    while (i < r && s[i] == ' ')
        i ++;
    if (i == r || s[i] == ')')
        return ;
    string f = "";
    for (; i < r && ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')); i ++)
        f += s[i];
    if (hash.count(f) == 0)
        hash[f] = num ++;
    g[now] = hash[f];
    
    while (i < r && s[i] == ' ')
        i ++;
    int a = i;
    int cnt = 0;
    for (; i < r; i ++)
    {
        if (s[i] == '(')
            cnt ++;
        else
            if (s[i] == ')')
                cnt --;
        if (cnt == 0)
            break;
    }
    i ++;
    son[now][0] = total;
    build(a, i);

    while (s[i] == ' ')
        i ++;
    
    a = i;
    cnt = 0;
    for (; i < r; i ++)
    {
        if (s[i] == '(')
            cnt ++;
        else
            if (s[i] == ')')
                cnt --;
        if (cnt == 0)
            break;
    }
    i ++;
    son[now][1] = total;
    build(a, i);
}

void            init()
{
    hash.clear();
    int l;
    scanf("%d", &l);
    gets(buf);
    s = "";
    for (int i = 0; i < l; i ++)
    {
        gets(buf);
        s += buf;
        s += " ";
    }
    total = 0;
    num = 0;
    build(0, s.size());
    //printf("%s\n", s.c_str());
}

void            make(int now)
{
    ans *= p[now];
    if (son[now][0] == -1)
        return ;
    bool flag = false;
    for (unsigned int i = 0; i < list.size(); i ++)
        if (list[i] == g[now])
        {
            flag = true;
            break;
        }
    if (flag)
        make(son[now][0]);
    else
        make(son[now][1]);
}

void            solve()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i ++)
    {
        scanf("%s", buf);
        int m;
        scanf("%d", &m);
        list.clear();
        for (int j = 0; j < m; j ++)
        {
            scanf("%s", buf);
            if (hash.count(buf) != 0)
                list.push_back(hash[buf]);
        }
        ans = 1;
        make(0);
        printf("%.7lf\n", ans);
    }
}

int             main()
{
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int cnt = 0;
    while (T > 0)
    {
        T --;
        printf("Case #%d:\n", ++ cnt);
        init();
        solve();
    }
    return 0;
}

