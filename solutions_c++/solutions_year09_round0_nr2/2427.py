#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

// drainage direction in case of tie: NWES
#define BUFSZ 10000


typedef struct cell
{
    int elev;
    int basin;
#if 0
    int sinkdir;
#endif
    void *point;
} celltype;

void setsinkdir(celltype *cellp,
                celltype *ncellp,
                celltype *wcellp,
                celltype *ecellp,
                celltype *scellp)
{
    int lowest = cellp->elev;

//    printf("%d -- %d %d %d %d ---> ", lowest, ncellp->elev, wcellp->elev,
//           ecellp->elev, scellp->elev);
    if (ncellp->elev < lowest)
    {
//        printf("North\n");
        cellp->point = (void *)ncellp;
        lowest = ncellp->elev;
    }

    if (wcellp->elev < lowest)
    {
//        printf("West\n");
        cellp->point = (void *)wcellp;
        lowest = wcellp->elev;
    }

    if (ecellp->elev < lowest)
    {
//        printf("East\n");
        cellp->point = (void *)ecellp;
        lowest = ecellp->elev;
    }

    if (scellp->elev < lowest)
    {
//        printf("South\n");
        cellp->point = (void *)scellp;
        lowest = scellp->elev;
    }

    if (lowest == cellp->elev)
    {
//        printf("Null\n");
        cellp->point = NULL; // sink
    }
}

int traverse(void *point, int *current)
{
    celltype &cell = *((celltype *)point);

    if (cell.basin == 0)
    {
        if (!cell.point)
        {
            cell.basin = *current;
            (*current)++;
        }
        else
        {
            cell.basin = traverse(cell.point, current);
        }
    }
    return cell.basin;

#if 0
    switch (cell.sinkdir)
    {
        case 0:  // unlabelled sink - label it now
            cell.basin = *current;
            (*current)++;
            return cell.basin;
            break;
        case 1:
#endif


}

int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T, H, W;
    int i, r, c;

    if (argc != 2)
    {
        exit(-1);
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("Usage: file is no good\n");
        exit(-1);
    }


    fgets(strBuf, BUFSZ, fp);
    token = strtok_r(strBuf, "\r\n", &sptr1);
    T = atoi(token);

    for (i=0; i<T; i++)
    {
        int current = 1;
        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);
        subtoken = strtok_r(token, " ", &sptr2);
        H = atoi(subtoken);
        subtoken = strtok_r(NULL, " ", &sptr2);
        W = atoi(subtoken);

        celltype cells[100][100];

        for (r=0; r<H; r++)
        {
            fgets(strBuf, BUFSZ, fp);
            token = strtok_r(strBuf, "\r\n", &sptr1);

            for (c=0; c<W; c++)
            {
                if (c==0)
                {
                    subtoken = strtok_r(token, " ", &sptr2);
                }
                else
                {
                    subtoken = strtok_r(NULL, " ", &sptr2);
                }
                cells[r][c].elev = atoi(subtoken);
                cells[r][c].basin = 0;
            }
        }

        // set sinks and directions
        for (r=0; r<H; r++)
        {
            for (c=0; c<W; c++)
            {
#if 0
                // set elevations
                n_elev = (r == 0) ? 10000 : cells[r-1][c].elev;
                w_elev = (c == 0) ? 10000 : cells[r][c-1].elev;
                e_elev = (c == W-1) ? 10000 : cells[r][c+1].elev;
                s_elev = (r == H-1) ? 10000 : cells[r+1][c].elev;

                cells[r][c].sinkdir =
                    getsinkdir(cells[r][c].elev, n_elev, w_elev, e_elev,
                               s_elev);
#endif

                setsinkdir(&(cells[r][c]),
                           (r == 0) ? &(cells[r][c]) : &(cells[r-1][c]),
                           (c == 0) ? &(cells[r][c]) : &(cells[r][c-1]),
                           (c == W-1) ? &(cells[r][c]) : &(cells[r][c+1]),
                           (r == H-1) ? &(cells[r][c]) : &(cells[r+1][c]));
            }
        }

        // label coordinates
        for (r=0; r<H; r++)
        {
            for (c=0; c<W; c++)
            {
                celltype &cell = cells[r][c];

//                printf("current = %d\n", current);
                cell.basin = traverse((void *)&cell, &current);
//                printf("current = %d %d\n", current, cell.basin);
#if 0
                // current cell has no basin label
                if (cell.basin == '\0')
                {
                    if (!cell.point) // sink
                    {
                        cell.basin = current;
                        current++;
                    }
                    else
                    {
                        cell.basin = traverse(cell.point, &current);
                    }
                }
#endif
            }
        }


#if 0
                    switch (cells[r][c].sinkdir)
                    {
                        case 0: // label the sink with new letter
                            cells[r][c].basin = current;
                            current++;
                            break;
                        case 1:
                            cells[r][c].basin = cells[r-1][c].basin;
                            break;
                        case 2:
                            cells[r][c].basin = cells[r][c-1].basin;
                            break;
                        case 3:
                            cells[r][c].basin = traverseE(cells[r][c+1], &current);
                            break;
                        case 4:
                            cells[r][c].basin = traverseS(cells[r+1][c], &current);
                            break;
                    }
#endif



        printf("Case #%d:\n", i+1);
        for (r=0; r<H; r++)
        {
            for (c=0; c<W; c++)
            {
                printf("%c", 'a' + (cells[r][c].basin -1));
                if (c==W-1)
                {
                    printf("\n");
                }
                else
                {
                    printf(" ");
                }
            }
        }
    }


    fclose(fp);
    return 0;
}
