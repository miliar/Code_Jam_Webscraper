#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
const int maxn=1000;
char ch[maxn+10];
char gl[]={'e', 'a', 'z', 'j', 'p', 'm', 's', 'l', 'c', 'y', 'k', 'd', 'x', 'v', 'n', 'r', 'i', 'b', 't', 'h', 'w', 'f', 'o', 'u', 'g', 'q'};
char normal[]={'o', 'y', 'q', 'u', 'r', 'l', 'n', 'g', 'e', 'a', 'i', 's', 'm', 'p', 'b', 't', 'd', 'h', 'w', 'x', 'f', 'c', 'k', 'j', 'v', 'z'};
int t, cnt;
int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    getchar();
    cnt=1;
    while (t--)
    {
        gets(ch);
        int len=strlen(ch);
        for (int i=0; i<len; i++)
        {
            if (ch[i]==' ') continue;
            for (int j=0; j<26; j++)
            {
                if (ch[i]!=gl[j]) continue;
                ch[i]=normal[j];
                break;
            }
        }
        printf("Case #%d: ", cnt++);
        puts(ch);
    }
    return 0;
}
