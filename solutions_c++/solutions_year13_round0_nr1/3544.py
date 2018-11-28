#include <stdlib.h>
#include <stdio.h>
#include <cstdlib>
#include <string>
#include <string.h>

using namespace std;

class Game {

    public:
        Game();
        ~Game();
        
        void reset();
        void update(register char* buffer);
        string play();
        
    private:
        void score();
        
        // board related
        char board[4][4];
        char free_cells;
        char scan_line;
        
        // T marker
        char T_x;
        char T_y;
        char T;
        
        // biggest scores after scan
        char score_X;
        char score_O;

        static const string X_won;
        static const string O_won;
        static const string draw;
        static const string ingame;  
};

const string Game::X_won  = "X won";
const string Game::O_won  = "O won";
const string Game::draw   = "Draw";
const string Game::ingame = "Game has not completed";

Game::Game() {}
Game::~Game() {}

void Game::reset() {
    memset(&board, 0, 16*sizeof(char));
    free_cells = 0;
    score_X = 0;
    score_O = 0;
    scan_line = 0;
    T   =  0;
    T_x = -1;
    T_y = -1;
}

void Game::update(register char* buffer) {

    register char x;
    register char c;
    for (x = 0; x < 4; x++) {
        c = buffer[x];
        
        if (c == 'X') {
            board[scan_line][x] = 1;
            continue;
        }
        
        if (c == 'O') {
            board[scan_line][x] = -1;
            continue;
        }
        
        if (c == '.') {
            board[scan_line][x] = 0;
            free_cells++;
            continue;
        }
        
        T   = 1;
        T_x = x;
        T_y = scan_line;
    }
    
    scan_line++;
}

string Game::play() {
    score();
    
    // print scores
    if (score_X ==  4) return X_won;
    if (score_O == -4) return O_won;
    
    if (free_cells > 0) {
        return ingame;
    }
    else {
        return draw;
    }
}

void Game::score() {
    register int x;
    register int y;
    register char score;
    
    // X scoring
    board[T_y][T_x] = 1;
        
        // diag 1
        score = 0;
        score = board[0][0] + board[1][1] + board[2][2] + board[3][3];
        if (score == 4) {
            score_X = 4;
            return;
        }
        
        // diag 2
        score = 0;
        score = board[0][3] + board[1][2] + board[2][1] + board[3][0];
        if (score == 4) {
            score_X = 4;
            return;
        }
    
        // horizontal scan
        for (y = 0; y < 4; y++) {
            score = 0;
            for (x = 0; x < 4; x++) {
                score += board[y][x];
                if (score == 4) {
                    score_X = 4;
                    return;
                }
            }
        }
        // vertical scan
        for (x = 0; x < 4; x++) {
            score = 0;
            for (y = 0; y < 4; y++) {
                score += board[y][x];
                if (score == 4) {
                    score_X = 4;
                    return;
                }
            }
        }
        
    // O scoring
    board[T_y][T_x] = -1;
    
        // diag 1
        score = 0;
        score = board[0][0] + board[1][1] + board[2][2] + board[3][3];
        if (score == -4) {
            score_O = -4;
            return;
        }
        
        // diag 2
        score = 0;
        score = board[0][3] + board[1][2] + board[2][1] + board[3][0];
        if (score == -4) {
            score_O = -4;
            return;
        }
        
        // horizontal scan
        for (y = 0; y < 4; y++) {
            score = 0;
            for (x = 0; x < 4; x++) {
                score += board[y][x];
                if (score == -4) {
                    score_O = -4;
                    return;
                }
            }
        }
        // vertical scan
        for (x = 0; x < 4; x++) {
            score = 0;
            for (y = 0; y < 4; y++) {
                score += board[y][x];
                if (score == -4) {
                    score_O = -4;
                    return;
                }
            }
        }
}

int main(int argc, char** argv) {
 
    int i,j,T;
    
    Game* game = new Game();
    
    register char* buffer = (char *) malloc(5*sizeof(char));
    
    scanf("%d\n", &T);
    for (i = 0; i < T; i++) {
        game->reset();
        for (j = 0; j < 4; j++) {
            scanf("%s\n", buffer);
            game->update(buffer);
        }
        scanf("\n");
        
        printf("Case #%d: %s\n", i+1, game->play().c_str());
    }
    
    free(buffer);
    delete(game);
    
    return 0;
}

