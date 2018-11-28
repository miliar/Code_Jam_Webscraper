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
        int numRows;
        int numCols;
        fscanf(input, "%d %d\n", &numRows, &numCols);
        //white: 0; blue: 1
        int grid[numRows][numCols];
        char temp;
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                fscanf(input, "%c", &temp);
                if (temp == '.') {
                    grid[i][j] = 0;
                } else if (temp == '#') {
                    grid[i][j] = 1;
                } else {
                    fprintf(stderr, "asdadasdsdsds\n");
                    exit(1);
                }
            }
            fscanf(input, "\n");
        }
        
        bool impossible = false;
        int answer[numRows][numCols];
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                if (grid[i][j] != 1) { //if not blue...
                    ;
                } else {
                    if (i+1 == numRows || j+1 == numCols) {
                        impossible = true;
                        i = numRows;
                        j = numCols;
                    } else {
                        if (grid[i+1][j] != 1 || grid[i][j+1] != 1 || grid[i+1][j+1] != 1) {
                            impossible = true;
                            i = numRows;
                            j = numCols;
                        } else {
                            grid[i][j] = 2;            //23
                            grid[i+1][j] = 4;          //45
                            grid[i][j+1] = 3;
                            grid[i+1][j+1] = 5;
                        }
                    }
                }
                answer[i][j] = grid[i][j];
            }
        }
        
        fprintf (output, "Case #%d:\n", ca+1);
        if (impossible) {
            fprintf(output, "Impossible\n");
        } else {
            for (int i = 0; i < numRows; i++) {
                for (int j = 0; j < numCols; j++) {
                    if (answer[i][j] == 0) {
                        fprintf(output, ".");
                    } else if (answer[i][j] == 1) {
                        fprintf(stderr, "asdasdasdasd\n");
                        exit(1);
                    } else if (answer[i][j] == 2 || answer[i][j] == 5) {
                        fprintf(output, "/");
                    } else if (answer[i][j] == 3 || answer[i][j] == 4) {
                        fprintf(output, "\\");
                    }
                }
                fprintf(output, "\n");
            }
        }
    }
    
    fclose(input);
    fclose(output);
    return 0;
}
