#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 111

const char hash[] = "yhesocvxduiglbkrztnwjpfmaq";

int n;
char s[MAX_LEN];
char s1[MAX_LEN];

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    scanf("%d\n", &n);
    for(int i = 0; i < n; ++i)
    {
        gets(s);
        for(int j = 0; s[j] != '\0'; ++j)
        {
            if(s[j] != ' ')
                s1[j] = hash[s[j] - 'a'];
            else
                s1[j] = ' ';
        }
        s1[strlen(s)] = '\0';
        printf("Case #%d: %s\n", i + 1, s1);
    }
    return 0;
}
