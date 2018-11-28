/*
 * Main.cpp
 *
 *   〃∩ ∧__∧
 *   ⊂⌒( ・ω･）ok ok, it's amusing, ya amusing.
 *     `ヽっ⌒/⌒ｃ
 *          ⌒ ⌒
 */

#define EXECUTE_TYPE 2


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
#define prin(...) fprintf(pFileOut, __VA_ARGS__)
#define _DBG
#else
#define prin(...) (void)0
#endif

#define PRINTF prin

#if (EXECUTE_TYPE == 0)
const char INPUT_FILE_NAME[] = "./input.txt";
#elif (EXECUTE_TYPE == 1) || (EXECUTE_TYPE == 3)
const char INPUT_FILE_NAME[]  = "C:\\Temp\\A-small-attempt0.in";
#else
const char INPUT_FILE_NAME[]  = "C:\\Temp\\A-large.in";
#endif
const char OUTPUT_FILE_NAME[] = "./output.txt";

void setup();
inline void runCase(FILE *pFileOut, FILE *pFileIn, u32 caseNumber);

FILE *pFileOut;

int main(int argc, char *argv[])
{
    FILE *pFileIn = fopen(INPUT_FILE_NAME, "r");
    if (!pFileIn)
    {
        prin("%16s:%4d input file \"%s\" not found\n", __FILE__, __LINE__, INPUT_FILE_NAME);
        return 1;
    }

    pFileOut = fopen(OUTPUT_FILE_NAME, "w");
    if (!pFileOut)
    {
        prin("%16s:%4d output file \"%s\" not found\n", __FILE__, __LINE__, OUTPUT_FILE_NAME);
        return 1;
    }

    u64 caseNumberMax;
    fscanf(pFileIn, "%lld\n", &caseNumberMax);

    setup();

    for (u32 caseNumber = 0; caseNumber < caseNumberMax; caseNumber++)
    {
        runCase(pFileOut, pFileIn, caseNumber);
    }

    _fcloseall();

    return 0;
}

//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////
//                    ここまでテンプレ                      //
//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////



s32 t;
s32 win[100][100];
double score[100];

void setup()
{
}

void runCase(FILE *pFileOut, FILE *pFileIn, u32 caseNumber)
{
    fscanf(pFileIn, "%ld", &t);

    for (int i = 0; i < t; i++)
    {
        char buf[101];
        fscanf(pFileIn, "%s\n", &buf);
        for (int j = 0; j < t; j++)
        {
            win[i][j] = (buf[j] == '.') ? -1 : buf[j] - '0';
        }
    }

    double wp[100];
    double owp[100];
    double oowp[100];
    for (int i = 0; i < t; i++)
    {
        score[i] = 0;
        int game = 0;
        int wins = 0;
        for (int j = 0; j < t; j++)
        {
            if (win[i][j] != -1)
                game++;
            if (win[i][j] == 1)
                wins++;
        }
        wp[i] = (double)wins/game;
    }

    for (int i = 0; i < t; i++)
    {
        int opp = 0;
        owp[i] = 0;
        for (int j = 0; j < t; j++)
        {
            if (win[i][j] != -1)
            {
                int op = 0;
                double s = 0;
                for (int k = 0; k < t; k++)
                {
                    if (win[j][k] != -1 && k != i)
                    {
                        op++;
                        s += win[j][k];
                    }
                }
                owp[i] += s / op;
                opp++;
            }
        }
        owp[i] /= opp;
    }

    printf("Case #%ld:\n", caseNumber + 1);
    fprintf(pFileOut, "Case #%ld:\n", caseNumber + 1);
    for (int i = 0; i < t; i++)
    {
        oowp[i] = 0;
        int op = 0;
        for (int j = 0; j < t; j++)
        {
            if (win[i][j] != -1)
            {
                op++;
                oowp[i] += owp[j];
            }
        }
        oowp[i] /= op;
        score[i] = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
        fprintf(pFileOut, "%.7lf\n",score[i]);
        printf("%.7lf\n",score[i]);
    }

}












































