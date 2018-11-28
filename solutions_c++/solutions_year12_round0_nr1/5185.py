#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char map[26]=
    {'y','h','e','s','o','c','v','x','d','u','i',
                'g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};



char str[100000];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int cas; cin >> cas;
    getchar();
    for(int i = 1; i <= cas; i++)
    {
        gets(str);
        int len = strlen(str);
        printf("Case #%d: ", i);
        for(int j = 0; j < len ;j++)
            if(str[j] == ' ')
                printf("%c", str[j]);
            else printf("%c", map[str[j]-'a']);
        printf("\n");
    }
    return 0;
}
