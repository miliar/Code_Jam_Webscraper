#include <iostream>
#include <cstring>
#include <cstdio>
#define maxn 1037
using namespace std;

char str[maxn];
char y[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char cy[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
    freopen("A-small-attempt0 (1).in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,cas = 1;
    scanf("%d",&t);
    getchar();
    while (t--)
    {
        gets(str);
        int len = strlen(str);
        printf("Case #%d: ",cas++);
        for (i = 0; i < len; ++i)
        {
            if (str[i] >= 'a' && str[i] <= 'z')
            {
                printf("%c",cy[str[i] - 'a']);
            }
            else if (str[i] == ' ')
            {
                printf("%c",str[i]);
            }
        }
        printf("\n");
    }
    return 0;
}
