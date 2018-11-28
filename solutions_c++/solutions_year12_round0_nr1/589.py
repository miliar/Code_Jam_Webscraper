#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

char map[200],a,b,g[10000];


int main()
{
    int i,j,k,T,t,l;
    map['z']='q';

    freopen("out.txt","r",stdin);

    for(i=0;i<26;i++)
    {
        scanf("%c %c\n",&a,&b);
        map[a]=b;
    }

    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-out.txt","w",stdout);

    scanf("%d\n",&T);

    for(t=1;t<=T;t++)
    {
        gets(g);

        l=strlen(g);

        for(i=0;i<l;i++)
        {
            if(g[i]==' ') continue;
            g[i]=map[g[i]];
        }

        printf("Case #%d: ",t);
        puts(g);
    }

    return 0;
}



