#include "stdio.h"
char* sin[3] = 
{
"ejp mysljylc kd kxveddknmc re jsicpdrys",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

char* sout[3] = 
{
"our language is impossible to understand",
"there are twenty six factorial possibilities",
 "so it is okay if you want to just give up"
};

char wdmap[256];

void setupmap()
{
    int i, j, k;
    for( i=0; i<256; i++)
        wdmap[i] = i;
    for( i=0; i<3; i++)
        for( j=0; sin[i][j]; j++)
            wdmap[sin[i][j]] = sout[i][j];
    wdmap['z'] = 'q';
    wdmap['q'] = 'z';
}

int main()
{
    setupmap();
    char str[2048];
    int cas;
    int t = 0;
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
    scanf("%d",&cas);
    getchar();
    while(cas--)
    {
        gets(str);
        int i = 0;
        for( i=0; str[i]; i++)
        {
            str[i] = wdmap[str[i]];
        }
        printf("Case #%d: %s\n", ++t,str);
    }
    return 0;
}
