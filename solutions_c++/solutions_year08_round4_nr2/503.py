// B.cpp : main project file.

#include "stdafx.h"
#include <stdio.h>
#include <math.h>

using namespace System;

int main(array<System::String ^> ^args)
{
    FILE* fin = stdin;
    FILE* fout = stdout;
    fopen_s(&fin, "B-small-attempt0.in", "rt");
    fopen_s(&fout, "output.out", "wt");
    int n;
    fscanf_s(fin, "%d", &n);
    for (int caseNum = 1; caseNum <= n; caseNum++)
    {
        long n, m, a;
        fscanf_s(fin, "%ld%ld%ld", &n, &m, &a);
        fprintf(fout, "Case #%d: ", caseNum);
        bool isPossible = false;
        for (int x1 = 0; x1 <= n; x1++)
        {
            for (int y2 = x1; y2 <= m; y2++)
            {
                for (int x2 = 0; x2 <= n; x2++)
                {
                    for (int y1 = 0; y1 <= m; y1++)
                    {
                        if (abs(x1 * y2 - x2 * y1) == a)
                        {
                            fprintf(fout, "0 0 %d %d %d %d\n", x1, y1, x2, y2);
                            isPossible = true;
                            break;
                        }
                    }
                    if (isPossible)
                        break;
                }
                if (isPossible)
                    break;
            }
            if (isPossible)
                break;
        }
        if (!isPossible)
            fprintf(fout, "IMPOSSIBLE\n");
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
