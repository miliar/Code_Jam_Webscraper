#include <stdio.h>
#include <string.h>

char map[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    int cas = 1;
    char str[1000];
    int n;
    scanf("%d", &n);
    getchar();
    while(n--)
    {
        gets(str);
        int len = strlen(str);
        printf("Case #%d: ",cas++);
        for (int i = 0; i < len; i++)
        {
            if(str[i] == ' ')
                putchar(' ');
            else if(str[i] =='\0')
                break;
            else
                putchar(map[str[i]-'a']);
        }
        printf("\n");
    }
    return 0;
}
