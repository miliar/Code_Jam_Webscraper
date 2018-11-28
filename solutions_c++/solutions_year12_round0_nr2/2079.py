//
//  main.cpp
//  code_jam_b
//
//  Created by Andriy Medvid' on 14.04.12.
//  Copyright (c) 2012 taran studio. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[])
{
    int T;
    int n, s, p, arr[110], clear = 0, dirty = 0;
    freopen("b.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    scanf("%d", &T);
    for(int t = 0; t < T; t++)
    {
        scanf("%d%d%d", &n, &s, &p);
        for(int i = 0; i < n; i++)
            scanf("%d", arr + i);
        
        clear = 0;
        dirty = 0;
        
        for(int i = 0; i < n; i++)
        {  
            if(arr[i] > (p - 1)*3)
            {
                clear++;
            }
            else if((arr[i] % 3 == 0) && (arr[i] / 3 > 0) && (arr[i] / 3 < 10) && (arr[i] / 3 + 1 >= p))
            {
                dirty++;
            }
            else if((arr[i] % 3 == 2) && (arr[i] / 3 < 9) && (arr[i] / 3 + 2 >= p))
            {
                dirty++;
            }
        }
        dirty = (dirty<s)?dirty:s;
        printf("Case #%d: %d\n", t+1, clear + dirty);
    }
    return 0;
}

