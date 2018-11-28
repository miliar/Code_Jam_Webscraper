/**
 * ===========================================================================
 *
 *          @file  game.cpp
 *         @brief  
 *
 *        @author  dengos (w), dengos.w@gmail.com, scut
 *       @version  1.0
 *          @date  04/13/2013 07:10:01 AM
 *
 * ===========================================================================
 */



#include <cstdio>
#include <cstdlib>
#include <cstring>



/**
 * @brief
 *
 * @param argc
 * @param argv[]
 *
 * @return 0 if ok.
 */
    int
main ( int argc, char *argv[] )
{
    int T;
    int i, j, k, cnt, space;
    int state = 0;
    char c;
    const char *msg = NULL;
    int PX[12];
    int PO[12];
    int ASS[20][3];
   
    memset(ASS, 0, sizeof ASS);
    for ( i = 1; i <= 4; ++i ) 
    {
        for ( j = 1; j <= 4; ++j ) 
        {
            k = (i-1) * 4 + j;
            ASS[k][0] = i;
            ASS[k][1] = 4 + j;
            if (i == j)     ASS[k][2] = 9;
            if (i + j == 5) ASS[k][2] = 10;
        }
    }

    scanf ( "%d", &T );
    for ( i = 1; i <= T; ++i ) 
    {
        cnt = 0;
        space = 0;
        memset(PX, 0, sizeof PX);
        memset(PO, 0, sizeof PO);
        while (cnt < 16)
        {
            c = (char)getchar();
            switch ( c ) 
            {
                case 'X':	
                    ++cnt;
                    ++PX[ASS[cnt][0]];
                    ++PX[ASS[cnt][1]];
                    ++PX[ASS[cnt][2]];
                    break;

                case 'O':
                    ++cnt;
                    ++PO[ASS[cnt][0]];
                    ++PO[ASS[cnt][1]];
                    ++PO[ASS[cnt][2]];
                    break;

                case 'T':
                    ++cnt;
                    ++PX[ASS[cnt][0]];
                    ++PX[ASS[cnt][1]];
                    ++PX[ASS[cnt][2]];
                    ++PO[ASS[cnt][0]];
                    ++PO[ASS[cnt][1]];
                    ++PO[ASS[cnt][2]];
                    break;
                
                case '.':
                    ++cnt;
                    ++space;
                    break;

                default:	
                    break;
            }				/* -----  end switch  ----- */
        }

        state = 0;
        for ( j = 1; j <= 10; ++j ) 
        {
            if (PX[j] == 4) 
            {
                state = 1;
                break;
            }
            if (PO[j] == 4)
            {
                state = 2;
                break;
            }
        }
        
        if (state)
        {
            msg = state == 1 ? "X won" : "O won";
        }
        else
        {
            msg = space ? "Game has not completed": "Draw";
        }
        printf ( "Case #%d: %s\n", i, msg );
    }

    return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */








