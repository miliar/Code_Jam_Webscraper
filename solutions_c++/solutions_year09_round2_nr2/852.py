#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <ctime>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cassert>
#include<cstring>
using namespace std;

int main()
{
    int kaseno, kases;
    for(scanf("%d",&kases), kaseno = 1; kaseno <= kases; ++kaseno)
    {
        int ret = -1;
        long long num;
        char str[1001] = {0};
        for(int i = 0; i < 1000; ++i)
        {
            str[i] = '0';
        }
        scanf("%s",str+20);
        next_permutation(str, str + strlen(str));
        int i = 0;
        int len = strlen(str);
        for(i = 0; i < len; ++i)
            if(str[i] != '0')
            {
                printf("Case #%d: %s\n",kaseno, str + i);
                break;
            }
    }

}
