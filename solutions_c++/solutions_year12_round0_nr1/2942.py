#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("aop.txt","w",stdout);

    int t,i,j,l;

    char g[250];
    char dmap[26]= {'y','h','e','s','o','c','v','x','d','u','i','g',
                    'l','b','k','r','z','t','n','w','j','p','f','m','a','q'
                   };

    scanf("%d",&t);
    for(j=1; j<=t; j++)
    {
        scanf(" %[^\n]s",g);

        l=strlen(g);
        printf("Case #%d: ",j);
        for(i=0; i<l; i++)
            if(g[i]==' ')
                printf(" ");
            else
                printf("%c",dmap[g[i]-97]);

        printf("\n");
    }

    return 0;
}
