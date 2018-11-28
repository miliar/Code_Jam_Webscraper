#include <stdio.h>

char f[4][4];

int main()
{
    FILE * fin = fopen("A-large.in", "r");
    FILE * fout = fopen("A-large.out", "w");
    bool over_flag, t_flag, none_flag;
    int x_num, o_num;
    int i, j;
    int t, num_t = 1;

    fscanf(fin, "%d\n", &t);
    for (; num_t <= t; num_t++)
    {
        for (i = 0; i < 4; i++)
        {
            for (j = 0; j < 4; j++)
                fscanf(fin, "%c", &f[i][j]);
            fscanf(fin, "\n");
        }
        fscanf(fin, "\n");

        over_flag = false;
        none_flag = false;
        for (i = 0; i < 4; i++)
        {
            //row
            t_flag = false;
            x_num = 0;
            o_num = 0;
            for (j = 0; j < 4; j++)
                if ( f[i][j] == 'X' )
                    x_num++;
                else if ( f[i][j] == 'O' )
                    o_num++;
                else if ( f[i][j] == 'T' )
                    t_flag = true;
                else
                    none_flag = true;
            if ( x_num == 4  ||  (t_flag && x_num == 3) )
            {
                fprintf(fout, "Case #%d: X won\n", num_t);
                over_flag = true;
                break;
            }
            if ( o_num == 4  ||  (t_flag && o_num == 3) )
            {
                fprintf(fout, "Case #%d: O won\n", num_t);
                over_flag = true;
                break;
            }

            //column
            t_flag = false;
            x_num = 0;
            o_num = 0;
            for (j = 0; j < 4; j++)
                if ( f[j][i] == 'X' )
                    x_num++;
                else if ( f[j][i] == 'O' )
                    o_num++;
                else if ( f[j][i] == 'T' )
                    t_flag = true;
                else
                    none_flag = true;
            if ( x_num == 4  ||  (t_flag && x_num == 3) )
            {
                fprintf(fout, "Case #%d: X won\n", num_t);
                over_flag = true;
                break;
            }
            if ( o_num == 4  ||  (t_flag && o_num == 3) )
            {
                fprintf(fout, "Case #%d: O won\n", num_t);
                over_flag = true;
                break;
            }
        }
        if ( over_flag )
            continue;

        //left
        t_flag = false;
        x_num = 0;
        o_num = 0;
        for (i = 0; i < 4; i++)
            if ( f[i][i] == 'X' )
                x_num++;
            else if ( f[i][i] == 'O' )
                o_num++;
            else if ( f[i][i] == 'T' )
                t_flag = true;
            else
                none_flag = true;
        if ( x_num == 4  ||  (t_flag && x_num == 3) )
        {
            fprintf(fout, "Case #%d: X won\n", num_t);
            over_flag = true;
            continue;
        }
        if ( o_num == 4  ||  (t_flag && o_num == 3) )
        {
            fprintf(fout, "Case #%d: O won\n", num_t);
            over_flag = true;
            continue;
        }

        //right
        t_flag = false;
        x_num = 0;
        o_num = 0;
        for (i = 0; i < 4; i++)
            if ( f[i][3-i] == 'X' )
                x_num++;
            else if ( f[i][3-i] == 'O' )
                o_num++;
            else if ( f[i][3-i] == 'T' )
                t_flag = true;
            else
                none_flag = true;
        if ( x_num == 4  ||  (t_flag && x_num == 3) )
        {
            fprintf(fout, "Case #%d: X won\n", num_t);
            over_flag = true;
            continue;
        }
        if ( o_num == 4  ||  (t_flag && o_num == 3) )
        {
            fprintf(fout, "Case #%d: O won\n", num_t);
            over_flag = true;
            continue;
        }

        if ( none_flag )
            fprintf(fout, "Case #%d: Game has not completed\n", num_t);
        else
            fprintf(fout, "Case #%d: Draw\n", num_t);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
