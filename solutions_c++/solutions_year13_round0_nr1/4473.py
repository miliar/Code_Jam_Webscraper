#include <cstdio>
#include <cstdlib>

#define GRID_WIDTH  4
#define GRID_HEIGHT 4

#define OUTCOME_UNSURE 0
#define OUTCOME_X 1
#define OUTCOME_O 2
#define OUTCOME_DRAW 3

int outcomeForGrid(char grid[][4]);

int main(int argc, char* argv[]) {
    FILE* infile = fopen("tomek.in", "r");

    int ncases;
    char grid[4][4];
    char c;

    fscanf(infile, "%d\n", &ncases);

    for (int i = 0; i < ncases; i++) {

        for (int y = 0; y < GRID_HEIGHT; y++) {
            for (int x = 0; x < GRID_WIDTH; x++) {
                fscanf(infile, "%c", &grid[x][y]);
            }
            fscanf(infile, "%c", &c); // newline
        }
        fscanf(infile, "%c", &c); // another newline

        int outcome = outcomeForGrid(grid);

        printf("Case #%d: ", i+1);
        if (outcome == OUTCOME_UNSURE) {
            printf("Game has not completed");
        } else if (outcome == OUTCOME_X) {
            printf("X won");
        } else if (outcome == OUTCOME_O) {
            printf("O won");
        } else if (outcome == OUTCOME_DRAW) {
            printf("Draw");
        }
        printf("\n");
    }

    fclose(infile);

    return EXIT_SUCCESS;
}

int outcomeForGrid(char grid[][4]) {
    // check for horizontal wins
    for (int y = 0; y < GRID_HEIGHT; y++) {
        int xcount = 0;
        int ocount = 0;
        int tcount = 0;

        for (int x = 0; x < 4; x++) {
            if (grid[x][y] == 'X') {
                xcount++;
            } else if (grid[x][y] == 'O') {
                ocount++;
            } else if (grid[x][y] == 'T') {
                tcount++;
            }
        }

        if (xcount == 4 || (xcount == 3 && tcount == 1)) {
            return OUTCOME_X;
        } else if (ocount == 4 || (ocount == 3 && tcount == 1)) {
            return OUTCOME_O;
        }
    }

    // check for vertical wins
    for (int x = 0; x < 4; x++) {
        int xcount = 0;
        int ocount = 0;
        int tcount = 0;

        for (int y = 0; y < 4; y++) {
            if (grid[x][y] == 'X') {
                xcount++;
            } else if (grid[x][y] == 'O') {
                ocount++;
            } else if (grid[x][y] == 'T') {
                tcount++;
            }
        }

        if (xcount == 4 || (xcount == 3 && tcount == 1)) {
            return OUTCOME_X;
        } else if (ocount == 4 || (ocount == 3 && tcount == 1)) {
            return OUTCOME_O;
        }
    }

    // check for diagonal wins
    int xcount1 = 0;
    int ocount1 = 0;
    int tcount1 = 0;

    int xcount2 = 0;
    int ocount2 = 0;
    int tcount2 = 0;

    for (int x = 0; x < 4; x++) {

        if (grid[x][x] == 'X') {
            xcount1++;
        } else if (grid[x][x] == 'O') {
            ocount1++;
        } else if (grid[x][x] == 'T') {
            tcount1++;
        }

        if (grid[3-x][x] == 'X') {
            xcount2++;
        } else if (grid[3-x][x] == 'O') {
            ocount2++;
        } else if (grid[3-x][x] == 'T') {
            tcount2++;
        }

    }

    if (xcount1 == 4 || (xcount1 == 3 && tcount1 == 1)) {
        return OUTCOME_X;
    } else if (ocount1 == 4 || (ocount1 == 3 && tcount1 == 1)) {
        return OUTCOME_O;
    }

    if (xcount2 == 4 || (xcount2 == 3 && tcount2 == 1)) {
        return OUTCOME_X;
    } else if (ocount2 == 4 || (ocount2 == 3 && tcount2 == 1)) {
        return OUTCOME_O;
    }

    // check for any presence of a dot to indicate it ain't over
    for (int x = 0; x < 4; x++) {
        for (int y = 0; y < 4; y++) {
            if (grid[x][y] == '.') {
                return OUTCOME_UNSURE;
            }
        }
    }

    // can only be a draw
    return OUTCOME_DRAW;
}
