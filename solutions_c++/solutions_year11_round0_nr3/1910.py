#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <cmath>
using namespace std;

const int N = 1005;
const int inf = 0x3fffffff;
int a[N];



int main()
{
    
    int t, i, j, k;
    freopen("C-large.in", "r", stdin);
    //freopen("ans1.txt", "w", stdout);
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++)
    {
        int n;
        scanf("%d", &n);
        int cnt = 0;
        int ans = 0;
        int Min = inf;
        for(i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
            cnt ^= a[i];     
            ans += a[i];
            Min = min(Min, a[i]);
        }
        printf("Case #%d: ", cas);
        if(cnt)
        {
            puts("NO");    
        }
        else
        {
            printf("%d\n", ans - Min);    
        }
    
    }
    
   // while(1);
    return 0;    
}
