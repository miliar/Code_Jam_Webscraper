#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 0x3fffffff
#define LL long long

int mapping[26]={24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16};
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t, i, cas = 1;
    char str[105];
    scanf("%d", &t);
    getchar();
    while(t--)
    {
        gets(str);
        int len = strlen(str);
        for(i = 0; i < len; i++)
        {
            if(str[i] == ' ')   continue;
            str[i] = 'a' + mapping[str[i] - 'a'];
        }
        printf("Case #%d: %s\n", cas++, str);
    }
    return 0;
}
