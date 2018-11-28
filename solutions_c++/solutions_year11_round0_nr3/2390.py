#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <list>
#include <assert.h>

using namespace std;

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
    
    
    for (int ca = 0; ca < numberCases; ca++) {
        int numberCandy;
        fscanf(input, "%d ", &numberCandy);
        int candies[numberCandy];
        for (int i = 0; i < numberCandy; i++) {
            fscanf(input, "%d ", &(candies[i]));
        }
        
        int patrickSum = 0;
        for (int i = 0; i < numberCandy; i++) {
            patrickSum = candies[i] ^ patrickSum;
        }
        
        if (patrickSum != 0) {
            fprintf (output, "Case #%d: NO\n", ca + 1);
        } else {
            int min = candies[0];
            int sum = 0;
            for (int i = 0; i < numberCandy; i++) {
                if (candies[i] < min) {
                    min = candies[i];
                }
                sum += candies[i];
            }
            fprintf (output, "Case #%d: %d\n", ca + 1, sum - min);
        }   
    }
    
    fclose(input);
    fclose(output);
    return 0;
}
