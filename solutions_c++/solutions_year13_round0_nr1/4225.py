#include <iostream>
#include <vector>

int main() {

        int size;
        std::cin >> size;

#ifndef NDEBUG
        std::cerr << size << " boards" << std::endl;
#endif

        for (int i = 1; i <= size; ++i) {

#ifndef NDEBUG
                std::cerr << std::endl << "Board " << i << std::endl;
#endif

                // Read input board

                std::string board;

#ifndef NDEBUG
                std::cerr << "Board:" << std::endl;
#endif

                for (int j = 0; j < 4; ++j) {
                        std::string line;
                        std::cin >> line;
                        board += line;
#ifndef NDEBUG
                        std::cerr << line << std::endl;
#endif
                }

                // Extract rows, columns, and diagonals

                std::vector<std::string> lines;

                {
                        std::string diagonal1, diagonal2;
                        for (int j = 0; j < 4; ++j) {
                                std::string row, column;
                                for (int k = 0; k < 4; ++k) {
                                        row += board[j * 4 + k];
                                        column += board[j + k * 4];
                                }
                                lines.push_back(row);
                                lines.push_back(column);
                                diagonal1 += board[j * 4 + j];
                                diagonal2 += board[j * 4 + (4 - (j + 1))];
                        }
                        lines.push_back(diagonal1);
                        lines.push_back(diagonal2);
                }

                // Look for win/lose conditions

#ifndef NDEBUG
                std::cerr << "Board lines:" << std::endl;
#endif

                bool XWon = false, OWon = false, gameCompleted = true;

                for (const auto& line: lines) {

                        bool noX = true, noO = true, noDot = true;

                        for (const auto& symbol: line) {
                                noX = noX and symbol != 'X';
                                noO = noO and symbol != 'O';
                                noDot = noDot and symbol != '.';
                        }

                        XWon = XWon or (noDot and noO);
                        OWon = OWon or (noDot and noX);
                        gameCompleted = gameCompleted and noDot;

#ifndef NDEBUG
                        std::cerr << line << " XWon=" << XWon << " OWon=" << OWon << std::endl;
#endif

                }

                // Output game state

                std::cout << "Case #" << i << ": " << (XWon ? "X won" : OWon ? "O won" : gameCompleted ? "Draw" : "Game has not completed") << std::endl;

        }

}
