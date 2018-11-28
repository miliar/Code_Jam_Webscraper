#include <stdio.h>
#include <stdlib.h>

int FuncComp(const void* x1, const void* x2)
{
    return *(long*)x1 > *(long*)x2 ? 1 : *(long*)x1 < *(long*)x2 ? -1 : 0;
}

int main()
{
    FILE* fin = stdin;
    FILE* fout = stdout;
    fopen_s(&fin, "A-large.in", "rt");
    fopen_s(&fout, "output.out", "wt");
    int t;
    fscanf_s(fin, "%d", &t);
    for (int caseNum = 1; caseNum <= t; caseNum++)
    {
        int n;
        fscanf_s(fin, "%d", &n);
        long v1[1000], v2[1000];
        for (int count = 0; count < n; count++)
            fscanf_s(fin, "%ld", &v1[count]);
        for (int count = 0; count < n; count++)
            fscanf_s(fin, "%ld", &v2[count]);
        qsort(v1, n, sizeof(*v1), FuncComp);
        qsort(v2, n, sizeof(*v1), FuncComp);
        __int64 sum = 0;
        for (int count = 0; count < n; count++)
            sum += (__int64)v1[count] * v2[n - 1 - count];
        fprintf(fout, "Case #%d: ", caseNum);
        if (sum == 0)
            fprintf(fout, "0");
        else
        {
            char num[100];
            int len = 0;
            bool isMinus = false;
            if (sum < 0)
            {
                isMinus = true;
                sum = -sum;
            }
            for (; sum > 0; sum /= 10)
                num[len++] = '0' + (int)(sum % 10);
            if (isMinus)
                fprintf(fout, "-");
            for (int count = len - 1; count >= 0; count--)
                fprintf(fout, "%c", num[count]);
            fprintf(fout, "\n");
        }
    }
    fclose(fin);
    fclose(fout);
	return 0;
}

