/**********************************************************************
Author: Jun
Created Time:  2011/5/7 16:23:29
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
const int maxn = 100 + 10;

int casenum, n;
char r[maxn];
int p[maxn];

int moveto(int s, int t, int d)
{
    if (s < t)
        return min(s + d, t);
    else return max(s - d, t);
}

void work(int num)
{
    scanf("%d", &n);
    char ch;
    for (int i = 0; i < n; i ++)
    {
        scanf("%c%c%d", &ch, &r[i], &p[i]);
    }
    r[n] = 'O';
    p[n] = 1000000;
    r[n + 1] = 'B';
    p[n + 1] = 1000000;
    int ia = 0, ib = 0;
    for (int i = 0; i < n + 1; i ++)
        if (r[i] == 'O') {
            ia = i;
            break;
        }
    for (int i = 0; i < n + 2; i ++)
        if (r[i] == 'B'){
            ib = i;
            break;
        }
    int ans = 0, a = 1, b = 1;
    while (true)
    {
        int x = p[ia];
        int y = p[ib];
        int t;
        if (ia < ib)
        {
            t = abs(x - a) + 1;
            ia ++;
        }
        else {
            t = abs(y - b) + 1;
            ib ++;
        }
//        printf("%d %d\n", ia, ib);
        a = moveto(a, x, t);
        b = moveto(b, y, t);
        ans += t;
        while (ia < n && r[ia] != 'O') 
            ia ++;
        while (ib < n && r[ib] != 'B')
            ib ++;
        if (ia >= n && ib >= n)
            break;
//        if (ans > 20) break;
//        printf("%d\n", ans);
    }
    printf("Case #%d: %d\n", num + 1, ans);
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &casenum);
    for (int i = 0; i < casenum; i ++)
        work(i);
    
    return 0;
}

