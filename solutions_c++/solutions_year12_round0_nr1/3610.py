#include <stdio.h>
#include <string.h>

char dic[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char str[110];
int ncase;

int main()
{
    while ( EOF != scanf("%d", &ncase) )
    {
        getchar();
        for ( int icase = 1 ; icase <= ncase; icase++ )
        {
            gets(str);
            int len = strlen(str);
            printf("Case #%d: ", icase);
            for ( int i = 0 ; i < len ; i++ )
                if (' '==str[i])
                    printf(" ");
                else printf("%c", dic[str[i]-'a']);
            putchar(10);
        }
    }
    return 0;
}
