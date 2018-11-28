#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("A-small-attempt0.out","w",stdout);
    char map[26] = {'y','h','e','s','o','c','v',
                    'x','d','u','i','g','l','b',
                    'k','r','z',    't','n','w',
                    'j','p','f',    'm','a','q'};
    char str[105];
    int t;
    scanf("%d",&t);getchar();
    for(int cases = 1;cases<=t;++cases)
    {
        gets(str);
        for(int i=0;str[i];++i) if(str[i]!=' ')str[i] = map[str[i]-'a'];
        printf("Case #%d: %s\n",cases,str);
    }
    return 0;
}
