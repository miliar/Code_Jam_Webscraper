#include<stdio.h>


__int64 g[1200], R, K, N;
__int64 sum[1200], round[1200];
__int64 fee[1200];
bool exist[1200];
// find the largest integer t such that sum[t] <= s
__int64 bsearch(__int64 s)
{
    __int64 min, max, mid;
    if(sum[0] > s)
        return -1;
    min = 0; max = N - 1;
    while(min < max)
    {
        mid = (min + max) / 2 + 1;
        if(sum[mid] <= s)
            min = mid;
        else
            max = mid - 1;
    }
    return min;
}


int main()
{
    __int64 t, test;
    scanf("%I64d", &t);
    __int64 i, rou, first, last, s, ans, res, div, start, period;
    for(test = 1; test <= t; test ++)
    {
        scanf("%I64d%I64d%I64d", &R, &K, &N);
        for(i = 0; i < N; i ++)
        {
            scanf("%I64d", g + i);
            if(i == 0)
                sum[0] = g[i];
            else
                sum[i] = sum[i - 1] + g[i];
            exist[i] = false;
        }
        if(sum[N - 1] <= K)
        {
            printf("Case #%I64d: %I64d\n", test, R * sum[N - 1]);
            continue;
        }
        rou = 1;
        first = 0;
        while(1)
        {
            round[rou] = first;
            exist[first] = true;
            rou ++; 
            if(first == 0)
                s = K;
            else if(sum[N - 1] - sum[first - 1] >= K)
                s = K + sum[first - 1];
            else
                s =  K - sum[N - 1] + sum[first - 1];
            last = bsearch(s);
            if(last >= first)
            {
                if(first == 0)
                    fee[first] = sum[last];
                else
                    fee[first] = sum[last] - sum[first - 1];
            }
            else
                fee[first] = sum[N - 1] - sum[first - 1] + sum[last];
            first = (last + 1) % N;
            if(exist[first])
            {
                round[rou] = first;
                break;
            }  
        }
        ans = 0;
        
        for(i = 1;; i ++)
            if(round[i] == round[rou])
                break;
            else
                ans += fee[round[i]];
        start = i;
        R = R - start + 1;
        div = R / (rou - start);
        res = R % (rou - start);
        period = 0;
        for(i = start; i < rou; i ++)
            period += fee[round[i]];
        for(i = start; i < res + start; i ++)
            ans += fee[round[i]];
        ans = ans + period * div;
        printf("Case #%I64d: %I64d\n", test, ans);        
                
    }
    return 0;
} 
