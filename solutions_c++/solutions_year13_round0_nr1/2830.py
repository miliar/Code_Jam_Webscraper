#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::string board_status(std::vector<short> const &board) {

    int diag1_sum = board[0] + board[5] + board[10] + board[15];
    int diag2_sum = board[3] + board[6] + board[9] + board[12];

    if (diag1_sum == 4 || diag2_sum == 4 || diag1_sum == 33 || diag2_sum == 33)
        return "X won";
    if (diag1_sum == -4 || diag2_sum == -4 || diag1_sum == 27 || diag2_sum == 27)
        return "O won";

    for (size_t ofs = 0; ofs < 4; ++ofs) {
        int row_sum = board[ofs * 4] + board[ofs * 4 + 1] + board[ofs * 4 + 2] + board[ofs * 4 + 3];
        int col_sum = board[ofs] + board[ofs + 4] + board[ofs + 8] + board[ofs + 12];
        if (row_sum == 4 || col_sum == 4 || row_sum == 33 || col_sum == 33)
            return "X won";
        if (row_sum == -4 || col_sum == -4 || row_sum == 27 || col_sum == 27)
            return "O won";
    }

    return std::find(board.begin(), board.end(), 0) == board.end() ? "Draw" : "Game has not completed";
}


int main() {

    size_t ncases;
    std::cin >> ncases;

    for (size_t game = 0; game < ncases; ++game) {
        std::vector<short> board;
        board.reserve(16);
        for (size_t idx = 0; idx < 16; ++idx) {
            char c;
            std::cin >> c;
            switch (c) {
                case 'X':
                    board.push_back(1);
                    break;
                case 'O':
                    board.push_back(-1);
                    break;
                case '.':
                    board.push_back(0);
                    break;
                case 'T':
                    board.push_back(30);
                    break;
                default:
                    --idx;
            }
        }
        std::cout << "Case #" << game + 1 << ": " << board_status(board) << '\n';
    }
}