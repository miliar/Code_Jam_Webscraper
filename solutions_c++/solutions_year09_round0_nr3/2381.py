#include <cstdio>

const int PATLEN =  19; // pattern length
const int MAXLEN = 500; // maximum input length

char pattern[PATLEN + 1] = "welcome to code jam";
char input[MAXLEN + 1];

int getline(char [], int, FILE *);
int find(int, int, int);
int findwelcome(int);

int main() {
    int n, i;
    FILE *fin, *fout;

    fin  = fopen("C-small-attempt0.in",  "r");
    fout = fopen("C-small-attempt0.out", "w");

    fscanf(fin, "%d\n", &n);
    for(i = 1; i <= n; i++)
        fprintf(fout, "Case #%d: %.4d\n", i, find(0, getline(input, MAXLEN + 1, fin) - (PATLEN - 1), 0));
//      fprintf(fout, "Case #%d: %.4d\n", i, findwelcome(getline(input, MAXLEN + 1, fin)));

    return 0;
}

int getline(char s[], int lim, FILE *fin) {
    int c, i;

    lim = lim - 1;
    for(i = 0; i < lim && (c = getc(fin)) != EOF && c != '\n'; i++)
        s[i] = c;
    s[i] = '\0';

    return i;
}

int findwelcome(int len) { // particular
    int s[PATLEN], n[PATLEN], found;

    n[0] = len - (PATLEN - 1);
    for(int i = 1; i < PATLEN; i++)
        n[i] = n[0] + i;

    found = 0;

    for(s[0]  = 0;         s[0]  < n[0];  s[0]++)  if(input[s[0]]  == 'w')
    for(s[1]  = s[0]  + 1; s[1]  < n[1];  s[1]++)  if(input[s[1]]  == 'e')
    for(s[2]  = s[1]  + 1; s[2]  < n[2];  s[2]++)  if(input[s[2]]  == 'l')
    for(s[3]  = s[2]  + 1; s[3]  < n[3];  s[3]++)  if(input[s[3]]  == 'c')
    for(s[4]  = s[3]  + 1; s[4]  < n[4];  s[4]++)  if(input[s[4]]  == 'o')
    for(s[5]  = s[4]  + 1; s[5]  < n[5];  s[5]++)  if(input[s[5]]  == 'm')
    for(s[6]  = s[5]  + 1; s[6]  < n[6];  s[6]++)  if(input[s[6]]  == 'e')
    for(s[7]  = s[6]  + 1; s[7]  < n[7];  s[7]++)  if(input[s[7]]  == ' ')
    for(s[8]  = s[7]  + 1; s[8]  < n[8];  s[8]++)  if(input[s[8]]  == 't')
    for(s[9]  = s[8]  + 1; s[9]  < n[9];  s[9]++)  if(input[s[9]]  == 'o')
    for(s[10] = s[9]  + 1; s[10] < n[10]; s[10]++) if(input[s[10]] == ' ')
    for(s[11] = s[10] + 1; s[11] < n[11]; s[11]++) if(input[s[11]] == 'c')
    for(s[12] = s[11] + 1; s[12] < n[12]; s[12]++) if(input[s[12]] == 'o')
    for(s[13] = s[12] + 1; s[13] < n[13]; s[13]++) if(input[s[13]] == 'd')
    for(s[14] = s[13] + 1; s[14] < n[14]; s[14]++) if(input[s[14]] == 'e')
    for(s[15] = s[14] + 1; s[15] < n[15]; s[15]++) if(input[s[15]] == ' ')
    for(s[16] = s[15] + 1; s[16] < n[16]; s[16]++) if(input[s[16]] == 'j')
    for(s[17] = s[16] + 1; s[17] < n[17]; s[17]++) if(input[s[17]] == 'a')
    for(s[18] = s[17] + 1; s[18] < n[18]; s[18]++) if(input[s[18]] == 'm')
        found = (found + 1) % 10000;

    return found;
}

int found;

void findpattern(int c, int n, int p) { // general
    if(p < PATLEN) {
        while(c < n)
            if(input[c++] == pattern[p])
                findpattern(c, n + 1, p + 1);
    } else {
        found = (found + 1) % 10000;
    }
}
int find(int c, int n, int p) {
    found = 0;
    findpattern(c, n, p);
    return found;
}
