#include <cstdlib>
#include <cstring>
#include <cstdio>
using namespace std;

int main (int argc, char** argv) {
    if (argc != 2) {
        printf ("\nERROR - Incorrect number of arguments");
        printf ("\nSyntax : %s filename\n", argv [0]);
        exit (EXIT_FAILURE);
    }
    
    FILE *inputStream = fopen (argv[1], "r");
    if (inputStream == NULL)
    {
        printf ("\nERROR - Unable to access %s\n", argv[1]);
        exit (EXIT_FAILURE);
    }
    
    char *outputFile = "output.txt";
    FILE *outputStream = fopen (outputFile, "w");
    if (outputStream == NULL)
    {
        printf ("\nERROR - Unable to access %s\n", outputFile);
        exit (EXIT_FAILURE);
    }
    

    int T, R, k, N, money, seated, first, a, b, c, d, x;
    int g[1000];
    char *groupSplit, *groups;
    
    fscanf (inputStream, "%i", &T);
    for (a = 1; a <= T; a++) {
        fscanf (inputStream, "%i %i %i\n", &R, &k, &N);
        fgets (groups , 9001, inputStream);

        groupSplit = strtok (groups, " ");
        b = 0;
        while (groupSplit != NULL) {
            g[b] = atoi(groupSplit);
            b++;
            groupSplit = strtok (NULL, " ");
        }

        money = 0;
        first = 0;
        for (c = 0; c < R; c++) {
            seated = 0;
            x = N;
            d = first;
            while (d < x) {
                if (seated + g[d] > k) {
                    first = d;
                    break;
                }
                seated += g[d];
                if (d == x - 1 && first != 0) {
                    d = 0;
                    x = first;
                } else
                    d++;
            }
            money += seated;
        }
        fprintf(outputStream, "Case #%i: %i\n", a, money);
        printf("Case #%i: %i\n", a, money);
    }
    fclose (inputStream);
    fclose (outputStream);
    return EXIT_SUCCESS;
}
