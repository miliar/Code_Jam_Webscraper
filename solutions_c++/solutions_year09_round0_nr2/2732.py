#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define CENTER 0
#define NORTH 1
#define WEST 2
#define EAST 3
#define SOUTH 4

int main()
{
    int **map = NULL; // map for "input"
    char **regen_map = NULL; // map for "output"
    
    int regCount = 0; // region in number
    char region = 'a'; // region in char
    char revise = 0,reviseto = 0;
    int alphabet[26] = {0};
    
    int T = 0; // number of maps
    int H = 0, W = 0; // height and width
    int mindir = CENTER; // record min value
    int minval = 10000;

    int t = 0; // counter for maps
    int i, j, m, n, a; // counter for array
    int empty = 0;
    int north = 10000, west = 10000, east = 10000, south = 10000; // neighbor value

    FILE *fPtrin, *fPtrout;

    if( ( fPtrout = fopen( "B-small-attempt2.out", "w" ) ) == NULL )
    {
		printf("File could not be poene!\n");
		system("pause");
		exit(0);
    }
    if( ( fPtrin = fopen( "B-small-attempt2.in", "r" ) ) == NULL )
    {
        printf("File could not be poene!\n");
		system("pause");
		exit(0);
    }

    fscanf(fPtrin, "%d", &T);

    while( fscanf(fPtrin, "%d%d", &H, &W) != EOF )
    {
        t++;
        /* Initialization for arrays and variables */
        region = 'a';
        map = new int *[H];
        regen_map = new char *[H];
        for( i = 0; i < H; i++ ) {
            map[i] = new int [W];
            regen_map[i] = new char [W];
            for( j = 0; j < W; j++ )
            {
                map[i][j] = '\0';
                regen_map[i][j] = -1;
            }
        }

        for( m = 0; m < H; m++ )
            for( n = 0; n < W; n++ )
                fscanf( fPtrin, "%d", &map[m][n]);
        
        for( i = 0; i < H; i++ )
        {
            for( j = 0; j < W; j++ )
            {
                //printf("%d ", map[i][j]);
                if( i == 0 && j == 0 )
                {
                    regen_map[i][j] = region;
                    alphabet[region-'a'] = 1;
                }
                mindir = CENTER;
                minval = map[i][j];
                /* check the min value of neighbor */
                if( i > 0 )
                {
                    north = map[i-1][j];
                    if( north < minval )
                    {
                        mindir = NORTH;
                        minval = north;
                    }
                }
                if( j > 0 )
                {
                    west = map[i][j-1];
                    if( west < minval )
                    {
                        mindir = WEST;
                        minval = west;
                    }
                }
                if( j < W-1 )
                {
                    east = map[i][j+1];
                    if( east < minval )
                    {
                        mindir = EAST;
                        minval = east;
                    }
                }
                if( i < H-1 )
                {
                    south = map[i+1][j];
                    if( south < minval )
                    {
                        mindir = SOUTH;
                        minval = south;
                    }
                }

                if( mindir == CENTER ) {
                    if( regen_map[i][j] == -1 )
                    {
                        regen_map[i][j] = ++region;
                        alphabet[region-'a'] = 1;
                    }
                }else if( mindir == NORTH ) {
                    if( regen_map[i][j] != -1 )
                    {
                        revise = regen_map[i][j];
                        reviseto = regen_map[i-1][j];
                        alphabet[revise-'a'] = 0;
                    }
                    regen_map[i][j] = regen_map[i-1][j];
                }else if( mindir == WEST ) {
                    if( regen_map[i][j-1] != -1 && regen_map[i][j] != -1 )
                    {
                        if( regen_map[i][j] < regen_map[i][j-1])
                        {
                            revise = regen_map[i][j-1];
                            reviseto = regen_map[i][j];
                            alphabet[revise-'a'] = 0;
                        }else
                        {
                            revise = regen_map[i][j];
                            reviseto = regen_map[i][j-1];
                            alphabet[revise-'a'] = 0;
                        }
                    }
                    else
                        regen_map[i][j] = regen_map[i][j-1];
                }else if( mindir == EAST ) {
                    if( regen_map[i][j+1] != -1 && regen_map[i][j] != -1 )
                    {
                        if( regen_map[i][j] < regen_map[i][j+1])
                        {
                            revise = regen_map[i][j+1];
                            reviseto = regen_map[i][j];
                            alphabet[revise-'a'] = 0;
                        }else
                        {
                            revise = regen_map[i][j];
                            reviseto = regen_map[i][j+1];
                            alphabet[revise-'a'] = 0;
                        }
                    }
                    else if( regen_map[i][j+1] != -1 )
                        regen_map[i][j] = regen_map[i][j+1];
                    else if( regen_map[i][j] != -1 )
                        regen_map[i][j+1] = regen_map[i][j];
                    else {
                        regen_map[i][j] = ++region;
                        regen_map[i][j+1] = region;
                        alphabet[region-'a'] = 1;
                    }
                }else if( mindir == SOUTH ) {
                    if( regen_map[i][j] != -1 ) {
                        regen_map[i+1][j] = regen_map[i][j];
                    }else {
                        regen_map[i][j] = ++region;
                        regen_map[i+1][j] = region;
                        alphabet[region-'a'] = 1;
                    }
                }
                if( revise )
                {
                    for( m = 0; m < H; m++ )
                    {
                        for( n = 0; n < W; n++ )
                        {
                            if( regen_map[m][n] == revise )
                                regen_map[m][n] = reviseto;
                            else if( regen_map[m][n] > revise )
                                regen_map[m][n]--;
                        }
                    }
                    region--;
                }
                revise = 0;
                reviseto = 0;
            }
        }

        fprintf(fPtrout, "Case #%d:\n", t);
        for( i = 0; i < H; i++ )
        {
            for( j = 0; j < W; j++ )
            {
                if( j != W-1 )
                    fprintf(fPtrout, "%c ", regen_map[i][j] );
                else
                    fprintf(fPtrout, "%c\n", regen_map[i][j] );
            }
        }
         north = south = west = east = 10000;
        region = 'a';
        /* free the array mamory */
        free(map);
        free(regen_map);
    }
    fclose(fPtrin);
    fclose(fPtrout);
    system("pause");
    return 0;
}

