//
//  main.cpp
//  code_jam_c
//
//  Created by Andriy Medvid' on 14.04.12.
//  Copyright (c) 2012 taran studio. All rights reserved.
//

#include <iostream>

int getRange(int a)
{
    int res;
    for(res = 0; a > 0; res++)
    {
        a /= 10;
    }
    return res;
}

int powers[8] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

int main(int argc, const char * argv[])
{
    int T;
    int a, b, result;
    int help;
    int arr[10];
    freopen("c.out", "w", stdout);
    freopen("C-large.in", "r", stdin);
    scanf("%d", &T);
    for(int t = 0; t < T; t++)
    {
        result = 0;
        scanf("%d%d", &a, &b);
        for(int i = a; i <= b; i++)
        {
            int len = getRange(i);
            int k = 0;
            for(int j = 0; j < len - 1; j++)
            {
                help = (i / powers[j+1]) + (i % powers[j+1])*powers[len - j - 1];
                if(help != i && help >= a && help <= b)
                {
                    bool was = false;
                    
                    for(int iter = 0; iter < k; iter++)
                    {
                        if(arr[iter] == help)
                            was = true;
                    }
                    
                    if(getRange(help) == len && !was)
                    {
                        arr[k] = help;
                        result++;
                        k++;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", t+1, result/2);
    }
    
    return 0;
}

