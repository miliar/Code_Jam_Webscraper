#include <stdio.h>

bool customer[3000][100][2] = {false};
int n, m;

int result[3000];
int resultMalted = 10000;
int curPermu[3000];
void Permu(int num, int numMalted)
{
    if (num >= n)
    {
        if (numMalted < resultMalted)
        {
            bool isValid = true;
            for (int count = 0; count < m; count++)
            {
                bool isSatisfied = false;
                for (int c1 = 1; c1 <= n; c1++)
                {
                    if (customer[count][c1][curPermu[c1 - 1]])
                    {
                        isSatisfied = true;
                        break;
                    }
                }
                if (!isSatisfied)
                {
                    isValid = false;
                    break;
                }
            }
            if (isValid)
            {
                resultMalted = numMalted;
                for (int count = 0; count < n; count++)
                    result[count] = curPermu[count];
            }
        }
        return;
    }
    curPermu[num] = 0;
    Permu(num + 1, numMalted);
    curPermu[num] = 1;
    Permu(num + 1, numMalted + 1);
}

int main()
{
    FILE* fin = stdin;
    FILE* fout = stdout;
    fopen_s(&fin, "B-small-attempt0.in", "rt");
    fopen_s(&fout, "output.out", "wt");
    int c;
    fscanf_s(fin, "%d", &c);
    for (int caseNum = 1; caseNum <= c; caseNum++)
    {
        fscanf_s(fin, "%d", &n);
        fscanf_s(fin, "%d", &m);
        for (int count = 0; count < m; count++)
        {
            int t;
            fscanf_s(fin, "%d", &t);
            for (int c1 = 1; c1 <= n; c1++)
                customer[count][c1][0] = customer[count][c1][1] = false;
            for (int c1 = 0; c1 < t; c1++)
            {
                int x, y;
                fscanf_s(fin, "%d%d", &x, &y);
                customer[count][x][y] = true;
            }
        }
        resultMalted = 10000;
        Permu(0, 0);
        fprintf(fout, "Case #%d: ", caseNum);
        if (resultMalted >= 10000)
            fprintf(fout, "IMPOSSIBLE");
        else
        {
            fprintf(fout, "%d", result[0]);
            for (int count = 1; count < n; count++)
                fprintf(fout, " %d", result[count]);
        }
        fprintf(fout, "\n");
    }
    fclose(fin);
    fclose(fout);
	return 0;
}

