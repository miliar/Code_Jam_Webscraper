#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <list>
#include <assert.h>

using namespace std;

char combinesWithToForm (char x, char y, char* combineArray[], int combineLength) {
    for (int i = 0; i < combineLength; i++) {
        char *comb = combineArray[i];
        if (comb[0] == x && comb[1] == y) {
            return comb[2];
        } else if (comb[1] == x && comb[0] == y) {
            return comb[2];
        }
    }
    return ' ';
}

bool isOpposedTo (char x, char y, char* opposedArray[], int opposedLength) {
    for (int i = 0; i < opposedLength; i++) {
        char *comb = opposedArray[i];
        if (comb[0] == x && comb[1] == y) {
            return true;
        } else if (comb[1] == x && comb[0] == y) {
            return true;
        }
    }
    return false;
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
    list<char> gameList;
    
    
    for (int ca = 0; ca < numberCases; ca++) {
        int numberCombine;
        int numberOpposed;
        int numberElements;
    
        fscanf(input, "%d ", &numberCombine);
        char *combine[numberCombine];
        for (int i = 0; i < numberCombine; i++) {
            combine[i] = new char[3];
            fscanf(input, "%c%c%c ", &(combine[i][0]), &(combine[i][1]), &(combine[i][2]));
        }
        
        fscanf(input, "%d ", &numberOpposed);
        char *opposed[numberOpposed];
        for (int i = 0; i < numberOpposed; i++) {
            opposed[i] = new char[2];
            fscanf(input, "%c%c ", &(opposed[i][0]), &(opposed[i][1]));
        }
        
        fscanf(input, "%d ", &numberElements);
        list<char> elements;
        for (int i = 0; i < numberElements; i++) {
            elements.push_back(fgetc(input));
        }
        fscanf(input, "\n");
        
        while (!gameList.empty()) {
            gameList.pop_back();
        }
        
        char curElement;
        char combElement;
        char lastElement;
        
        while (!elements.empty()) {
            bool combined = false;
            curElement = elements.front();
            if (!gameList.empty()) {
                lastElement = gameList.back();
            } else {
                lastElement = ' ';
            }
            elements.pop_front();
            gameList.push_back(curElement);
            //combinations
            if (!gameList.empty()) {
                combElement = combinesWithToForm(curElement, lastElement, combine, numberCombine);
                if (combElement != ' ') {
                    gameList.pop_back();
                    gameList.pop_back();
                    gameList.push_back(combElement);
                    combined = true;
                }
            }
            
            //oppositions
            if (!combined) {
                for (list<char>::iterator it = gameList.begin(); it != gameList.end(); it++) {
                    if (isOpposedTo(curElement, *it, opposed, numberOpposed)) {
                        while (!gameList.empty()) {
                            gameList.pop_back();
                        }
                        assert (gameList.empty());
                        it = gameList.end();
                    }
                }
            }
        }
        
        fprintf (output, "Case #%d: [", ca + 1);
        list<char>::iterator it;
        for (it = gameList.begin(); it != gameList.end(); ) {
            fprintf (output, "%c", *it);
            if (++it != gameList.end()) {
                fprintf (output, ", ");
            }
        }
        fprintf (output, "]\n");
        
    }
    
    
    fclose(input);
    fclose(output);
    return 0;
}
