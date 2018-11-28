/**********************************************************************
Author: Jun
Created Time:  2011/5/7 19:39:52
File Name: b.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxn = 100 + 10;

char s[maxn], t[maxn];
bool a[30][30], b[30][30];
char c[30][30];

void work(int num)
{
    int m;
    scanf("%d", &m);
    memset(a, 0, sizeof(a));
    memset(b, 0, sizeof(b));
    for (int i = 0; i < m; i ++)
    {
        scanf("%s", s);
        a[s[0] - 'A'][s[1] - 'A'] = true;
        a[s[1] - 'A'][s[0] - 'A'] = true;
        c[s[0] - 'A'][s[1] - 'A'] = s[2];
        c[s[1] - 'A'][s[0] - 'A'] = s[2];
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i ++)
    {
        scanf("%s", s);
        b[s[0] - 'A'][s[1] - 'A'] = true;
        b[s[1] - 'A'][s[0] - 'A'] = true;
    }
    
    scanf("%d", &m);
    scanf("%s", s);
    int l = 0;
    for (int i = 0; i < m; i ++)
    {
        t[l ++] = s[i];
        while (true)
        {
            bool pd = false;
            if (l > 1 && a[t[l - 1] - 'A'][t[l - 2] - 'A'])
            {
                char aa = t[l - 1], bb = t[l - 2];
                l -= 2;
                t[l ++] = c[aa - 'A'][bb - 'A'];
                pd = true;
                continue;
            }
            for (int j = 0; j < l - 1; j ++)
                if (b[t[j] - 'A'][t[l - 1] - 'A'])
                {
                    l = 0;
                    pd = true;
                    break;
                }
            if (!pd) break;
        }
    }
    printf("Case #%d: [", num);
    for (int i = 0; i < l; i ++)
        if (i == l - 1)
            printf("%c", t[i]);
        else printf("%c, ", t[i]);
    printf("]\n");
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int casenum;
    scanf("%d", &casenum);
    for (int i = 0; i < casenum; i ++)
        work(i + 1);
    
    return 0;
}

