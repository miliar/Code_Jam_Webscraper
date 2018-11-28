#include <cstdio>
#include <cstdlib>
char a[4][5];
bool wins(char p)
{
    int i, c, j;
    for(i = 0; i < 4; i++)
    {
        c = 0;
        for(j = 0; j < 4; j++)
            if(a[i][j] == p || a[i][j] == 'T')
                c++;
        if(c == 4)
            return true;
        c = 0;
        for(j = 0; j < 4; j++)
            if(a[j][i] == p || a[j][i] == 'T')
                c++;
        if(c == 4)
            return true;
    }
    c = 0;
    for(i = 0; i < 4; i++)
        if(a[i][i] == p || a[i][i] == 'T')
            c++;
    if(c == 4)
        return true;
    c = 0;
    for(i = 0; i < 4; i++)
        if(a[i][3 - i] == p || a[i][3 - i] == 'T')
            c++;
    return c == 4;
}
bool completed()
{
    int i, j;
    for(i = 0; i < 4; i++)
        for(j = 0; j < 4; j++)
            if(a[i][j] == '.')
                return false;
    return true;
}
int main()
{
    FILE *fin = fopen("Tic-Tac-Toe-Tomek.in", "r"), *fout = fopen("Tic-Tac-Toe-Tomek.out", "w");
    int t, i, j, k, c;
    fscanf(fin, "%d", &t);
    for(i = 1; i <= t; i++)
    {
        fprintf(fout, "Case #%d: ", i);
        for(j = 0; j < 4; j++)
            fscanf(fin, "%s", a[j]);
        if(wins('X'))
            fprintf(fout, "X won\n");
        else if(wins('O'))
            fprintf(fout, "O won\n");
        else if(completed())
            fprintf(fout, "Draw\n");
        else
            fprintf(fout, "Game has not completed\n");
    }
    return 0;
}
