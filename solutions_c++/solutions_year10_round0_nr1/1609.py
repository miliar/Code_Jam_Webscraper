/**********************************************************************
Author: Jun
Created Time:  2010/5/8 11:05:00
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
const int maxn = 100;

int tot[maxn], power[maxn];
int n, k, case_num;

void work()
{
    scanf("%d %d", &n, &k);
    if (k != 0 && (k + 1) % (tot[n - 1] + 1) == 0)
        printf("ON\n");
    else printf("OFF\n");
}

int main()
{
//    freopen("a.out", "w", stdout);
    power[0] = 1;
    for (int i = 1; i <= 30; i ++)
        power[i] = power[i - 1] * 2;
    tot[0] = 1;
    for (int i = 1; i < 30; i ++)
        tot[i] = tot[i - 1] + power[i];
    scanf("%d", &case_num);
    for (int i = 0; i < case_num; i ++)
    {
        printf("Case #%d: ", i + 1);
        work();
    }
    
    return 0;
}

