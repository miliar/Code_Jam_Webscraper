#include<stdio.h>
#include<stdlib.h>

char map[26] = {'y','h','e','s','o','c',
                'v','x','d','u','i','g',
                'l','b','k','r','z','t',
                'n','w','j','p','f','m',
                'a','q'};

char s[110];

int main()
{
    freopen("A-small-attempt0.in","rt",stdin);
    freopen("A-small-attempt0.out","wt",stdout);
    int tcase,i,j;
    scanf("%d",&tcase);
    for(i=1;i<=tcase;i++)
    {
        scanf(" %[^\n]",&s);
        printf("Case #%d: ",i);
        for(j=0;s[j]!='\0';j++)
            if(s[j]!=' ')
                printf("%c",map[s[j]-'a']);
            else
                printf(" ");
        printf("\n");
    }
    return 0;
}
