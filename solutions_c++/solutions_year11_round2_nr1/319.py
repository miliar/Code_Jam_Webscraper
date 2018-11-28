#include <stdio.h>
#include <assert.h>
#include <string.h>

int T;              // no of test cases

int N;              // no of teams
char schedule[200][200];
float wp[100];  // winning percentage
int games[100]; // games each team has played
float owp[100]; // opponent winning percentage
float oowp[100]; // opponent-opponent winning percentage
float rpi[100]; // the RPI


void calcRPI()
{
    // calculate wp;
    for(int i=0;i<N;i++)
    {
        games[i]=0;
        wp[i]=0;
        for(int j=0;j<N;j++)
        {
            if(schedule[i][j] != '.')
            {
                games[i]++;
            }
            if(schedule[i][j] == '1')
            {
                wp[i]++;
            }
        }
        wp[i] = wp[i] / games[i];
    }

    // calculate owp
    for(int i=0;i<N;i++)
    {
        owp[i]=0;
        int owp_count=0;
        for(int j=0;j<N;j++)
        {
            if(schedule[i][j] != '.')
            {
                owp_count++;
                float wp = 0;
                float wp_count = 0;
                for(int k=0;k<N;k++)
                {
                    if(schedule[j][k]!='.' && i!=k)
                    {
                        wp_count++;
                        if(schedule[j][k] == '1') wp++;
                    }
                }
                wp /= wp_count;
                owp[i] += wp;
            }
        }
        owp[i] /= owp_count;
    }

    // calculate oowp
    for(int i=0;i<N;i++)
    {
        int oowp_count = 0;
        oowp[i] = 0;
        for(int j=0;j<N;j++)
        {
            if(schedule[i][j] != '.')
            {
                oowp_count++;
                oowp[i] += owp[j];
            }
        }
        oowp[i] /= oowp_count;
    }

    // calculate rpi
    for(int i=0;i<N;i++)
    {
        rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
    }
}

int main()
{
    FILE *fp = fopen("c:\\inp.txt", "r+"); // get input data from file
    fscanf(fp, "%d", &T);

    FILE *fpo = fopen("c:\\op.txt", "w+"); // write op data to file

    for(int c=1;c<=T;c++)    // process each test case
    {
        fscanf(fp, "%d", &N);
        for(int i=0;i<N;i++)
            fscanf(fp, "%s", &schedule[i]);

        calcRPI();

        fprintf(fpo, "Case #%d:\n", c);
        for(int i=0;i<N;i++)
            fprintf(fpo, "%f\n", rpi[i]);

    }

    fclose(fp);
    fclose(fpo);
    return 0;
}

