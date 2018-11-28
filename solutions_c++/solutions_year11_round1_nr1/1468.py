#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <list>
#include <assert.h>

using namespace std;

// a >= b
int gcd (int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd (b, a % b);
}

int main (int argc, char *argv[]) {

    if (argc != 2) {
        fprintf(stderr, "Not the right number of command line arguments\n");
        exit(1);
    } 
    FILE *input = fopen(argv[1], "r");
    FILE *output = fopen(strcat (argv[1], "_output"), "w");
    assert(input);
    int numberCases = 0;
    fscanf(input, "%d\n", &numberCases);
    int n;
    int pd;
    int pg;
    for (int ca = 0; ca < numberCases; ca++) {
        
        fscanf (input, "%d %d %d\n", &n, &pd, &pg);
        bool possible = false;
        bool pdpossible = true;
        if (n < 100) {
            if (n < 100 / gcd(100, pd)) {
                pdpossible = false;
            }
        }
        if (pdpossible && pd != 0) {
            for (int i = 0; i < 10000 || i < n; i++) {
                if ((i * 100) % pd == 0) {
                    possible = true;
                }
            }
        }
        if (pg == 100 && pd != 100) {
            possible = false;
        }
        if (pg == 0 && pd != 0) {
            possible = false;
        }
        
        if (possible) {
            fprintf (output, "Case #%d: Possible\n", ca + 1);
        } else {
            fprintf (output, "Case #%d: Broken\n", ca + 1);
        }
    }
    
    fclose(input);
    fclose(output);
    return 0;
}
