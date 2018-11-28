#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_L   (15 + 1)
#define MAX_D   (5000 + 1)

char dict[MAX_D][MAX_L];

char table[MAX_L][BUFSIZ];
int count[MAX_L];

int match(char *s)
{
    int n = strlen(s);
    int i;
    int j;

    for (i = 0; i < n; i++)
    {
        int found = -1;
        for (j = 0; j < count[i]; j++)
        {
            if (table[i][j] == s[i])
            {
                found = j; // break;
            }
        }

        if (-1 == found)
        {
            return 0;
        }
    }

    return 1;
}

void create_table(char *p)
{
    int pn = strlen(p);
    int i;
    int bInner;
    int pos;
    
    // init
    for (i = 0; i < MAX_L; i++)
    {
        count[i] = 0;
        table[i][0] = '\0';
    }

    // create table
    bInner = 0;
    pos = 0;
    for (i = 0; i < pn; i++)
    {
        if ('(' == p[i])
        {
            bInner = 1;
        }
        else
        if (')' == p[i])
        {
            bInner = 0;
            pos++;
        }
        else
        {
            if (bInner)
            {
                table[pos][ count[pos] ] = p[i];
                count[pos]++;
                table[pos][ count[pos] ] = '\0';
            }
            else
            {
                table[pos][0] = p[i];
                table[pos][1] = '\0';
                count[pos]++;
                pos++;
            }
        }
    }

}

int main(void)
{
    FILE * fin = fopen("A-large.in", "r");
    FILE * fex = fopen("output.txt", "w");
    int i,j;
    int L,D,N;
    char buf[BUFSIZ];
    int count;

    fscanf(fin, "%d%d%d", &L, &D, &N);

    for (i = 0; i < D; i++)
    {
        fscanf(fin, "%s\n", dict[i]);
    }

    for (i = 0; i < N; i++)
    {
        fgets(buf, BUFSIZ, fin);
        create_table(buf);
        count = 0;
        for (j = 0; j < D; j++)
        {
            if (match(dict[j]))
            {
                count++;
            }
        }

        fprintf(fex, "Case #%d: %d\n", i+1, count);
    }


    fclose(fin);
    fclose(fex);

    return 0;
}
