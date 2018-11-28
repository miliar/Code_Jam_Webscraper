#include <stdio.h>
#include <string.h>

FILE *fin, *fout;
int S, Q, dap;
char inp[110][210];
char qry[1010][210];
int limit[110];

void input()
{
    int i;
    char c;

    fscanf(fin, "%d", &S);
    fscanf(fin, "%c", &c);
    for(i=1; i<=S; i++)
        fgets(inp[i], 200, fin);

    fscanf(fin, "%d", &Q);
    fscanf(fin, "%c", &c);
    for(i=1; i<=Q; i++)
        fgets(qry[i], 200, fin);
}

void proc()
{
    int i, j, uplimit = 1;
    int max, maxin;

    dap = 0;
    while(1) {
        max = 0;
        for(i=1; i<=S; i++) {
            limit[i] = 99999999;

            for(j=uplimit; j<=Q; j++) {
                if(strcmp(inp[i], qry[j]) == 0) {
                    limit[i] = j;
                    break;
                }
            }
        }

        for(i=1; i<=S; i++) {
            if(max < limit[i]) {
                max = limit[i];
                maxin = i;
            }
        }

        uplimit = max;

        if(max == 99999999)
            break;

        dap++;
    }
}

void output(int casei)
{
    fprintf(fout, "Case #%d: %d\n", casei, dap);
}

int main()
{
    int casei, casen;

    fin = fopen("input.txt", "r");
    fout = fopen("output.txt", "w");

    fscanf(fin, "%d", &casen);

    for(casei=1; casei<=casen; casei++) {
        input();
        proc();
        output(casei);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
