/**********************************************************************
Author: Jun
Created Time:  2010/5/23 17:08:05
File Name: C:\Users\June\Desktop\gcj\5.23\a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxn = 1000 + 100;

int a[maxn], b[maxn];
int n, ans, case_num;

void work()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++)
        scanf("%d%d", &a[i], &b[i]);
    ans = 0;
    for (int i = 0; i < n; i ++)
        for (int j = i + 1; j < n; j ++)
            if ((a[i] > a[j] && b[i] < b[j]) || (a[i] < a[j] && b[i] > b[j]))
                ans ++;
    printf("%d\n", ans);
}

int main()
{
    freopen("a.out", "w", stdout);
    
    scanf("%d", &case_num);
    for (int i = 0; i < case_num; i ++)
    {
        printf("Case #%d: ", i + 1);
        work();
    }
    return 0;
}

