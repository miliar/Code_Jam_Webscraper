#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>

#define zduration 1000
#define hitcharge 750
#define mstep 100

void checkwin(char board[4][4], bool &done, bool &draw, char &winner) 
{
    int ocountlist[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        xcountlist[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    bool spacea = false;

    for (int i=0; i<4; ++i)
    {
        for (int j=0; j<4; ++j) 
        {
            char c = board[i][j];
            bool wild = 'T'==c ;
            bool opath = 'O'==c || wild,
                 xpath = 'X'==c || wild;

            if ('.'==c ) 
                spacea = true;

            if ( opath )
            {
                ocountlist[i]++;
                ocountlist[j+4]++;
                if (i==j)
                    ocountlist[8]++;
                if (3==i+j)
                    ocountlist[9]++;
            }
            if ( xpath )
            {
                xcountlist[i]++;
                xcountlist[j+4]++;
                if (i==j)
                    xcountlist[8]++;
                if (3==i+j)
                    xcountlist[9]++;
            }
        } 
    }

    int omax = 0 , xmax = 0; 
    for (int i=0; i<10; ++i) 
    {
        omax = std::max(ocountlist[i], omax);
        xmax = std::max(xcountlist[i], xmax);
    } 
    printf("omax: %d xmax: %d \n", omax, xmax);

    if (4 == xmax)
    {
        draw = false;
        done = true;
        winner='X';
    }
    else if (4 == omax)
    {
        draw = false;
        done = true;
        winner='O';
    }
    else if (spacea)
    {
        draw = false;
        done = false;
    }
    else
    {
        draw = true;
        done = true;
    }
}

int main(int argc, char** argv) {
    if (argc<3) {
        printf("not enough parameters: %d\n", argc);
        return 0;
    }
    FILE *fp;
    printf("%s\n", argv[1]);

    if ( (fp = fopen( (const char*) argv[1], "r" )) == NULL ) {
        printf("Open Input File ERROR!\n"); 
        return 0;
    }

    std::ofstream ofs(argv[2]);

    int ncases;
    fscanf(fp, "%d\n", &ncases);

    printf("#Cases: %d\n", ncases);
    if (ncases<=0) return -1;

    char board[4][4];
    char winner;
    bool draw, done;

    for (int i=0; i<ncases; ++i) 
    {

        for (int j=0; j<4; ++j) 
        {
            fscanf(fp, "%c%c%c%c\n", &board[j][0], &board[j][1], &board[j][2], &board[j][3] );
        }
        fscanf(fp, "\n");

        for (int j=0; j<4; ++j) 
        {
            printf("%c%c%c%c\n", board[j][0], board[j][1], board[j][2], board[j][3] );
        }


        checkwin(board, done, draw, winner) ;
        std::cout<<"Case #"<<i+1<<": ";
        ofs<<"Case #"<<i+1<<": ";
        if ( done )
        {
            draw ? std::cout<<"Draw\n" : std::cout<<winner<<" won\n";
            draw ? ofs<<"Draw\n" : ofs<<winner<<" won\n";
        }
        else
        {
            std::cout<<"Game has not completed\n";
            ofs<<"Game has not completed\n";
        }
    }


    ofs.close();

    fclose(fp);
}

