/**********************************************************************
Author: Jun
Created Time:  2011/5/7 19:05:10
File Name: c.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int maxint = 0x7FFFFFFF;

void work(int num)
{
    int n, x, minx;
    minx = maxint;
    scanf("%d", &n);
    int tmp, tot = 0;
    for (int i = 0; i < n; i ++)
    {
        scanf("%d", &x);
        if (i == 0)
            tmp = x;
        else tmp = tmp ^ x;
        if (x < minx)
            minx = x;
        tot += x;
    }
    
    if (tmp != 0)
        printf("Case #%d: NO\n", num);
    else printf("Case #%d: %d\n", num, tot - minx);
    
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int casenum;
    scanf("%d", &casenum);
    for (int i = 0; i < casenum; i ++)
        work(i + 1);
    
    return 0;
}

