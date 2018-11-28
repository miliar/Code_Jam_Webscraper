#include <stdio.h>
#include <string.h>

char str[100];
int  a[256];

int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1; i<=t; i++)
    {
        scanf("%s",str);
        printf("Case #%d: ",i);
        int len = strlen(str);
        int cnt = 2;
        for(int j=0; j<256; j++)
            a[j] = -1;
        if( len == 1)
        {
            printf("1\n");
            continue;
        }
        else
        {
            a[str[0]] = 1;
            for(int j=1; j<len; j++)
                if( str[j]!= str[0])
                {
                    a[str[j]] = 0;
                    break;
                }
            for( int j=0; j<len; j++)
                if( a[str[j]] == -1)
                {
                    a[str[j]] = cnt;
                    cnt++;                 
                }
            long long re= 0, base = 1;
            for(int j = len-1; j>=0; j--)
            {
                re = re+ a[str[j]]*base;
                base = base*cnt;
            }
            printf("%I64d\n",re);
        }
    }
    return 0;
}
