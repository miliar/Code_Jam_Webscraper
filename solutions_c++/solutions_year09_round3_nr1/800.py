#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <utility>

int replace[500];

long long minimun(char* in)
{
    int i = 0;
    int num[64];
    int num_size = 0;
    int base = 0;
    memset(replace, -1, sizeof replace);

    int c = 1;
    while(in[i] != '\0') {
        if (replace[in[i]] == -1) {
            base++;
            replace[in[i]] = c;
            num[i] = c;
            if (c == 1)
                c = 0;
            else if (c == 0) {
                c = 2;
            } else {
                c++;
            }
        } else {
            num[i] = replace[in[i]];
        }
        i++;
    }
    num_size = i;
    if (base < 2) base = 2;

    /*for(int j = 0; j < num_size; j++) {
        printf("%d ", num[j]);
    }
    putchar('\n');*/

    int j = 1;
    int k = num_size - 1;
    long long first_pow = 1;
    long long retVal = num[k];
    //printf(" :: size %d, base %d, k %d\n", num_size, base, k);
    for(; j < num_size; j++) {
        k--;
        first_pow *= base;
        retVal += num[k] * first_pow;
    }
    return retVal;
}

int main(void)
{
    int T;
    scanf("%d", &T);

    for(int caso = 1; caso <= T; caso++) {
        char in[64];
        scanf("%s", in);
        printf("Case #%d: %lld\n", caso, minimun(in));
    }

    return 0;
}

