/* 
 * main.cpp
 *
 *  Created on: 2010. 5. 9.
 *      Author: programmeryh
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int tcase;

int data[10010][2];

int main(int argc, char **argv)
{
    int i;
//    bool tmp[40] = { 0, };

    FILE *fd_in;
    FILE *fd_out;

    fd_in = fopen("input.txt", "r");
    fd_out = fopen("output.txt", "w");

    fscanf(fd_in, "%d", &tcase);

    for (i = 0; i < tcase; i++)
    {
        fscanf(fd_in, "%d", &data[i][0]);       // Value of N
        fscanf(fd_in, "%d", &data[i][1]);       // Value of K
    }

    for (i = 0; i < tcase; i++)
    {
        if(((data[i][1] + 1) % (int)pow((double)2, (double)data[i][0])) == 0)
        {
        	fprintf(fd_out, "Case #%d: ON\n", i+1);
        }
        else
        {
        	fprintf(fd_out, "Case #%d: OFF\n", i+1);
        }
    }

    fclose(fd_in);
    fclose(fd_out);
    return 0;
}
