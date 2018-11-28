/* 
 * main.cpp
 *
 *  Created on: 2010. 5. 9.
 *      Author: programmeryh
 */
#include <stdio.h>
#include <stdlib.h>

int canride[60];

int canrun[60];

int team[60][1010];

int nteam[60];

int main()
{
    FILE *fd_in;

    FILE *fd_out;

    int tcase;
    int p_avl;
    int cash;
    int ptr;
    int rteam;

    int i, j;

    fd_in = fopen("input.txt", "r");
    fd_out = fopen("output.txt", "w");

    fscanf(fd_in, "%d", &tcase);

    for (i = 0; i < tcase; i++)
    {
        fscanf(fd_in, "%d", &canrun[i]);
        fscanf(fd_in, "%d", &canride[i]);
        fscanf(fd_in, "%d", &nteam[i]);

        for (j = 0; j < nteam[i]; j++)
        {
            fscanf(fd_in, "%d", &team[i][j]);
        }
    }

    for (i = 0; i < tcase; i++)
    {
    	cash = 0;
    	ptr = 0;
        for(j = 0; j < canrun[i]; j++)
        {
        	p_avl = canride[i];

        	rteam = 0;
        	while(p_avl >= team[i][ptr] && rteam < nteam[i])
        	{
				p_avl -= team[i][ptr];
				cash += team[i][ptr];
				rteam ++;
				if(ptr == nteam[i]-1) ptr = -1;
				ptr++;
        	}
        }
        fprintf(fd_out, "Case #%d: %d\n", i+1, cash);
    }

    fclose(fd_in);
    fclose(fd_out);
    return 0;
}
