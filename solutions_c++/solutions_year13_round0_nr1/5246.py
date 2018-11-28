#include <stdio.h>
#include <stdlib.h>

static const char* x_won = "X won";
static const char* o_won = "O won";
static const char* draw = "Draw";
static const char* incomplete = "Game has not completed";

const char* ticTacToeTomek(char square[4][4])
{
//    for (int row=0; row<4; ++row) {
//        printf("%c%c%c%c\n", square[row][0], square[row][1], square[row][2], square[row][3]);
//    }
//    printf("\n");
    
    // rows
    int emptySquares=0;
    for (int row=0; row<4; ++row) {
        int x=0, o=0;
        for (int col=0; col<4; ++col) {
            if (square[row][col] == 'X') {
                ++x;
            } else if (square[row][col] == 'O') {
                ++o;
            } else if (square[row][col] == 'T') {
                ++x;
                ++o;
            } else if (square[row][col] == '.') {
                ++emptySquares;
            }
        }
        
        if (x == 4) {
            return x_won;
        } else if (o == 4) {
            return o_won;
        }
    }
    
    // cols
    for (int col=0; col<4; ++col) {
        int x=0, o=0;
        for (int row=0; row<4; ++row) {
            if (square[row][col] == 'X') {
                ++x;
            } else if (square[row][col] == 'O') {
                ++o;
            } else if (square[row][col] == 'T') {
                ++x;
                ++o;
            }
        }
        
        if (x == 4) {
            return x_won;
        } else if (o == 4) {
            return o_won;
        }
    }

    // back slash
    int x, o;
    
    x=0, o=0;
    for (int i=0; i<4; ++i) {
        if (square[i][i] == 'X') {
            ++x;
        } else if (square[i][i] == 'O') {
            ++o;
        } else if (square[i][i] == 'T') {
            ++x;
            ++o;
        }
        
        if (x == 4) {
            return x_won;
        } else if (o == 4) {
            return o_won;
        }
    }
    
    // forward slash
    x=0, o=0;
    for (int i=0; i<4; ++i) {
        if (square[i][3-i] == 'X') {
            ++x;
        } else if (square[i][3-i] == 'O') {
            ++o;
        } else if (square[i][3-i] == 'T') {
            ++x;
            ++o;
        }
        
        if (x == 4) {
            return x_won;
        } else if (o == 4) {
            return o_won;
        }
    }
    
    if (emptySquares) {
        return incomplete;
    }
    
    return draw;
}

void codeJam(int numcases, FILE* fin, FILE* fout)
{
    char square[4][4] = {0};
    
    for (int test=0; test<numcases; ++test) {
        for (int i=0; i<4; ++i) {
            fscanf(fin, "%c%c%c%c\n", square[i]+0, square[i]+1, square[i]+2, square[i]+3);
        }
        fscanf(fin, "\n");
        
        fprintf(fout, "Case #%d: %s\n", test+1, ticTacToeTomek(square));
    }
}

int main(int argc, const char * argv[])
{
    if (argc != 3) {
        printf("usage: %s [input.txt] [output.txt]\n", argv[0]);
        exit(1);
    }
    
    FILE* fin = fopen(argv[1], "r");
    if (!fin) {
        printf("unable to open input '%s'\n", argv[1]);
        exit(1);
    }
    
    FILE* fout = fopen(argv[2], "w");
    if (!fout) {
        printf("unable to open output '%s'\n", argv[2]);
        exit(1);
    }

    int numcases = 0;
    fscanf(fin, "%d\n", &numcases);

    printf("code jamming %d cases: '%s' -> '%s'.\n", numcases, argv[1], argv[2]);
    codeJam(numcases, fin, fout);
    
    fclose(fin);
    fclose(fout);
    
    return 0;
}

