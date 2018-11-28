#include <cstdio>
#include <cstring>

int main ()
{
    char map[26] = {
        'y', 'h', 'e', 's', 'o', 'c', 'v',
        'x', 'd', 'u', 'i', 'g', 'l', 'b',
        'k', 'r', 'z', 't', 'n', 'w',
        'j', 'p', 'f', 'm', 'a', 'q',
    };
    int n;
    scanf("%d\n", &n);
    char line[101];
    for (int i = 1; i <= n; i++)
    {
        gets(line);
        printf("Case #%d: ", i);
        for (int j = 0; j < strlen(line); j++)
            if (line[j] == ' ')
                putchar(' ');
            else
                putchar(map[line[j] - 'a']);
        putchar('\n');
    }
    return 0;
}