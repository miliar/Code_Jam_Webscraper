#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const char m[100]={121,104,101,115,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113};

int main()
{
    int t;
    scanf("%d", &t);
    getchar();
    char ch[110];
    for (int tcase = 1; tcase <= t; tcase++)
    {
        gets(ch);
        printf("Case #%d: ", tcase);
        for (int i = 0; i < strlen(ch); i++)
        {
            if (ch[i] == ' ') printf(" ");
            else printf("%c", m[ch[i]-'a']);
        }
        printf("\n");
    }
    return 0;
}
