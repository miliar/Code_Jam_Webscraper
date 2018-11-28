#include <stdio.h>
#include <string.h>
#define MAXN 104

char chwd(char ch)
{
    if(ch == 'a')   return 'y';
    if(ch == 'b')   return 'h';
    if(ch == 'c')   return 'e';
    if(ch == 'd')   return 's';
    if(ch == 'e')   return 'o';
    if(ch == 'f')   return 'c';
    if(ch == 'g')   return 'v'; //?
    if(ch == 'h')   return 'x';
    if(ch == 'i')   return 'd';
    if(ch == 'j')   return 'u';
    if(ch == 'k')   return 'i';
    if(ch == 'l')   return 'g';
    if(ch == 'm')   return 'l';
    if(ch == 'n')   return 'b';
    if(ch == 'o')   return 'k';
    if(ch == 'p')   return 'r';
    if(ch == 'q')   return 'z';
    if(ch == 'r')   return 't';
    if(ch == 's')   return 'n';
    if(ch == 't')   return 'w';
    if(ch == 'u')   return 'j';
    if(ch == 'v')   return 'p';
    if(ch == 'w')   return 'f';
    if(ch == 'x')   return 'm';
    if(ch == 'y')   return 'a';
    if(ch == 'z')   return 'q'; //?
    return ch;
}
int main()
{
    int count, tmpi;
    freopen ("q1.out", "w+", stdout);
    freopen ("q1.in", "r", stdin);
    scanf("%d\n", &count);

    for(tmpi = 1; tmpi <= count; tmpi++)
    {

        char str[MAXN];
        int tmpj;
        gets(str);
        for(tmpj = 0; tmpj < strlen(str); tmpj++)
            str[tmpj] = chwd(str[tmpj]);
        printf("Case #%d: %s\n", tmpi, str);
    }
}
