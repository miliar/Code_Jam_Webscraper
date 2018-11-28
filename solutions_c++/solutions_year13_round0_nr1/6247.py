
#include <stdio.h>
#include <set>

using namespace std;
static char modboard[10][17];

struct cmp_str {
    bool operator()(char const *a, char const *b) {
        return strcmp(a, b) < 0;
    }
};


set<char *, cmp_str> xwon_set;
set<char *, cmp_str> owon_set;

void prepare_sets()
{
    // Populate xwon set
    xwon_set.insert("XXXX............");
    xwon_set.insert("TXXX............");
    xwon_set.insert("XTXX............");
    xwon_set.insert("XXTX............");
    xwon_set.insert("XXXT............");
    xwon_set.insert("....XXXX........");
    xwon_set.insert("....TXXX........");
    xwon_set.insert("....XTXX........");
    xwon_set.insert("....XXTX........");
    xwon_set.insert("....XXXT........");
    xwon_set.insert("........XXXX....");
    xwon_set.insert("........TXXX....");
    xwon_set.insert("........XTXX....");
    xwon_set.insert("........XXTX....");
    xwon_set.insert("........XXXT....");
    xwon_set.insert("............XXXX");
    xwon_set.insert("............TXXX");
    xwon_set.insert("............XTXX");
    xwon_set.insert("............XXTX");
    xwon_set.insert("............XXXT");
    xwon_set.insert("X...X...X...X...");
    xwon_set.insert("T...X...X...X...");
    xwon_set.insert("X...T...X...X...");
    xwon_set.insert("X...X...T...X...");
    xwon_set.insert("X...X...X...T...");
    xwon_set.insert(".X...X...X...X..");
    xwon_set.insert(".T...X...X...X..");
    xwon_set.insert(".X...T...X...X..");
    xwon_set.insert(".X...X...T...X..");
    xwon_set.insert(".X...X...X...T..");
    xwon_set.insert("..X...X...X...X.");
    xwon_set.insert("..T...X...X...X.");
    xwon_set.insert("..X...T...X...X.");
    xwon_set.insert("..X...X...T...X.");
    xwon_set.insert("..X...X...X...T.");
    xwon_set.insert("...X...X...X...X");
    xwon_set.insert("...T...X...X...X");
    xwon_set.insert("...X...T...X...X");
    xwon_set.insert("...X...X...T...X");
    xwon_set.insert("...X...X...X...T");
    xwon_set.insert("X....X....X....X");
    xwon_set.insert("T....X....X....X");
    xwon_set.insert("X....T....X....X");
    xwon_set.insert("X....X....T....X");
    xwon_set.insert("X....X....X....T");
    xwon_set.insert("...X..X..X..X...");
    xwon_set.insert("...T..X..X..X...");
    xwon_set.insert("...X..T..X..X...");
    xwon_set.insert("...X..X..T..X...");
    xwon_set.insert("...X..X..X..T...");

    // Populate owon set
    owon_set.insert("OOOO............");
    owon_set.insert("TOOO............");
    owon_set.insert("OTOO............");
    owon_set.insert("OOTO............");
    owon_set.insert("OOOT............");
    owon_set.insert("....OOOO........");
    owon_set.insert("....TOOO........");
    owon_set.insert("....OTOO........");
    owon_set.insert("....OOTO........");
    owon_set.insert("....OOOT........");
    owon_set.insert("........OOOO....");
    owon_set.insert("........TOOO....");
    owon_set.insert("........OTOO....");
    owon_set.insert("........OOTO....");
    owon_set.insert("........OOOT....");
    owon_set.insert("............OOOO");
    owon_set.insert("............TOOO");
    owon_set.insert("............OTOO");
    owon_set.insert("............OOTO");
    owon_set.insert("............OOOT");
    owon_set.insert("O...O...O...O...");
    owon_set.insert("T...O...O...O...");
    owon_set.insert("O...T...O...O...");
    owon_set.insert("O...O...T...O...");
    owon_set.insert("O...O...O...T...");
    owon_set.insert(".O...O...O...O..");
    owon_set.insert(".T...O...O...O..");
    owon_set.insert(".O...T...O...O..");
    owon_set.insert(".O...O...T...O..");
    owon_set.insert(".O...O...O...T..");
    owon_set.insert("..O...O...O...O.");
    owon_set.insert("..T...O...O...O.");
    owon_set.insert("..O...T...O...O.");
    owon_set.insert("..O...O...T...O.");
    owon_set.insert("..O...O...O...T.");
    owon_set.insert("...O...O...O...O");
    owon_set.insert("...T...O...O...O");
    owon_set.insert("...O...T...O...O");
    owon_set.insert("...O...O...T...O");
    owon_set.insert("...O...O...O...T");
    owon_set.insert("O....O....O....O");
    owon_set.insert("T....O....O....O");
    owon_set.insert("O....T....O....O");
    owon_set.insert("O....O....T....O");
    owon_set.insert("O....O....O....T");
    owon_set.insert("...O..O..O..O...");
    owon_set.insert("...T..O..O..O...");
    owon_set.insert("...O..T..O..O...");
    owon_set.insert("...O..O..T..O...");
    owon_set.insert("...O..O..O..T...");
}

void prepare_modboards(char *board)
{
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < 17; ++j) {
            modboard[i][j] = '.';
        }
        modboard[i][16] = '\0';
    }

    modboard[0][0] = board[0];
    modboard[0][1] = board[1];
    modboard[0][2] = board[2];
    modboard[0][3] = board[3];

    modboard[1][4] = board[4];
    modboard[1][5] = board[5];
    modboard[1][6] = board[6];
    modboard[1][7] = board[7];

    modboard[2][8] = board[8];
    modboard[2][9] = board[9];
    modboard[2][10] = board[10];
    modboard[2][11] = board[11];

    modboard[3][12] = board[12];
    modboard[3][13] = board[13];
    modboard[3][14] = board[14];
    modboard[3][15] = board[15];

    modboard[4][0] = board[0];
    modboard[4][4] = board[4];
    modboard[4][8] = board[8];
    modboard[4][12] = board[12];

    modboard[5][1] = board[1];
    modboard[5][5] = board[5];
    modboard[5][9] = board[9];
    modboard[5][13] = board[13];

    modboard[6][2] = board[2];
    modboard[6][6] = board[6];
    modboard[6][10] = board[10];
    modboard[6][14] = board[14];

    modboard[7][3] = board[3];
    modboard[7][7] = board[7];
    modboard[7][11] = board[11];
    modboard[7][15] = board[15];

    modboard[8][0] = board[0];
    modboard[8][5] = board[5];
    modboard[8][10] = board[10];
    modboard[8][15] = board[15];

    modboard[9][3] = board[3];
    modboard[9][6] = board[6];
    modboard[9][9] = board[9];
    modboard[9][12] = board[12];
}

bool check_modboards(bool& xwon, bool& owon)
{
    for (int i = 0; i < 10; ++i) {
        if (xwon_set.find(modboard[i]) != xwon_set.end())
            xwon = true;
        else if (owon_set.find(modboard[i]) != owon_set.end())
            owon = true;

        if (xwon || owon) return true;
    }
    return false;
}

int main(int argc, char **argv)
{
    int num_tests = 0;
    char board[17];
    char row[5];

    prepare_sets();

    scanf("%d", &num_tests);
    board[16] = '\0';

    for (int i = 0; i < num_tests; ++i) {
        int bnow = 0;
        bool xwon = false, owon = false, draw = false, incomplete = false;

        for (int j = 0; j < 4; ++j) {
            scanf("%s", row);
            board[bnow++] = row[0];
            board[bnow++] = row[1];
            board[bnow++] = row[2];
            board[bnow++] = row[3];
        }

        prepare_modboards(board);

        printf("Case #%d: ", i+1);

        if (check_modboards(xwon, owon)) {
            if (xwon)
                printf("X won\n");
            else 
                printf("O won\n");
        }
        else {
            if (strchr(board, '.'))
                printf("Game has not completed\n");
            else
                printf("Draw\n");
        }

        fflush(stdout);
    }

    return 0;
}


