/*
Problem

Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board.
The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares.
There are two players: X and O. They take turns to make moves, with X starting.
In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X',
and player O's symbol is 'O'.

After a player's move, if there is a row, column or a diagonal containing 4 of that
player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and
the game ends. Otherwise the game continues with the other player's move. If all of
the fields are filled with symbols and nobody won, the game ends in a draw. See the
sample input for examples of various winning positions.

Given an 4 x 4 board description containing 'X', 'O', 'T' and '.' characters
(where '.' represents an empty square), describing the current state of a game, determine
the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:
    "X won" (the game is over, and X won)
    "O won" (the game is over, and O won)
    "Draw" (the game is over, and it ended in a draw)
    "Game has not completed" (the game is not over yet)

Input

The first line of the input gives the number of test cases, T. T test cases follow.
Each test case consists of 4 lines with 4 characters each, with each character being
'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.

Output

For each test case, output one line containing "Case #x: y", where x is the case number
(starting from 1) and y is one of the statuses given above. Make sure to get the statuses
exactly right. When you run your code on the sample input, it should create the sample
output exactly, including the "Case #1: ", the capital letter "O" rather than the
number "0", and so on.

Limits

The game board provided will represent a valid state that was reached through play of the
game Tic-Tac-Toe-Tomek as described above.

Small dataset

1 ≤ T ≤ 10.
Large dataset

1 ≤ T ≤ 1000. 
*/

#include <iostream>
#include <string>

using namespace std;
 
// Bit-set manipulation helpers
const size_t ONE = size_t(0x1);
const size_t SHIFT = (32 == sizeof(size_t) * 8) ? 5 : 6;
const size_t MASK = (32 == sizeof(size_t) * 8) ? 0x1f : 0x3f;
const size_t BITS_PER_WORD = sizeof(size_t) << 3;
#define SET_BIT(a, i) (a[i >> SHIFT] |= (ONE << (i & MASK)))
#define GET_BIT(a, i) (a[i >> SHIFT] & (ONE << (i & MASK)))

// Global variables
#define NUM_MASKS 10
#define MAX_T 1001
size_t masks[NUM_MASKS][1];
int incomplete_games[MAX_T];

// Function prototypes
size_t CountSetBits(size_t a);
bool IsVictorious(size_t board);
void PopulateMasks(void);


int main(void)
{
    int T;
    cin >> T;  // Number of testcases
    int N = T; // To print tescase number in the output

    PopulateMasks();
    for (int i = 0; i < MAX_T; ++i)
        incomplete_games[i] = 0; // Initially assume that all games are complete; uncheck when "." (dot) is found on the board
    while (T--) {
        size_t i = 0, x_pos[1], y_pos[1];
        x_pos[0] = 0;
        y_pos[0] = 0;
        do {
            string row;
            cin >> row;
            ++i;
            for (int j = 0; j < 4; ++j) { // Scan columns
                size_t bit = 4 * (i - 1) + j;
                if ('X' == row[j])
                    SET_BIT(x_pos, bit);
                else if ('O' == row[j])
                    SET_BIT(y_pos, bit);
                else if ('T' == row[j]) {
                    SET_BIT(x_pos, bit);
                    SET_BIT(y_pos, bit);
                } else if ('.' == row[j])
                    incomplete_games[N-T] = 1;
            }
        } while (i % 4);
        bool x_won = IsVictorious(x_pos[0]);
        bool y_won = IsVictorious(y_pos[0]);

        cout << "Case #" << (N - T) << ": ";
        if (x_won && y_won) cout << "Draw" << endl;
        else if (x_won) cout << "X won" << endl;
        else if (y_won) cout << "O won" << endl;
        else if (incomplete_games[N-T]) cout << "Game has not completed" << endl;
        else cout << "Draw" << endl;
    }
    return 0;
}

void PopulateMasks(void)
{
    for (int i = 0; i < NUM_MASKS; ++i)
        masks[i][0] = 0;

    SET_BIT(masks[0], 0); SET_BIT(masks[0], 1); SET_BIT(masks[0], 2); SET_BIT(masks[0], 3);
    SET_BIT(masks[1], 4); SET_BIT(masks[1], 5); SET_BIT(masks[1], 6); SET_BIT(masks[1], 7);
    SET_BIT(masks[2], 8); SET_BIT(masks[2], 9); SET_BIT(masks[2], 10); SET_BIT(masks[2], 11);
    SET_BIT(masks[3], 12); SET_BIT(masks[3], 13); SET_BIT(masks[3], 14); SET_BIT(masks[3], 15);
    SET_BIT(masks[4], 0); SET_BIT(masks[4], 4); SET_BIT(masks[4], 8); SET_BIT(masks[4], 12);
    SET_BIT(masks[5], 1); SET_BIT(masks[5], 5); SET_BIT(masks[5], 9); SET_BIT(masks[5], 13);
    SET_BIT(masks[6], 2); SET_BIT(masks[6], 6); SET_BIT(masks[6], 10); SET_BIT(masks[6], 14);
    SET_BIT(masks[7], 3); SET_BIT(masks[7], 7); SET_BIT(masks[7], 11); SET_BIT(masks[7], 15);
    SET_BIT(masks[8], 0); SET_BIT(masks[8], 5); SET_BIT(masks[8], 10); SET_BIT(masks[8], 15);
    SET_BIT(masks[9], 3); SET_BIT(masks[9], 6); SET_BIT(masks[9], 9); SET_BIT(masks[9], 12);
    return;
}


size_t CountSetBits(size_t a)
{
    size_t ones = 0;
    if (32 == BITS_PER_WORD) {
        size_t tmp = a - ((a >> 1) & 033333333333) - ((a >> 2) & 011111111111);
        ones = ((tmp + (tmp >> 3)) & 030707070707) % 63;
    } else if (64 == BITS_PER_WORD) { // Here we make groups of 4 bits and also use
                                      // hexadecimal representation instead of octal
        size_t tmp = a - ((a >> 1) & 0x7777777777777777) - ((a >> 2) & 0x3333333333333333) - ((a >> 3) & 0x1111111111111111);
        ones = ((tmp + (tmp >> 4)) & 0x0f0f0f0f0f0f0f0f) % 255;
    }
    return ones;
}

bool IsVictorious(size_t board)
{
    // Apply masks to the board
    for (int i = 0; i < 10; ++i)
        if (4 == CountSetBits(board & masks[i][0]))
            return true;
    return false;
}

