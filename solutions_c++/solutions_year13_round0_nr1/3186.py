
#include <iostream>

int main () {

    size_t num_cases = 0;

    std::cin >> num_cases;

    for (size_t i = 0; i < num_cases; ++i) {
   
        char cells[4][4] = { '.' };
        bool unplayed = false;

        for (size_t row = 0; row < 4; ++row) {
        
            for (size_t col = 0; col < 4; ++col) {
            
                std::cin >> cells[row][col]; 

                if (cells[row][col] == '.') unplayed = true;
            }
        }

        size_t sums[10] = { 0 };
        
        //rows
        sums[0] = cells[0][0] + cells[0][1] + cells[0][2] + cells[0][3];
        sums[1] = cells[1][0] + cells[1][1] + cells[1][2] + cells[1][3];
        sums[2] = cells[2][0] + cells[2][1] + cells[2][2] + cells[2][3];
        sums[3] = cells[3][0] + cells[3][1] + cells[3][2] + cells[3][3];

        //cols
        sums[4] = cells[0][0] + cells[1][0] + cells[2][0] + cells[3][0];
        sums[5] = cells[0][1] + cells[1][1] + cells[2][1] + cells[3][1];
        sums[6] = cells[0][2] + cells[1][2] + cells[2][2] + cells[3][2];
        sums[7] = cells[0][3] + cells[1][3] + cells[2][3] + cells[3][3];

        //diags

        sums[8] = cells[0][0] + cells[1][1] + cells[2][2] + cells[3][3];
        sums[9] = cells[0][3] + cells[1][2] + cells[2][1] + cells[3][0];

        char winner = ' ';

        for (size_t j=0; j < 10; ++j) {

            if (sums[j] == 'X'+'X'+'X'+'X' ||
                    sums[j] == 'X'+'X'+'X'+'T' ) {
            
                winner = 'X';
                break;
            } else if (sums[j] == 'O'+'O'+'O'+'O' ||
                    sums[j] == 'O'+'O'+'O'+'T') {
            
                winner = 'O';
                break;
            }
        }

        std::cout << "Case #" << i+1 << ": ";

        if (winner != ' ' ) {
            std::cout << winner << " won" << std::endl;
        } else if (unplayed) {
            std::cout << "Game has not completed" << std::endl;
        } else {
            std::cout << "Draw" << std::endl; 
        }
    }

    return 0;
}
