#include <iostream>

using namespace std;

char hints[][111] = {
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv",
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};

char rep[222];
char result[22222];

char* replace(char *str) {
    int i = 0;
    while (*str != '\0') {
        if (isalpha(*str)) {
            result[i++] = rep[ *str ];
        } else {
            result[i++] = ' ';
        }
        str++;
    }
    result[i] = '\0';
    return result;
}

int main()
{
    rep['q'] = 'z'; rep['z'] = 'q';
    for (int i = 0; i < 3; i++) {
        for (int j = strlen(hints[i])-1; j >= 0; j--) {
            if (isalpha(hints[i][j])) {
                if (rep[ hints[i][j] ] != hints[i+3][j]) {
                    if (rep[ hints[i][j] ] != 0) {
                        printf("Error: %c %c %c\n", hints[i][j], rep[ hints[i][j] ], hints[i+3][j]);
                    }
                    rep[ hints[i][j] ] = hints[i+3][j];
                }
            }
        }
    }
    /*
    for (int i = 'a'; i <= 'z'; i++) {
        printf("%c-->%c\n", i, rep[i]);
    }
    sort(rep+'a', rep+'z');
    for (int i = 'a'; i <= 'z'; i++) {
        printf("=%c=\n", rep[i]);
    }
    */
    FILE *fin, *fout;
    fin = fopen("D:\\TopCoder\\gcj2012\\QR\\A-small-attempt0.in", "r");
    fout = fopen("D:\\TopCoder\\gcj2012\\QR\\A.out", "w");
    int T;
    fscanf(fin, "%d\n", &T);
    for (int ca = 1; ca <= T; ca++) {
        char str[11111];
        fgets(str, 11111, fin);
        fprintf(fout, "Case #%d: %s\n", ca, replace(str));
    }
    
    fclose(fin);
    fclose(fout);
    return 0;
}
