/*
 * Main.cpp
 *
 *   〃∩ ∧__∧
 *   ⊂⌒( ・ω･）ok ok, it's amusing, ya amusing.
 *     `ヽっ⌒/⌒ｃ
 *          ⌒ ⌒
 */

#define EXECUTE_TYPE 2

#define COMMIT_ALPHABET 'A'
#define COMMIT_ATTEMPT 0


#include <stdio.h>
#include <wchar.h>
#include <locale.h>
#include <deque>
#include <vector>
#include <string>
#include <algorithm>

typedef signed char  s8;
typedef signed short s16;
typedef signed long  s32;
typedef signed long long s64;
typedef unsigned char  u8;
typedef unsigned short u16;
typedef unsigned long  u32;
typedef unsigned long long u64;
typedef unsigned char  bit8;
typedef unsigned short bit16;
typedef unsigned long  bit32;
typedef unsigned long long bit64;

#if (EXECUTE_TYPE == 0) || (EXECUTE_TYPE > 2)
#define prin(...) printf(__VA_ARGS__)
#define _DBG
#else
#define prin(...) (void)0
#endif

#define PRINTF prin

#if (EXECUTE_TYPE == 0)
#define INPUT_FILE_NAME "./input.txt"
#elif (EXECUTE_TYPE == 1) || (EXECUTE_TYPE == 3)
#define INPUT_FILE_NAME "C:\\Temp\\%c-small-attempt%d.in"
#else
#define INPUT_FILE_NAME "C:\\Temp\\%c-large.in"
#endif
#define OUTPUT_FILE_NAME "./output%c%d.txt"

void setup();
inline void runCase();

FILE *pFileIn;
FILE *pFileOut;

int OpenFile()
{
    char fileName[128];
#if (EXECUTE_TYPE == 0)
    strcpy(fileName, INPUT_FILE_NAME);
#elif (EXECUTE_TYPE == 1) || (EXECUTE_TYPE == 3)
    sprintf(fileName, INPUT_FILE_NAME, COMMIT_ALPHABET, COMMIT_ATTEMPT);
#else
    sprintf(fileName, INPUT_FILE_NAME, COMMIT_ALPHABET);
#endif

    pFileIn = fopen(fileName, "r");
    if (!pFileIn)
    {
        printf("%16s:%4d input file \"%s\" not found\n", __FILE__, __LINE__, fileName);
        return 1;
    }

    sprintf(fileName, OUTPUT_FILE_NAME, COMMIT_ALPHABET, COMMIT_ATTEMPT);

    pFileOut = fopen(fileName, "w");
    if (!pFileOut)
    {
        printf("%16s:%4d output file \"%s\" not found\n", __FILE__, __LINE__, fileName);
        return 1;
    }
    return 0;
}

int main(int argc, char *argv[])
{
    if (OpenFile())
    {
        return 1;
    }

    u64 caseNumberMax;
    fscanf(pFileIn, "%lld\n", &caseNumberMax);

    setup();

    for (u32 caseNumber = 0; caseNumber < caseNumberMax; caseNumber++)
    {
#ifndef _DBG
        fprintf(pFileOut, "Case #%ld: ", caseNumber + 1);
#endif
        prin("Case #%ld: ", caseNumber + 1);
        runCase();
    }

    _fcloseall();

    return 0;
}

//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////
//                    ここまでテンプレ                      //
//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////

u8 pic[52][52];
char out[52][52];


const char *OUTPUT_STRING[] =
{
        "Impossible",
};


void setup()
{
}

void runCase()
{
    s32 h;
    s32 w;
    fscanf(pFileIn, "%ld%ld", &h, &w);

    for (int i = 0; i < h; i++)
    {
        char buf[52];
        fscanf(pFileIn, "%s", &buf);
        for (int j = 0; j < w; j++)
        {
            pic[i][j] = (buf[j] == '.') ? 0 : 1;
        }
    }

    bool ok = true;
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            if (pic[i][j] == 1)
            {
                if (i == h-1)
                    ok = false;
                else if (j == w-1)
                    ok = false;
                else if (pic[i+1][j+0] != 1 ||
                        pic[i+0][j+1] != 1 ||
                        pic[i+1][j+1] != 1)
                    ok = false;
                else
                {

                    pic[i+0][j+0] = 255;
                    pic[i+1][j+0] = 255;
                    pic[i+0][j+1] = 255;
                    pic[i+1][j+1] = 255;

                    out[i+0][j+0] = '/';
                    out[i+1][j+0] = '\\';
                    out[i+0][j+1] = '\\';
                    out[i+1][j+1] = '/';
                }
            }
            else if (pic[i][j] == 255)
               ;
            else
                out[i][j] = '.';

        }
    }

    fprintf(pFileOut, "\n");
    if (!ok)
        fprintf(pFileOut, "%s\n", OUTPUT_STRING[0]);
    else
    {
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                fprintf(pFileOut, "%c", out[i][j]);
            }
            fprintf(pFileOut, "\n");
        }
    }
}












































