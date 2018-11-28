#include<stdio.h>
#include<string.h>

char table[5][5];

int solve(char c0, char c1, char c2, char c3)
{
    char tmp[5];
    tmp[0] = c0; tmp[1] = c1; tmp[2] = c2; tmp[3] = c3; tmp[4] = '\0';
    if(!strcmp(tmp, "OOOO") || !strcmp(tmp, "OOOT") || !strcmp(tmp, "OOTO") || !strcmp(tmp, "OTOO") || !strcmp(tmp, "TOOO"))
    {
        printf("O won\n");
        return 1;
    }
    if(!strcmp(tmp, "XXXX") || !strcmp(tmp, "XXXT") || !strcmp(tmp, "XXTX") ||  !strcmp(tmp, "XTXX") || !strcmp(tmp, "TXXX"))
    {
        printf("X won\n");
        return 1;
    }
    
    return 0;
}

bool isComplete()
{
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            if(table[i][j] == '.')
                return false;
    return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
    freopen("out.txt", "w", stdout);
#endif

    int t;
    scanf("%d\t", &t);

    for(int i = 1; i <= t; i++)
    {
        for(int j = 0; j < 4; j++)
            scanf("%s", table[j]);

        printf("Case #%d: ", i);
        if(solve(table[0][0], table[0][1], table[0][2], table[0][3]) || 
           solve(table[1][0], table[1][1], table[1][2], table[1][3]) ||
           solve(table[2][0], table[2][1], table[2][2], table[2][3]) ||
           solve(table[3][0], table[3][1], table[3][2], table[3][3]) ||
           solve(table[0][0], table[1][0], table[2][0], table[3][0]) ||
           solve(table[0][1], table[1][1], table[2][1], table[3][1]) ||
           solve(table[0][2], table[1][2], table[2][2], table[3][2]) ||
           solve(table[0][3], table[1][3], table[2][3], table[3][3]) ||
           solve(table[0][0], table[1][1], table[2][2], table[3][3]) ||
           solve(table[0][3], table[1][2], table[2][1], table[3][0]))
            continue;

        if(isComplete())
            printf("Draw\n");
        else
           printf("Game has not completed\n");


    }
	return 0;

}
