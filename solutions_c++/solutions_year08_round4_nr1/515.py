// A.cpp : main project file.

#include "stdafx.h"
#include <stdio.h>

using namespace System;

int main(array<System::String ^> ^args)
{
    int minGate[20000][2];
    int gateType[20000];
    bool isChangable[20000];
    FILE* fin = stdin;
    FILE* fout = stdout;
    fopen_s(&fin, "A-large.in", "rt");
    fopen_s(&fout, "output.out", "wt");
    int n;
    fscanf_s(fin, "%d", &n);
    for (int caseNum = 1; caseNum <= n; caseNum++)
    {
        int m, v;
        fscanf_s(fin, "%d%d", &m, &v);
        for (int count = 0; count < m; count++)
            minGate[count][0] = minGate[count][1] = 30000;
        int numGate = (m - 1) / 2;
        for (int count = 0; count < numGate; count++)
        {
            int g, c;
            fscanf_s(fin, "%d%d", &g, &c);
            gateType[count] = g;
            isChangable[count] = c > 0;
        }
        int numLeaf = (m + 1) / 2;
        for (int count = 0; count < numLeaf; count++)
        {
            int x;
            fscanf_s(fin, "%d", &x);
            minGate[(m - 1) / 2 + count][x] = 0;
        }
        for (int count = (m - 1) / 2 - 1; count >= 0; count--)
        {
            int leftNode = count * 2 + 1;
            int rightNode = count * 2 + 2;
            if (gateType[count] == 1 || isChangable[count])
            {
                int changeValue = 1 - gateType[count];
                int result;
                result = minGate[leftNode][0] + minGate[rightNode][0] + changeValue;
                if (result < minGate[count][0])
                    minGate[count][0] = result;
                result = minGate[leftNode][0] + minGate[rightNode][1] + changeValue;
                if (result < minGate[count][0])
                    minGate[count][0] = result;
                result = minGate[leftNode][1] + minGate[rightNode][0] + changeValue;
                if (result < minGate[count][0])
                    minGate[count][0] = result;
                result = minGate[leftNode][1] + minGate[rightNode][1] + changeValue;
                if (result < minGate[count][1])
                    minGate[count][1] = result;
            }
            if (gateType[count] == 0 || isChangable[count])
            {
                int changeValue = gateType[count];
                int result;
                result = minGate[leftNode][0] + minGate[rightNode][0] + changeValue;
                if (result < minGate[count][0])
                    minGate[count][0] = result;
                result = minGate[leftNode][0] + minGate[rightNode][1] + changeValue;
                if (result < minGate[count][1])
                    minGate[count][1] = result;
                result = minGate[leftNode][1] + minGate[rightNode][0] + changeValue;
                if (result < minGate[count][1])
                    minGate[count][1] = result;
                result = minGate[leftNode][1] + minGate[rightNode][1] + changeValue;
                if (result < minGate[count][1])
                    minGate[count][1] = result;
            }
        }
        fprintf(fout, "Case #%d: ", caseNum);
        if (minGate[0][v] < 30000)
            fprintf(fout, "%d", minGate[0][v]);
        else
            fprintf(fout, "IMPOSSIBLE");
        fprintf(fout, "\n");
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
