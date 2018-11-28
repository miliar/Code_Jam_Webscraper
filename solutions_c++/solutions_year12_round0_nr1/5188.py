#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    int t, i, j;
    char str[105];

    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);

    gets(str);
    sscanf(str, "%d", &t);
    //printf("%d\n",t);
    //system("pause");
    for( i = 1; i <= t; i++)
    {
        gets(str);
        printf("Case #%d: ", i);
        for( j = 0; str[j] != '\0'; j++)
        {
            if( 'a' <= str[j] && str[j] <= 'z')
            {
                if(str[j] == 'a')str[j] = 'y';
                else if(str[j] == 'b')str[j] = 'h';
                else if(str[j] == 'c')str[j] = 'e';
                else if(str[j] == 'd')str[j] = 's';
                else if(str[j] == 'e')str[j] = 'o';
                else if(str[j] == 'f')str[j] = 'c';
                else if(str[j] == 'g')str[j] = 'v';
                else if(str[j] == 'h')str[j] = 'x';
                else if(str[j] == 'i')str[j] = 'd';
                else if(str[j] == 'j')str[j] = 'u';
                else if(str[j] == 'k')str[j] = 'i';
                else if(str[j] == 'l')str[j] = 'g';
                else if(str[j] == 'm')str[j] = 'l';
                else if(str[j] == 'n')str[j] = 'b';
                else if(str[j] == 'o')str[j] = 'k';
                else if(str[j] == 'p')str[j] = 'r';
                else if(str[j] == 'q')str[j] = 'z';
                else if(str[j] == 'r')str[j] = 't';
                else if(str[j] == 's')str[j] = 'n';
                else if(str[j] == 't')str[j] = 'w';
                else if(str[j] == 'u')str[j] = 'j';
                else if(str[j] == 'v')str[j] = 'p';
                else if(str[j] == 'w')str[j] = 'f';
                else if(str[j] == 'x')str[j] = 'm';
                else if(str[j] == 'y')str[j] = 'a';
                else if(str[j] == 'z')str[j] = 'q';
            }
            printf("%c", str[j]);
        }
        printf("\n");
    }
}
