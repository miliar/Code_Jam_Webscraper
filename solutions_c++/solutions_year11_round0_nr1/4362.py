//
//  main.cpp
//  google code jam
//
//  Created by Andriy Medvid' on 07.05.11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <cstdio>

int max(int a, int b)
{
    return a>b? a:b;
}

int abs(int a)
{
    return a < 0? -a:a;
}

int main ()
{
    int T, n, oLast, bLast, oTime, bTime, pos;
    char robot[3];
    freopen("result.txt", "w", stdout);
    scanf("%d", &T);
    for(int t = 0; t < T; t++)
    {
        oLast = 1;
        bLast = 1;
        oTime = 0;
        bTime = 0;
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            scanf("%s %d", &robot, &pos);
            if(robot[0] == 'O')
            {
                oTime = max(bTime+1, oTime + abs(pos - oLast) + 1);
                oLast = pos;
            }
            else
            {
                bTime = max(oTime+1, bTime + abs(pos - bLast) + 1);
                bLast = pos;
            }
        }
        printf("Case #%d: %d\n", t+1, max(oTime, bTime));
    }
    return 0;
}

