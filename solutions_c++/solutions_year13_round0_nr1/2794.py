#include <iostream>
#include <cstdio>
using namespace std;

#define _X (0x1)
#define _O (0x2)
#define _T (_X|_O)

#define STEP 2

#define X_WON ( (_X << (STEP * 0)) | \
                (_X << (STEP * 1)) | \
                (_X << (STEP * 2)) | \
                (_X << (STEP * 3)) )

#define O_WON ( (_O << (STEP * 0)) | \
                (_O << (STEP * 1)) | \
                (_O << (STEP * 2)) | \
                (_O << (STEP * 3)) )

#define GET_DIAG_L(x) ((uint8_t)(((x)[0]&(0xC0))|((x)[1]&(0x30))|((x)[2]&(0x0C))|((x)[3]&(0x03))))
#define GET_DIAG_R(x) ((uint8_t)(((x)[0]&(0x03))|((x)[1]&(0x0C))|((x)[2]&(0x30))|((x)[3]&(0xC0))))

void work(int no) {
    uint8_t board[4] = {0};
    uint8_t board_rotated[4] = {0};
    int cnt = 0;
    int dots = 0;
    bool X_won = false;
    bool O_won = false;
    while (cnt < 16) {
        switch (getchar()) {
            case 'X':
                board[cnt / 4] |= (uint8_t) _X << ((cnt % 4) * STEP);
                board_rotated[cnt % 4] |= (uint8_t) _X << ((cnt / 4) * STEP);
                cnt++;
                break;
            case 'O':
                board[cnt / 4] |= (uint8_t) _O << ((cnt % 4) * STEP);
                board_rotated[cnt % 4] |= (uint8_t) _O << ((cnt / 4) * STEP);
                cnt++;
                break;
            case 'T':
                board[cnt / 4] |= (uint8_t) _T << ((cnt % 4) * 2);
                board_rotated[cnt % 4] |= (uint8_t) _T << ((cnt / 4) * STEP);
                cnt++;
                break;
            case '.':
                cnt++;
                dots++;
                break;
            default:
                break;
        }
    }
    for (int i = 0; i < 4; i++) {
        if ((board[i] & X_WON) == X_WON || (board_rotated[i] & X_WON) == X_WON) {
            X_won = true;
        }
        if ((board[i] & O_WON) == O_WON || (board_rotated[i] & O_WON) == O_WON) {
            O_won = true;
        }
    }
    if (!X_won && (GET_DIAG_L(board) & X_WON) == X_WON || (GET_DIAG_R(board) & X_WON) == X_WON)
        X_won = true;
    if (!O_won && (GET_DIAG_L(board) & O_WON) == O_WON || (GET_DIAG_R(board) & O_WON) == O_WON)
        O_won = true;
    cout << "Case #" << no << ": ";
    if ((X_won && O_won) || (!dots && !X_won && !O_won)) {
        cout << "Draw";
    }
    else if (X_won) {
        cout << "X won";
    }
    else if (O_won) {
        cout << "O won";
    }
    else {
        cout << "Game has not completed";
    }
    cout << endl;
}

int main(void) {
    int n_cases = 0;
    cin >> n_cases;
    for (int i = 1; i <= n_cases; i++) {
        work(i);
    }
    return 0;
}