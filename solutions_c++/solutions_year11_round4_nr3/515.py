/*
 * summary:
 *
 */

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <string.h>
#define INF (1<<30)
#define MAX 0
#define EPS 0
using namespace std;

bool used[1005];
int prime[1005];

int filter(int n)             //返回范围内质数个数，0、1既不是素数也不是合数
{      
    for(int i = 2; i * 2 <= n; i++) used[i*2] = true;
    for (int i = 3; i * i <= n; i++)
        if(!used[i])
            for (int j = i; i * j <= n; j += 2)
                used[i * j] = true;             //是否合数
    int cnt = 0;
    for (int i = 2; i <= n; i++)
        if (!used[i])
            prime[cnt++] = i;
    return cnt;
}

//求n的约数的个数
int Divisor_Sum(int n)
{
   int ret = 1; 
   for (int i = 2;i * i <= n; i++)
   {
       int t = 0;
       while (0 == n % i)
       {
          n /= i;
          t++;   
       }
       ret *= t + 1;
   }
   if(n > 1) ret *= 2;
   return ret; 
}



bool vis[1005];
int num[1005];

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

    int T, N;
    scanf("%d", &T);
    int cnt = filter(1000);
    for(int tcase = 1; tcase <= T; tcase++)
    {
        scanf("%d", &N);
        int worst = 0, best = 0;
        memset(vis, 0, sizeof(vis));
        memset(num, 0, sizeof(num));
        for(int i = 2; i <= N; i++)
        {
            int n = i, add = 0;
            for(int j = 0; prime[j] * prime[j] <= n; j++)
            {
                int t = 0;
                while(n % prime[j] == 0)
                {
                    n /= prime[j];
                    t++;
                }
                if(t > num[ prime[j] ])
                {
                    if(num[ prime[j] ] == 0) best++;
                    num[ prime[j] ] = t;
                    add = 1;
                }
            }
            if(n > 1)
            {
                int t = 1;
                if(t > num[ n ])
                {
                    if(num[ n ] == 0) best++;
                    num[ n ] = t;
                    add = 1;
                }
            }
            worst += add;

//            for(int j = 0; j < cnt && prime[j] * prime[j] <= i; j++)
//                if(i % prime[j] == 0 && !vis[ prime[j] ])
//                {
//                    vis[ prime[j] ] = true;
//                    best++;
//                }
        }
        worst++;
        if(N == 1) best = 1;
//        for(int 
//        printf("%d %d\n", worst, best);
        printf("Case #%d: %d\n", tcase, worst - best);
    }

    return 0;
}
