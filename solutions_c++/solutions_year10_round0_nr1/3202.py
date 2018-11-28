#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define MAXWORDLEN  20
#define MAXLINELEN  1024

int main(int argc, char * argv[])
{
    FILE * fp = fopen(argv[1], "r");
    if (NULL == fp)
    {
        printf("Input File Not Exist!\n");
        return 1;
    }
    FILE * fOut = fopen("output.txt", "w");
    if (NULL == fOut)
    {
        printf("Cannot Open Output File!\n");
        fclose(fp);
        return 1;
    }

    int T;
    fscanf(fp, "%d", &T);
    for (int i=0; i<T; i++)
    {
        int N, K;
        fscanf(fp, "%d %d", &N, &K);
        vector <char> snaps;
        vector <char> stats;
        snaps.push_back(0);
        stats.push_back(1);
        for (int j=0; j<K; j++)
        {
            for (int k=0; k<stats.size(); k++)
            {
                if (stats[k])
                    snaps[k] = snaps[k] ^ 1;
                if (k>0)
                {
                    if (snaps[k-1] && stats[k-1])
                        stats[k] = 1;
                    else
                        stats[k] = 0;
                }
            }
            if (*(snaps.end()-1) && *(stats.end()-1))
            {
                snaps.push_back(0);
                stats.push_back(1);
            }
        }

        if (N < snaps.size() && snaps[N-1] && stats[N-1])
        {
            fprintf(fOut, "Case #%d: ON\n", i+1);
        }
        else
        {
            fprintf(fOut, "Case #%d: OFF\n", i+1);
        }
    }
    
    fclose(fp);
    fclose(fOut);
    return 0;
}
