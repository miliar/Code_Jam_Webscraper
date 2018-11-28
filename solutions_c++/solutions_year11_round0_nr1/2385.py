#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <list>
#include <assert.h>

using namespace std;

int findNext(char color, char* instrColors, int startingWith, int instrLength) {
    int i = startingWith;
    while (i < instrLength) {
        if (instrColors[i] == color) {
            return i;
        }
        i++;
    }
    return -1;
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
    
    
    
    for (int i = 0; i < numberCases; i++) {
        
        int instrLength;
        int nextBlue = -1;
        int nextOrange = -1;
        int blueLoc = 0; //0 based remember
        int orangeLoc = 0;
        int timer;
        int upto;
        
        fscanf(input, "%d ", &instrLength);
        char instrColors[instrLength];
        int instrLocs[instrLength];
        for (int j = 0; j < instrLength; j++) {
            fscanf(input, "%c %d ", &(instrColors[j]), &(instrLocs[j]));
        }
        for (int j = 0; j < instrLength; j++) {
            instrLocs[j]--; //make it zero-indexed
        }
        
        timer = 0;
        upto = 0;
        nextOrange = findNext('O', instrColors, 0, instrLength);
        nextBlue = findNext('B', instrColors, 0, instrLength);
        
        while (upto != instrLength) {
            if (upto == nextOrange) {
                if (orangeLoc == instrLocs[upto]) {
                    upto++;
                    nextOrange = findNext('O', instrColors, upto, instrLength);
                    /*if (nextOrange == -1 && nextBlue == -1) {
                        continue;
                    }*/
                } else if (orangeLoc < instrLocs[upto]) {
                    orangeLoc++;
                } else { // >
                    orangeLoc--;
                }
                
                if (blueLoc == instrLocs[nextBlue]) {
                    ;
                } else if (blueLoc < instrLocs[nextBlue]) {
                    blueLoc++;
                } else {
                    blueLoc--;
                }
            } else {
                if (blueLoc == instrLocs[upto]) {
                    upto++;
                    nextBlue = findNext('B', instrColors, upto, instrLength);
                    /*if (nextOrange == -1 && nextBlue == 1) {
                        continue;
                    }*/
                } else if (blueLoc < instrLocs[upto]) {
                    blueLoc++;
                } else { // >
                    blueLoc--;
                }
                
                if (orangeLoc == instrLocs[nextOrange]) {
                    ;
                } else if (orangeLoc < instrLocs[nextOrange]) {
                    orangeLoc++;
                } else {
                    orangeLoc--;
                }
            }
            
            timer++;
        }
        
        
        
        
        
        
        
        
        
        fprintf (output, "Case #%d: %d\n", i + 1, timer);
    }
    
    
    fclose(input);
    fclose(output);
    return 0;
}
