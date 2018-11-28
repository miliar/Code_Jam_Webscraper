#include <iostream>
#define LMax 505

using namespace std;

char wstr[20] = "welcome to code jam";
//---------------1234567890123456789

FILE *fin = fopen("input.in", "rt");
FILE *fout = fopen("output.out", "wt");

char s[LMax];
int len, ways[LMax][19];

int main()
{
    int n, i, j, sum, test;
    fscanf(fin, "%d\n", &n);\

    for (test = 1; test <= n; test++)
    {
        fgets(s, LMax, fin);
        len = strlen(s) - 1;

        for (i = 0; i < len; i++)
            for (j = 0; j < 19; j++)
                ways[i][j] = 0;

        if (s[0] == wstr[0])
            ways[0][0] = 1;

        for (i = 1; i < len; i++)
        {
            if (s[i] == wstr[0])
                ways[i][0]++;

            for (j = 1; j < 19; j++) {
                if (s[i] == wstr[j])
                {
                    ways[i][j] += ways[i-1][j-1];
                    ways[i][j] %= 10000;
                }
            }
            for (j = 0; j < 19; j++) {
                ways[i][j] += ways[i-1][j];
                ways[i][j] %= 10000;
            }
        }

        //sum = 0;
        //for (i = len-1; i < len; i++)
            //sum = (sum + ways[i][18]) % 10000;
        sum = ways[len-1][18];

        fprintf(fout, "Case #%d: %04d\n", test, sum);
    }

    return 0;
}
