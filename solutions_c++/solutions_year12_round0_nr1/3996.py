#include <stdio.h>

char code[] = {'y','h','e','s','o','c','v','x','d','u','i',
'g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    int test;
    scanf("%d",&test);
    char line[1000];
    gets(line);
    for (int cas = 1;cas <= test;cas++)
    {
        gets(line);
        printf("Case #%d: ",cas);
        for (int i=0;line[i]!=0;i++)
        if  (line[i] != ' ')
            putchar(code[line[i] - 'a']);
        else putchar(' ');
        puts("");
    }
}
