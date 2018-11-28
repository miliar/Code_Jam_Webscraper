#include <iostream>
#include <fstream>
#include <string>

typedef struct Board {
    char elements[4][4];
} Board;

typedef struct State {
    int dimension;
    int x_pieces;
    int o_pieces;
    State() {
        dimension = 4;
        x_pieces = 0;
        o_pieces = 0;
    }
} State;

typedef struct GameResult {
    bool x_won;
    bool o_won;
    bool draw;
    bool game_over;
    bool empty_cell_found;
    GameResult() {
        x_won = false;
        o_won = false;
        draw = false;
        game_over = false;
        empty_cell_found = false;
    }
    GameResult operator||(GameResult right) {
        if (this->game_over) {
            return *this;
        } else if (right.game_over) {
            return right;
        } else {
            return GameResult();
        }
    }
} GameResult;

using namespace std;


char board_element(Board& board, int row, int col) {
    return board.elements[row][col];
}


GameResult is_game_over(State& s) {
    GameResult result;
    if (s.x_pieces == s.dimension) {
        result.x_won = true;
        result.game_over = true;
    }
    else if (s.o_pieces == s.dimension) {
        result.o_won = true;
        result.game_over = true;
    }
    return result;
}

bool check_for_empty_cell(Board& board, int i, int j) {
    char piece = board_element(board, i, j);
    if (piece == '.') {
        return true;
    }
    return false;
}

void update_state(State& s, Board& board, int i, int j) {
    char piece = board_element(board, i, j);
    if (piece == 'T') {
        s.x_pieces++; s.o_pieces++;
    }
    else if (piece == 'X') {
        s.x_pieces++;
    }
    else if (piece == 'O') {
        s.o_pieces++;
    }
}

void clear_state(State& s) {
    s.x_pieces = 0; s.o_pieces = 0;
}

void output_answer(GameResult& result, fstream& output_file) {
    if (result.x_won) {
        output_file << "X won";
    }
    if (result.o_won) {
        output_file << "O won";
    }
    if (result.draw) {
        output_file << "Draw";
    }
    if (!result.game_over) {
        output_file << "Game has not completed";
    }
}

void solve_board_configuration(Board& board, fstream& output_file) {
    State row_state, column_state;
    GameResult result;
    bool empty_cell_found = false;
    // Check rows and columns
    for (int i = 0; i < row_state.dimension; i++) {
        for (int j = 0; j < row_state.dimension; j++) {
            update_state(row_state, board, i, j); // row
            update_state(column_state, board, j, i); // column
            // We need to see if all cells are occupied for draw/game not complete
            empty_cell_found = empty_cell_found || check_for_empty_cell(board, i, j);
        }
        result = is_game_over(row_state) || is_game_over(column_state);
        if (result.game_over) {
            output_answer(result, output_file);
            return;
        }
        clear_state(row_state); clear_state(column_state);
    }

    State d1, d2;
    // Check diagonals
    for (int i = 0; i < d1.dimension; i++) {
        update_state(d1, board, i, i); // left diagonal
        int right_diagonal_index = d1.dimension - i - 1;
        update_state(d2, board, i, right_diagonal_index); // right diagonal
    }
    result = is_game_over(d1) || is_game_over(d2);
    // Final check if it's a draw, otherwise default case is game not finished
    if (!result.game_over && !empty_cell_found) {
        result.draw = true;
        result.game_over = true;
    }
    output_answer(result, output_file);
}

int main()
{
    fstream input_file;
    fstream output_file;
    input_file.open("tic_tac_toe.in", ios::in);
    output_file.open("tic_tac_toe.out", ios::out | ios::trunc);
    if (input_file.is_open() && output_file.is_open()) {
        int test_cases;
        input_file >> test_cases;
        input_file.get(); // Skip newline

        string line_of_input;
        for (int i = 1; i <= test_cases; i++) {
            Board board;
            for (int row = 0; row < 4; row++) {
                getline(input_file, line_of_input);
                for (int col = 0; col < 4; col++) {
                    board.elements[row][col] = line_of_input[col];
                }
            }
            output_file << "Case #" << i << ": ";
            solve_board_configuration(board, output_file);
            if (i < test_cases) {
                output_file << "\n";
            }
            getline(input_file, line_of_input); // Skip newline
        }
        input_file.close();
        output_file.close();
    } else {
        cout << "Error opening file.";
    }
    return 0;
}

