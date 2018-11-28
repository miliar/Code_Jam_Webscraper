#include <stdio.h>
 
char g[4][4];
bool complete(void)
{
for(int i = 0; i < 4; i++)
    for(int j = 0; j < 4; j++)
                if(g[i][j] == '.')
                        return false;
return true;
}
 
bool won(char c)
{
bool retv = false;
for(int i = 0; i < 4; i++)
        if((g[i][0] == c || g[i][0] == 'T') && (g[i][1] == c || g[i][1] == 'T') && (g[i][2] == c || g[i][2] == 'T') && (g[i][3] == c || g[i][3] == 'T'))
                retv = true;
for(int i = 0; i < 4; i++)
        if((g[0][i] == c || g[0][i] == 'T') && (g[1][i] == c || g[1][i] == 'T') && (g[2][i] == c || g[2][i] == 'T') && (g[3][i] == c || g[3][i] == 'T'))
                retv = true;
if((g[0][0] == c || g[0][0] == 'T') && (g[1][1] == c || g[1][1] == 'T') && (g[2][2] == c || g[2][2] == 'T') && (g[3][3] == c || g[3][3] == 'T'))
        retv = true;
if((g[0][3] == c || g[0][3] == 'T') && (g[1][2] == c || g[1][2] == 'T') && (g[2][1] == c || g[2][1] == 'T') && (g[3][0] == c || g[3][0] == 'T'))
        retv = true;
return retv;
}
int
main(void)
{
int t, t2 = 1;
scanf("%d", &t);
while(t--)
        {
        printf("Case #%d: ", t2++);
        for(int i = 0; i < 4; i++)
                for(int j = 0; j < 4; j++)
                        scanf(" %c", &g[i][j]);
        if(won('X'))
                printf("X won\n");
        else if(won('O'))
                printf("O won\n");
        else if(complete())
                printf("Draw\n");
        else
                printf("Game has not completed\n");
        }
return 0;
}
