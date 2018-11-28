//
//  main.cpp
//  code_jam_a
//
//  Created by Andriy Medvid' on 14.04.12.
//  Copyright (c) 2012 taran studio. All rights reserved.
//

#include <iostream>

char translate[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(int argc, const char * argv[])
{
    int T;
    char str[110];
    freopen("a.out", "w", stdout);
    freopen("A-small-attempt2.in", "r", stdin);
    scanf("%d", &T);
    gets(str);
    for(int t = 0; t < T; t++)
    {
        gets(str);
        int i = 0;
        for(; str[i] > 31; i++)
        {
            if(str[i] >= 'a' && str[i] <= 'z')
            {
                str[i] = translate[str[i] - 'a'];
            }
        }
        str[i] = 0;
        printf("Case #%d: %s\n", t+1, str);
    }
    return 0;
}
