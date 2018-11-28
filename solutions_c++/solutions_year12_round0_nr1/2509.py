#include <stdio.h>
#include <string.h>

char translate(char c)
{
    switch(c)
    {
        case 'a':
            return 'y';
            break;
        case 'b':
            return 'h';
            break;
        case 'c':
            return 'e';
            break;
        case 'd':
            return 's';
            break;
        case 'e':
            return 'o';
            break;
        case 'f':
            return 'c';
            break;
        case 'g':
            return 'v';
            break;
        case 'h':
            return 'x';
            break;
        case 'i':
            return 'd';
            break;
        case 'j':
            return 'u';
            break;
        case 'k':
            return 'i';
            break;
        case 'l':
            return 'g';
            break;
        case 'm':
            return 'l';
            break;
        case 'n':
            return 'b';
            break;
        case 'o':
            return 'k';
            break;
        case 'p':
            return 'r';
            break;
        case 'q':
            return 'z';
            break;
        case 'r':
            return 't';
            break;
        case 's':
            return 'n';
            break;
        case 't':
            return 'w';
            break;
        case 'u':
            return 'j';
            break;
        case 'v':
            return 'p';
            break;
        case 'w':
            return 'f';
            break;
        case 'x':
            return 'm';
            break;
        case 'y':
            return 'a';
            break;
        case 'z':
            return 'q';
            break;
    }


    return c;
}

int main()
{
    int T = 0;
    char str[100000];

    scanf("%d\n", &T);

    for(int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);

        memset(str, 0, sizeof(str));
        gets(str);

        for(int i = 0; i < strlen(str); i++)
        {
            printf("%c", translate(str[i]));
        }

        if(i != T)
        {
            printf("\n");
        }
    }

    return 0;
}