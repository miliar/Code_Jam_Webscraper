/**********************************************************************
Author: Jun
Created Time:  2010/5/23 18:17:03
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

long long l, p;
int c, ans, tot, case_num;

void work()
{
    scanf("%I64d %I64d %d", &l, &p, &c);
    tot = 1;
    while (l < p)
    {
        l = l * c;
        tot ++;
    }
    ans = 0;
    while (1)
    {
        if (tot <= 2) break;
        ans ++;
        tot = (tot / 2) + 1;
    }
    printf("%d\n", ans);
}

int main()
{
    freopen("b.out", "w", stdout);
    scanf("%d", &case_num);
    for (int i = 0; i < case_num; i ++)
    {
        printf("Case #%d: ", i + 1);
        work();
    }
    return 0;
}

