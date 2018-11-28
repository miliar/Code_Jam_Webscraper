#include <stdio.h>
#include <stdlib.h>


inline int solve(char table[4][4])
{
    int count = 0;
    char val;
    bool undefined = true;
    for (int j = 0; j < 4; j++)
    {
        if (table[0][j] == '.')
            continue;
        val=table[0][j];
        undefined = true;
        count = 0;
        for(int k=0; k<4; k++)
        {
            if (table[k][j] == '.')
                break;

            if (undefined) {
                if ('.' != table[k][j]  && 'T' != table[k][j])
                    {
                        val = table[j][k];
                        undefined = false;
                    }
            }

            if (val == table[k][j] || table[k][j]=='T') {
                count++;
                if (count == 4)
                {
                    return (int)(val);
                }
            }

        }
    }
    count = 0;
    undefined = true;
    for (int j = 0; j < 4; j++)
    {
        if (table[j][0] == '.')
            continue;
        val=table[j][0];
        undefined = true;
        count = 0;
        for(int k=0; k<4; k++)
        {
            if (table[j][k] == '.')
                break;

            if (undefined) {
                if ('.' != table[j][k]  && 'T' != table[j][k])
                    {
                        val = table[j][k];
                        undefined = false;
                    }
            }

            if (val == table[j][k] || table[j][k]=='T') {
                count++;
                if (count == 4)
                {
                    return (int)(val);
                }
            }

        }
    }
    // diags :
    val = table[0][0];
    if (val != '.') {
        undefined = true;
        for (int i = 0; i < 4; i++)
        {
            if (table[i][i] == '.')
            {
                undefined = true;
                break;
            }
            if (undefined && table[i][i] != 'T')
            {
                val = table[i][i];
                undefined = false;
            }
            if (table[i][i] != 'T' && table[i][i] != val)
            {
                undefined = true;
                break;
            }
        }
        if (!undefined)
        {
            return (int)(val);
        }
    }
    val = table[0][3];
    if (val != '.') {
        undefined = true;
        for (int i = 0; i < 4; i++)
        {
            if (table[i][3-i] == '.')
            {
                undefined = true;
                break;
            }
            if (undefined && table[i][3-i] != 'T')
            {
                val = table[i][3-i];
                undefined = false;
            }
            if (table[i][3-i] != 'T' && table[i][3-i] != val)
            {
                undefined = true;
                    break;
            }
        }
        if (!undefined)
        {
            return (int)(val);
        }
    }
    for (int i = 0; i < 16; i++)
    {
        if (table[i%4][i/4] == '.')
            return -1;
    }
    return 0;
}

int main()
{
    int count = 0;
    FILE* file;
    file = fopen("test.txt", "r");
    fscanf(file, "%i", &count);
    int* results = (int*)(malloc(sizeof(int)*count));
    for (int i = 0 ; i < count ; i++)
    {
        char tableau[4][4];
        for (int j = 0; j < 4; j++) {
            fscanf(file, "\n%c%c%c%c",&tableau[j][0],&tableau[j][1],&tableau[j][2],&tableau[j][3]);
        }
        results[i] = solve(tableau);
    }
    fclose(file);
    FILE* file2;
    file2 = fopen("testout.txt", "w");
    for (int i = 0; i < count ; i++)
    {
        fprintf(file2,"Case #%d: ", i+1);
        switch(results[i])
        {
            case -1:
            fprintf(file2, "Game has not completed");
            break;
            case 0:
            fprintf(file2,"Draw");
            break;
            case (int)('X'):
            fprintf(file2,"X won");
            break;
            case (int)('O'):
            fprintf(file2,"O won");
            break;
            default:
            break;
        }
        if (i!=count-1)
            fprintf(file2,"\n");
    }
    fclose(file2);
    return 0;
}
