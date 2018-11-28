#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::cout;
using std::cin;
using std::string;

vector<size_t> ReadGame() {
    vector<size_t> game(21);
    for (size_t row = 0; row < 4; ++row) {
        for (size_t col = 0; col < 4; ++col) {
            char letter;
            cin >> letter;
            if (letter == '.') {
                ++game[20] ;   
            }
            if (letter == 'X' || letter == 'T') {
                if (row == col) {
                    ++game[8];    
                }    
                if (row + col == 3) {
                    ++game[9];    
                }
                ++game[row];
                ++game[col + 4];          
            }        
            if (letter == 'O' || letter == 'T') {
                if (row == col) {
                    ++game[8 + 10];    
                }    
                if (row + col == 3) {
                    ++game[9 + 10];    
                }
                ++game[row + 10];
                ++game[col + 4 + 10];          
            }  
            
        }    
    }
    return game;
}

string GameResult(const vector<size_t>& game) {
    for (size_t i = 0; i < 10; ++i) {
        if (game[i] == 4) {
            return "X won";   
        }
    }
    for (size_t i = 10; i < 20; ++i) {
        if (game[i] == 4) {
            return "O won";   
        }
    }
    if (game[20] == 0) {
        return "Draw";   
    } else {
        return "Game has not completed";    
    }
}

template<typename T>
void PrintVector(const vector<T>& printing_vector){
    for (typename vector<T>::const_iterator element = printing_vector.begin();
         element != printing_vector.end();
         ++element) {
                
        cout << *element << " ";           
    }    
    cout <<std::endl;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    size_t game_number;
    cin >> game_number;
    for (size_t i = 0; i < game_number; ++i) {
        vector<size_t> game = ReadGame();
        //PrintVector(game);
        cout << "Case #" << i + 1 <<": " << GameResult(game) << std::endl;    
    }
    return 0;    
}
