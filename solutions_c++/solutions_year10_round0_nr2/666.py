/* 
 * File:   main.cpp
 * Author: Tim
 *
 * Created on 08 May 2010, 01:12
 */

#include <stdlib.h>
#include <stdio.h>
#include <sys/unistd.h>

typedef int64_t tint;

inline tint abs(tint a)
{
    return (a < 0) ? -a : a;
}

inline tint mod(tint a, tint b)
{
    tint div = a / b;
    return a - div * b;
}

tint gcd(tint a, tint b)
{
    while (b != 0)
    {
        tint t = b;
        b = mod(a, b);
        a = t;
    }
    return a;
}

tint solve(tint N, tint *t)
{
    tint opt = abs(t[0] - t[1]);
    
    for (int n = 1; n < N - 1; n++)
    {
        const tint d = abs(t[n] - t[n+1]);
        if (opt != d)
        {
            opt = gcd(d, opt);
        }
    }
    // opt should now contain the gcd of all the differences

    tint next = opt - mod(t[N-1], opt);
    
    if (next == opt) return 0;
    return next;
}

int main(int argc, char** argv)
{
    int Tests;
    scanf("%d", &Tests);

    tint t[1024];

    for (int test = 1; test <= Tests; test++)
    {   
        int N;
        scanf("%d", &N);
        
        for (int i = 0; i < N; i++)
        {
            scanf("%llu", &t[i]);
        }
        
        tint y = solve(N, t);
        printf("Case #%d: %llu\n", test, y);

        fprintf(stderr, "Done test %d\n", test);
    }
    return (EXIT_SUCCESS);
}
