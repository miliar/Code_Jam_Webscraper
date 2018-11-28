#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
char map[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
void chg(char c)
{
    if (c == ' ')
        printf(" ");
    else
        printf("%c",map[c - 'a']);
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    char s[105];
    scanf("%d",&T);
    getchar();
    for (int ca = 1; ca <= T; ca++)
    {
        gets(s);
        printf("Case #%d: ",ca);
        for (int i = 0; s[i] != '\0';++i)
            chg(s[i]);
        puts("");
    }
    return 0;
}
