/*
 * Main.cpp
 *
 *   〃∩ ∧__∧
 *   ⊂⌒( ・ω･）ok ok, it's amusing, ya amusing.
 *     `ヽっ⌒/⌒ｃ
 *          ⌒ ⌒
 */

#define EXECUTE_TYPE 1

#define COMMIT_ALPHABET 'C'
#define COMMIT_ATTEMPT 5


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


s32 N;
s64 F[10000];
s64 L;
s64 H;

const char *OUTPUT_STRING[] =
{
        "NO",
};


void setup()
{
}

void runCase()
{
    fscanf(pFileIn, "%ld", &N);
    fscanf(pFileIn, "%lld", &L);
    fscanf(pFileIn, "%lld", &H);
    for (int i = 0; i < N; i++)
    {
        fscanf(pFileIn, "%lld", &F[i]);
    }

    s64 note = 0;
    for (s64 i = L; i <= H; i++)
    {
        bool ok = true;
        for (s64 j = 0; j < N; j++)
        {
            if (!(F[j] % i == 0 || i % F[j] == 0))
            {
                ok = false;
                break;
            }
        }
        if (ok)
        {
            note = i;
            break;
        }
    }

    if (note == 0)
        fprintf(pFileOut, "%s\n", OUTPUT_STRING[0]);
    else
        fprintf(pFileOut, "%lld\n", note);
}












































