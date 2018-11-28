#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int R, K, N, g[1000+5], vist[1000+5], next[1000+5];
long long total, sum, val[1000+5];
long long cc[2000+5];
int T, ca;
//long long t1, t2;
//void test()
//{
//    long long temp = 0;
//    for(int i = 0, now = 0; i < R; i++)
//    {
//        temp += val[now];
//        now = next[now];
//    }
//    t1 = temp;
//    cout << temp << endl;
//}
int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d %d %d", &R, &K, &N);
        //if(ca + 1 == 32)   cout << R << " "  << K << " " << N << endl;
        sum = total = 0;
        memset(val, 0, sizeof(val));
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &g[i]);
         //   if(ca + 1 == 32)  cout << g[i] << " ";
            sum += g[i];
        }
        //cout << endl;
        if (sum <= K)
        {
            for (int i = 0; i < N; i++)
            {
                next[i] = i;
                val[i] = sum;
            }
        }
        else
        {
            long long temp = 0;
            for (int i = 0; i < N; i++)
            {
                next[i] =  i;
                temp = 0;
                while (1)
                {
                    if (temp + g[next[i]] > K)
                    {
                        break;
                    }
                    temp += g[next[i]];
                    next[i] = (next[i] + 1)%N;
                }
                val[i] = temp;
            }
        }
        memset(vist, -1, sizeof(vist));
       // test();
        memset(cc, 0, sizeof(cc));
        for (int i = 0, now = 0; i < R; i++)
        {
            if (vist[now] == -1)
            {
                total += val[now];
                vist[now] = i;
                now = next[now];
            }
            else
            {
                long long t = i - vist[now], tv = R - i;
                if (g[now] <= K)
                {
                    sum = cc[i] - cc[vist[now]];
                    total += tv/t*sum;
                    tv = tv%t;
                    for (int j = 0; j < tv; j++)
                    {
                        total += val[now];
                        now = next[now];
                    }
                }
                break;
            }
            cc[i+1] = total;
        }
        printf("Case #%d: %I64d\n", ++ca, total);
    }
    return 0;
}
