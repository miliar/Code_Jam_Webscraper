#include <iostream>
#define LMax 20
#define DMax 5005

using namespace std;

FILE *fin = fopen("input.in", "rt");
FILE *fout = fopen("output.out", "wt");

int L, D, N;
char dic[DMax][LMax];
char s[LMax * 30];

int main()
{
    int i, j;

    fscanf(fin, "%d %d %d\n", &L, &D, &N);
    for (i = 0; i < D; i++)
        fscanf(fin, "%s\n", dic[i]);

    for (i = 0; i < N; i++)
    {
        fscanf(fin, "%s\n", s);

        int ind, match, sum = 0, find;

        for (int word = 0; word < D; word++)
        {
            ind = 0;
            match = 1;
            for (int letter = 0; letter < L && match; letter++)
            {
                if (s[ind] != '(')
                {
                    if (s[ind] != dic[word][letter])
                        match = 0;
                    ind++;
                }
                else
                {
                    find = 0;
                    for (; s[ind] != ')'; ind++)
                    {
                        if (s[ind] == dic[word][letter])
                            find = 1;
                    }
                    ind ++;
                    if (find == 0)
                        match = 0;
                }
            }
            if (match)
                sum++;
        }
        fprintf(fout, "Case #%d: %d\n", i + 1, sum);
    }

    return 0;
}
