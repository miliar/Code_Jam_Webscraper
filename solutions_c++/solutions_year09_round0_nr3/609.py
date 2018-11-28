#include <iostream>
#include <fstream>
#include <string>
#include <memory.h>
#include <algorithm>
using namespace std;

const char iname[] = "A-large.in";
const char oname[] = "A-large.out";

const int MAXL = 505;

int getAnswer(char *A, int lenA, char *B, int lenB)
{
    int C[2][19], s;
    memset(C, 0, sizeof C);

    C[0][0] = (A[0] == B[0]);
    for (int i = 1; i < lenA; ++ i) {
        s = i & 1;
        C[s][0] = (C[s ^ 1][0] + (A[i] == B[0])) % 10000;
        for (int j = 1; j < lenB; ++ j) {
            C[s][j] = C[s ^ 1][j];
            if (A[i] == B[j])
                C[s][j] = (C[s][j] + C[s ^ 1][j - 1]) % 10000;
        }
    }
    return C[(lenA - 1) & 1][lenB - 1];
}

int main(void)
{
    FILE *fi = fopen(iname, "r");
    FILE *fo = fopen(oname, "w");
    int runs;
    char line[MAXL];
    char pattern[] = "welcome to code jam";
    int pattern_length = strlen(pattern);

    fscanf(fi, "%d\n", &runs);
    for (int i = 0; i < runs; ++ i) {
        fgets(line, MAXL, fi);
        int length = strlen(line);
        while (line[length - 1] == '\n' || line[length - 1]== '\r')
            length --;
        fprintf(fo, "Case #%d: %04d\n", i + 1, getAnswer(line, length, pattern, pattern_length));
    }
    fclose(fi);
    fclose(fo);
    return 0;
}
