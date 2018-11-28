#include "cstdio"
#include "cstdlib"
#include <iostream>

inline bool bit_test(int val, int pos) { return(val & (1 << pos)); }

int main(int argc, char *argv[])
{
    FILE *ifp = fopen(argv[1], "r");
    FILE *ofp = fopen(argv[2], "w");

    int tc;

    fscanf(ifp, "%d", &tc);

    printf("%d tests\n", tc);

    for (int t = 1; t <= tc; t++)
    {
        int N, K;

        fscanf(ifp, "%d %d", &N, &K);

        printf("Processing testcase #%d (N:%d K:%d)\n", t, N, K);

        int p = (1 << N) - 1;

        bool light_is_on = ((K & p) == p);

        fprintf(ofp, "Case #%d: %s\n", t, light_is_on ? "ON" : "OFF");
    }

    fclose(ifp);
    fclose(ofp);

    return (0);
}
