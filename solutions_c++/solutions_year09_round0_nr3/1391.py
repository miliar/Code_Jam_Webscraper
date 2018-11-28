#include <stdio.h>
#include <string.h>

int main()
{
    int N;
    int value;
    int a, b;
    int x, y;
    char text[1024];
    char pattern[] = "welcome to code jam";
    int table[1024][20], len;

    scanf("%d\n", &N);
    for(a = 1; a<=N; a++)
    {
        value = 0;
        fgets(text, sizeof(text), stdin);
        len = strlen(text);
        memset(table, 0, sizeof(int)*1024*20);

        y = 0;
        for(x=0; x<len; x++)
        {
            if( text[x]==pattern[y] )
            {
                if( x==0 )
                    table[x][y] = 1;
                else
                    table[x][y] = table[x-1][y]+1;
            }
            else
            {
                table[x][y] = x ? table[x-1][y] : 0;
            }
        }
        for(y=1; y<19; y++)
        {
            for(x=y; x<len; x++)
            {
                if( text[x]==pattern[y] )
                {
                    table[x][y] = table[x-1][y]+table[x-1][y-1];
                }
                else
                    table[x][y] = table[x-1][y];
                table[x][y]%=10000;
            }
        }
/*
        for(y=0; y<19; y++)
        {
            for(x=0; x<len; x++)
                printf("%2d ", table[x][y]);
            printf("\n");
        }
*/
        printf("Case #%d: %04d\n", a, table[len-1][18]);
    }
    return 0;
}
