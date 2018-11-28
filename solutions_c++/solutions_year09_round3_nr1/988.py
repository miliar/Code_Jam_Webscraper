#include <cstdio>

const int MAXMESS = 61;
const int DIGIT =  10;
const int ALPHA =  26;
const int ASCII = 128;

char message[MAXMESS];
int isdigit[ASCII];
int decimal[ASCII];
char digit[DIGIT + ALPHA];

int translate(char *m) {
    isdigit[*m] = 1;
    decimal[digit[1] = *m] = 1; // first encountered digit is 1

    while(isdigit[*++m])
        ;
    isdigit[*m] = 1;
    decimal[digit[0] = *m] = 0; // second encountered digit is 0

    int d = 2;
    while(*++m)
        if(!isdigit[*m]) {
            digit[d] = *m;
            isdigit[*m] = 1;
            decimal[*m] = d++;
        }
    return d; // return base
}
void reset(int b) {
    while(--b >= 0)
        isdigit[digit[b]] = 0;
}
// alien to decimal
unsigned long long atod(char *s, int b) {
    unsigned long long n = 0ULL;

    while(*s)
        n = b * n + decimal[*s++];

    return n;
}
int main() {
    int ntests, test, base;
    FILE *fin, *fout;

    fin  = fopen("A-small-attempt0.in",  "r");
    fout = fopen("A-small-attempt0.out", "w");

    fscanf(fin, "%d", &ntests);
    for(test = 1; test <= ntests; test++) {
        fscanf(fin, "%s", message);
        base = translate(message);
        fprintf(fout, "Case #%d: %llu\n", test, atod(message, base));
        reset(base);
    }

    return 0;
}
