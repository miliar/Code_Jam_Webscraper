#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int casenum = 0;

    FILE * resultfile = fopen( "A-large.out","w" );
    if( !resultfile )
        return 0;

    FILE* stream = fopen("A-large.in", "rb" );
    if( stream )
    {
        char line[1024] = {0};
        fgets(line, 1024, stream );
        while( fgets( line, 1024, stream ) )
        {
            int time = 0;
            casenum ++;

            char* p = strtok( line, " " );
            int step = atoi(p);

            int robtype[110] = {0};
            int A[110] = {0};
            int B[110] = {0};

            int i = 0;
            int ai = 0, bi = 0;
            while( p = strtok( NULL, " ") )
            {
                if( !strcmp( p, "O" ) )
                    robtype[i++] = 1;
                else if( !strcmp( p, "B" ) )
                    robtype[i++] = 2;
                else
                {
                    if( robtype[i-1] == 1 )
                        A[ai++] = atoi(p);
                    if( robtype[i-1] == 2 )
                        B[bi++] = atoi(p);
                }
            }

            i = 0;
            ai = 0;
            bi = 0;
            int AL = 1; 
            int BL = 1;
            int bpress = 0;
            while( i < step )
            {
                time++;
                bpress = 0;
                if( A[ai] != 0 )
                {
                    if( AL < A[ai] )
                        AL++;
                    else if( AL > A[ai] )
                        AL--;
                    else
                    {
                        if( robtype[i] == 1 && !bpress)
                        {
                            i++;
                            ai++;
                            bpress = 1;
                        }
                    }
                }

                if( B[bi] != 0 )
                {
                    if( BL < B[bi] )
                        BL++;
                    else if( BL > B[bi] )
                        BL--;
                    else
                    {
                        if( robtype[i] == 2 && !bpress )
                        {
                            i++;
                            bi++;
                        }
                    }
                }
            }
            fprintf( resultfile, "Case #%d: %d\n", casenum, time );
        }
        fclose(stream);
    }

    if( resultfile )
        fclose( resultfile );
    return 0;
}