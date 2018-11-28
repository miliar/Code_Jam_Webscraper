//
//  main.cpp
//  google code jam
//
//  Created by Andriy Medvid' on 07.05.11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <cstdio>

int main ()
{

    int T, number, n, axor, min, sum;
    
    freopen("result.txt", "w", stdout);    
    scanf("%d", &T);
    for(int t = 0; t < T; t++)
    {
        axor = 0;
        sum = 0;
        min = 100000000;
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            scanf("%d", &number);
            sum += number;
            if(number < min)
                min = number;
            axor ^= number;
        }
        if(axor)
            printf("Case #%d: NO\n", t+1);
        else
            printf("Case #%d: %d\n", t+1, sum - min);
    }
    
    return 0;
}

