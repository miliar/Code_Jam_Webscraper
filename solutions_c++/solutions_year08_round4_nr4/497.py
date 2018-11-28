// D.cpp : main project file.

#include "stdafx.h"
#include <stdio.h>
#include <string.h>

using namespace System;

int k;
char s[10000];
int minCompressedSize;
bool isNumUsed[20] = {false};
int permuNum[20];

void Permu(int x)
{
    if (x >= k)
    {
        int len = strlen(s);
        int compressedSize = 0;
        char lastChar = 0;
        for (int count = 0; count < len; count += k)
        {
            for (int c1 = 0; c1 < k; c1++)
            {
                char curChar = s[count + permuNum[c1]];
                if (curChar != lastChar)
                    compressedSize++;
                lastChar = curChar;
            }
        }
        if (compressedSize < minCompressedSize)
            minCompressedSize = compressedSize;
        return;
    }
    for (int count = 0; count < k; count++)
        if (!isNumUsed[count])
        {
            isNumUsed[count] = true;
            permuNum[x] = count;
            Permu(x + 1);
            isNumUsed[count] = false;
        }
}

int main(array<System::String ^> ^args)
{
    FILE* fin = stdin;
    FILE* fout = stdout;
    fopen_s(&fin, "D-small-attempt0.in", "rt");
    fopen_s(&fout, "output.out", "wt");
    int n;
    fscanf_s(fin, "%d", &n);
    for (int caseNum = 1; caseNum <= n; caseNum++)
    {
        fscanf_s(fin, "%d", &k);
        fscanf_s(fin, "%s", s, 10000);
        minCompressedSize = 10000;
        Permu(0);
        fprintf(fout, "Case #%d: %d\n", caseNum, minCompressedSize);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
