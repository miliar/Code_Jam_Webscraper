#include <cstdio>

int main(int argc, char **argv) {
    unsigned int t;
    scanf("%u\n", &t);

    for (unsigned int i = 1; i <= t; i++) {
        unsigned int n, k;
        scanf("%u %u\n", &n, &k);

        unsigned int mask = 1 << n;
        unsigned int remainder = k % mask;

        printf("Case #%u: ", i); 
        if (remainder == mask - 1) {
            printf("ON");
        } else {
            printf("OFF");
        }
        printf("\n");
    }
}
