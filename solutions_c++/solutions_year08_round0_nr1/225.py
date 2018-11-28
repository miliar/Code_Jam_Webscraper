#include <stdio.h>
#include <string.h>

int main()
{
    char searchEngineNames[200][200];
    bool isUsed[200];
    int numUsed;
    FILE* fin = stdin;
    FILE* fout = stdout;
    fopen_s(&fin, "A-large.in", "rt");
    fopen_s(&fout, "output.out", "wt");
    int n;
    fscanf_s(fin, "%d", &n);
    for (int count = 1; count <= n; count++)
    {
        int s;
        fscanf_s(fin, "%d\n", &s);
        for (int c1 = 0; c1 < s; c1++)
        {
            fgets(searchEngineNames[c1], 200, fin);
            isUsed[c1] = false;
        }
        numUsed = 0;
        int q;
        fscanf_s(fin, "%d\n", &q);
        int numSwitch = 0;
        for (int c1 = 0; c1 < q; c1++)
        {
            char queryWord[200];
            fgets(queryWord, 200, fin);
            for (int c2 = 0; c2 < s; c2++)
                if (strcmp(queryWord, searchEngineNames[c2]) == 0)
                {
                    if (!isUsed[c2])
                        numUsed++;
                    isUsed[c2] = true;
                    if (numUsed >= s)
                    {
                        for (int c3 = 0; c3 < s; c3++)
                            isUsed[c3] = false;
                        numUsed = 1;
                        isUsed[c2] = true;
                        numSwitch++;
                    }
                    break;
                }
        }

        fprintf_s(fout, "Case #%d: %d\n", count, numSwitch);
    }
    fclose(fin);
    fclose(fout);
	return 0;
}
