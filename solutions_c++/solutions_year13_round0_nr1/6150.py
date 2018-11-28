#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <math.h>

//#include <inttypes.h>

#if 0
using namespace std;
#endif


#define SUCCESS 1
#define FAILURE 0


#define __LF__  0x000a
#define __SPACE__ 0x0020

#define __SPACE_CHAR__  ' '
#define __NULL_TERMINATOR__ '\0'


#define GET_INT_VAL_OF_CHAR(__c)  ((__c) - 0x30)

#define IS_LF(__c)    ((__c) == __LF__)


#define Max_Int_Val()   pow(2, (sizeof(int) << 3)) - 1;
#define Min_Int_Val()   0 - pow(2, (sizeof(int) << 3));


#define swap(x, y)      \
    (x) = (x) + (y);    \
    (y) = (x) - (y);    \
    (x) = (x) - (y);


#define write_Int_To_OutputFile(outputFilePtr, caseId, value)       \
    fprintf (outputFilePtr, "Case #%d: %d\n", (caseId), (value));

#define write_Int64_To_OutputFile(outputFilePtr, caseId, value)       \
    fprintf (outputFilePtr, "Case #%d: %I64d\n", (caseId), (value));

#define write_Str_To_OutputFile(outputFilePtr, caseId, str)       \
    fprintf (outputFilePtr, "Case #%d: %s\n", (caseId), (str));

#define write_Intss_To_OutputFile(outputFilePtr, caseId, value1, value2)  \
    fprintf (outputFilePtr, "Case #%d: %d %d\n", (caseId), (value1), (value2));




/*********************************************************************/
/********************** GENERAL USE CODE STARTS **********************/
/*********************************************************************/

/***** Func Declarations *****/
int movePtrToSpace(char ** __p__);

void toNextLine(char ** stream);

int readIntValue(char ** stream);

int getLineAsStr(char * stream, char * str, int size);

int getLineAsIntArray(char * stream, int * str, int size);



/***** Func Definitions *****/

/* moves the pointer to the immediate next space character
 * if no space is found then FAILURE is returned
 * else SUCCESS is returned. */
int
movePtrToSpace(char ** __p__)
{
    int ret = SUCCESS;

    while( **(__p__) != __SPACE_CHAR__)
    {
        if( **(__p__) == __NULL_TERMINATOR__ )
        {
            ret = FAILURE;
            break;
        }
        (*__p__)++;
    }

    return ret;
}


/* moves the stream to the next line. */
/* I think it is NEW LINE PLATFORM INDEPENDENT */
void
toNextLine(char ** stream)
{
    while( ! IS_LF(**stream) )
        (*stream)++;
    (*stream)++;
}


/* for reading and returning the integer value from the stream. */
/* I think it is NEW LINE PLATFORM INDEPENDENT */
int
readIntValue(char ** stream)
{
    int intVal = 0, negative = 0;

#if 1
    while( (**stream == ' ') )
    {
        (*stream)++;
    }/* end while */

    while( ((**stream >= '0') && (**stream <= '9')) || 
            (**stream == '-') )
    {
        if(**stream == '-')
        {
            negative = 1;
        }
        else
        {
            intVal = intVal*10 + GET_INT_VAL_OF_CHAR(**stream);
        }/* end else if */

        (*stream)++;
    }/* end while */

    if(negative)
        intVal = 0 - intVal;
#else
    intVal = atoi(stream);
#endif

    return intVal;
}/* end readIntValue */



/* copy the current line (from where stream is pointing) into the memory provided
 * If the space provided is not enough then FAILURE is returned 
 * else SUCCESS is returned. */
int
getLineAsStr(char * stream, char * str, int size)
{
    int ret = SUCCESS;
    int i = 0;

    while( ! IS_LF(*stream) )
    {
        if(size <= 0)
        {
            ret = FAILURE;
            break;
        }

        str[i++] = *stream++;
        size--;
    }

    return ret;
}


/* get the integer values in the current line into the array
 * If the space provided is not enough then FAILURE is returned 
 * else SUCCESS is returned. */
int
getLineAsIntArray(char * stream, int * arr, int size)
{
    int ret = SUCCESS;
    int i = 0;

    while( ! IS_LF(*stream) )
    {
        if(size <= 0)
        {
            ret = FAILURE;
            break;
        }

        arr[i++] = readIntValue(&stream);
        size--;
    }

    return ret;
}

/*******************************************************************/
/********************** GENERAL USE CODE ENDS **********************/
/*******************************************************************/


void reverseWords(char * str, int size);


/* MAIN METHOD */
int
main()
{
    FILE * filePtr = NULL;
    FILE * outputFilePtr = fopen("output.txt", "wb");
    filePtr = fopen("A-large.in", "rb");

    
    if(filePtr)
    {
        int fileSize = 0;

        fseek(filePtr, 0, SEEK_END);
        fileSize = ftell(filePtr);
        fseek(filePtr, 0, SEEK_SET);

        if(fileSize)
        {
            char * fileBuf_ori = (char*) malloc(sizeof(char) * fileSize);
            char * fileBuf = fileBuf_ori;

            if(fileBuf)
            {
                /* General values */
                int numTestCases = 0, iCases = 0;
                fread(fileBuf, sizeof(char), fileSize, filePtr);

                /* NOW get the values of ... 
                 * number of test-cases, 
                 * etc. */
                /* 1st value is - number of test-cases */
                numTestCases = readIntValue(&fileBuf);      toNextLine(&fileBuf);


/*******************************************************************/
/********************** GENERAL USE CODE ENDS **********************/
/*******************************************************************/


                /* FOR THIS PROBLEM */
#define __num_vals__ 2001
                char board[4][4];
                int valHash[__num_vals__];
                int val[__num_vals__];

                int xWon = 0;
                int oWon = 0;
                int draw = 0;

                for( ; iCases < numTestCases; iCases++)
                {
                    /* SPECIFIC VALUES / CODE */

                    int i, j;
                    int prev = 0;

                    /* for each case we have 4 lines */
                    for(i = 0; i < 4; i++)
                    {
                        getLineAsStr(fileBuf, board[i], 4);
                        toNextLine(&fileBuf);
                    }

                    /* i have the board now */

                    /* check if player X has won */
                    for(i = 0; i < 4; i++)
                    {
                        xWon = 1;
                        for(j = 0; j < 4; j++)
                        {
                            if(board[i][j] != 'X' && board[i][j] != 'T')
                            {
                                xWon = 0;
                                break;
                            }
                        }

                        if(xWon == 1)
                            goto PLAYER_WON;
                    }
                    for(j = 0; j < 4; j++)
                    {
                        xWon = 1;
                        for(i = 0; i < 4; i++)
                        {
                            if(board[i][j] != 'X' && board[i][j] != 'T')
                            {
                                xWon = 0;
                                break;
                            }
                        }

                        if(xWon == 1)
                            goto PLAYER_WON;
                    }
                    for(i = 0; i < 4; i++)
                    {
                        xWon = 1;
                        if(board[i][i] != 'X' && board[i][i] != 'T')
                        {
                            xWon = 0;
                            break;
                        }
                    }
                    if(xWon == 1)
                        goto PLAYER_WON;
                    for(i = 0; i < 4; i++)
                    {
                        xWon = 1;
                        if(board[i][3-i] != 'X' && board[i][3-i] != 'T')
                        {
                            xWon = 0;
                            break;
                        }
                    }
                    if(xWon == 1)
                        goto PLAYER_WON;


                    /* check if player O has won */
                    for(i = 0; i < 4; i++)
                    {
                        oWon = 1;
                        for(j = 0; j < 4; j++)
                        {
                            if(board[i][j] != 'O' && board[i][j] != 'T')
                            {
                                oWon = 0;
                                break;
                            }
                        }

                        if(oWon == 1)
                            goto PLAYER_WON;
                    }
                    for(j = 0; j < 4; j++)
                    {
                        oWon = 1;
                        for(i = 0; i < 4; i++)
                        {
                            if(board[i][j] != 'O' && board[i][j] != 'T')
                            {
                                oWon = 0;
                                break;
                            }
                        }

                        if(oWon == 1)
                            goto PLAYER_WON;
                    }
                    for(i = 0; i < 4; i++)
                    {
                        oWon = 1;
                        if(board[i][i] != 'O' && board[i][i] != 'T')
                        {
                            oWon = 0;
                            break;
                        }
                    }
                    if(oWon == 1)
                        goto PLAYER_WON;
                    for(i = 0; i < 4; i++)
                    {
                        oWon = 1;
                        if(board[i][3-i] != 'O' && board[i][3-i] != 'T')
                        {
                            oWon = 0;
                            break;
                        }
                    }
                    if(oWon == 1)
                        goto PLAYER_WON;


PLAYER_WON:
                    if(xWon == 1)
                    {
                        /* print X Won */
                        write_Str_To_OutputFile(outputFilePtr, iCases+1, "X won");
                    }
                    else if(oWon == 1)
                    {
                        /* print O Won */
                        write_Str_To_OutputFile(outputFilePtr, iCases+1, "O won");
                    }
                    else
                    {
                        /* check for a draw */
                        draw = 1;
                        for(i = 0; i < 4; i++)
                        {
                            for(j = 0; j < 4; j++)
                            {
                                if(board[i][j] == '.')
                                {
                                    draw = 0;
                                    goto IS_DRAW;
                                }
                            }
                        }

IS_DRAW:
                        if(draw == 0)
                        {
                            write_Str_To_OutputFile(outputFilePtr, iCases+1, "Game has not completed");
                        }
                        else
                        {
                            write_Str_To_OutputFile(outputFilePtr, iCases+1, "Draw");
                        }
                    }

                    /* empty line between test-cases */
                    toNextLine(&fileBuf);
                }/* end for */

                free(fileBuf_ori);
            }/* end if */
        }/* end if */
    }/* end if */

    fclose(outputFilePtr);

    return 0;
}/* end main */

