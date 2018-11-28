#include <stdio.h>

int main()
{
    int timeA[200][2];
    int timeB[200][2];
    bool isLinkedA[200];
    bool isLinkedB[200];
    FILE* fin = stdin;
    FILE* fout = stdout;
    fopen_s(&fin, "B-large.in", "rt");
    fopen_s(&fout, "output.out", "wt");
    int n;
    fscanf_s(fin, "%d", &n);
    for (int count = 1; count <= n; count++)
    {
        int t, na, nb;
        fscanf_s(fin, "%d", &t);
        fscanf_s(fin, "%d%d", &na, &nb);
        for (int c1 = 0; c1 < na; c1++)
        {
            int h, m;
            fscanf_s(fin, "%d:%d", &h, &m);
            timeA[c1][0] = h * 60 + m;
            fscanf_s(fin, "%d:%d", &h, &m);
            timeA[c1][1] = h * 60 + m;
            isLinkedA[c1] = false;
        }
        for (int c1 = 0; c1 < nb; c1++)
        {
            int h, m;
            fscanf_s(fin, "%d:%d", &h, &m);
            timeB[c1][0] = h * 60 + m;
            fscanf_s(fin, "%d:%d", &h, &m);
            timeB[c1][1] = h * 60 + m;
            isLinkedB[c1] = false;
        }

        int xa = na, xb = nb;
        for (int c1 = 0; c1 < na; c1++)
        {
            int minTime = 10000;
            int minNum = -1;
            for (int c2 = 0; c2 < nb; c2++)
            {
                if (timeB[c2][0] >= timeA[c1][1] + t && !isLinkedB[c2] && timeB[c2][0] < minTime)
                {
                    minTime = timeB[c2][0];
                    minNum = c2;
                }
            }
            if (minNum >= 0)
            {
                xb--;
                isLinkedB[minNum] = true;
            }
        }
        for (int c1 = 0; c1 < nb; c1++)
        {
            int minTime = 10000;
            int minNum = -1;
            for (int c2 = 0; c2 < na; c2++)
            {
                if (timeA[c2][0] >= timeB[c1][1] + t && !isLinkedA[c2] && timeA[c2][0] < minTime)
                {
                    minTime = timeA[c2][0];
                    minNum = c2;
                }
            }
            if (minNum >= 0)
            {
                xa--;
                isLinkedA[minNum] = true;
            }
        }

        fprintf(fout, "Case #%d: %d %d\n", count, xa, xb);
    }
    fclose(fin);
    fclose(fout);
	return 0;
}

