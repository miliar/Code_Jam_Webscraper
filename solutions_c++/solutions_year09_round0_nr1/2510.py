#include <cstdio>

const int MAXL =   15; // maximum number of letters
const int ALPH =   26; // number of letters in the alphabet
const int MAXW = 5000; // maximum number of words in the dictionary
const int MAXP = MAXL * (ALPH + 2); // maximum pattern length (abc...z)(abc...z)...(abc...z)

int getline(char s[], int lim, FILE *fin) {
    int c, i;

    lim = lim - 1;
    for(i = 0; i < lim && (c = getc(fin)) != EOF && c != '\n'; i++)
        s[i] = c;
    s[i] = '\0';

    return i;
}
void tokens(char pattern[], char token[][ALPH + 1]) {
    int i, t, j;
    for(t = i = 0; pattern[i]; i++) {
        if(pattern[i] != '(') {
            token[t][0] = pattern[i];
            token[t++][1] = '\0';
        } else {
            for(j = 0; pattern[++i] != ')'; j++)
                token[t][j] = pattern[i];
            token[t++][j] = '\0';
        }
    }
}
int findletter(char letter, char token[]) {
    for(int i = 0; token[i]; i++)
        if(token[i] == letter)
            return 1;
    return 0;
}
int findword(char word[], char token[][ALPH + 1]) {
    for(int letter = 0; word[letter]; letter++)
        if(!findletter(word[letter], token[letter]))
            return 0;
    return 1;
}
// number of possible interpretations
int npossib(char dictionary[][MAXL + 1], int nwords, char token[][ALPH + 1]) {
    int possib = 0;

    for(int word = 0; word < nwords; word++)
        possib += findword(dictionary[word], token);

    return possib;
}
int main() {
    char dictionary[MAXW][MAXL + 1];
    char pattern[MAXP + 1];
    char token[MAXL][ALPH + 1];
    int nletters, nwords, n, i;
    FILE *fin, *fout;

    fin  = fopen("A-small-attempt0.in",  "r");
    fout = fopen("A-small-attempt0.out", "w");

    fscanf(fin, "%d%d%d\n", &nletters, &nwords, &n);

    for(i = 0; i < nwords; i++)
        getline(dictionary[i], MAXL + 1, fin);

    for(i = 1; i <= n; i++) {
        getline(pattern, MAXP + 1, fin);
        tokens(pattern, token);
        fprintf(fout, "Case #%d: %d\n", i, npossib(dictionary, nwords, token));
    }

    return 0;
}
