#include <stdio.h>
#include <string.h>

char a[1000], b[1000];
char map[1000], s[1000];

int main()
{
    scanf("%s%s", a, b);
    for (int i = 0; i < strlen(a); i++)
        map[a[i]] = b[i];
    map['q'] = 'z';
    map['z'] = 'q';

    int n;
    scanf("%d ", &n);
    for (int i = 1; i <= n; i++) {
        gets(s);
        printf("Case #%d: ", i);
        for (int i = 0; i < strlen(s); i++) 
            if (s[i] == ' ')
                putchar(' ');
            else
            putchar(map[s[i]]);
        puts("");
    }
}
