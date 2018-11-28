#include <iostream>
#include <string>
#include <algorithm>

#define SIZE 4

int main() {
    int noc;
    std::string empty;

    std::cin >> noc;
    for(int i = 0; i < noc; i++) {
        std::string row[SIZE];

        std::string rowX[SIZE];
        std::string rowY[SIZE];
        std::string rowXT[SIZE];
        std::string rowYT[SIZE];

        std::string diagX[2];
        std::string diagY[2];
        diagX[0] = "iiii";
        diagX[1] = "iiii";
        diagY[0] = "iiii";
        diagY[1] = "iiii";

        for (int j = 0; j < SIZE; j++) {
            rowX[j] = "iiii";
            rowY[j] = "iiii";
            rowXT[j] = "iiii";
            rowYT[j] = "iiii";

            std::cin >> row[j];
            rowX[j] = row[j];
            std::replace(rowX[j].begin(), rowX[j].end(), 'T', 'X');
            rowY[j] = row[j];
            std::replace(rowY[j].begin(), rowY[j].end(), 'T', 'O');
        }

        for (int k = 0; k < SIZE; k++) {
            for (int j = 0; j < SIZE; j++) {
                rowXT[k][j] = rowX[j][k];
                rowYT[k][j] = rowY[j][k];
            }
            diagX[0][k] = rowX[k][k];
            diagX[1][k] = rowX[k][SIZE - 1 - k];
            diagY[0][k] = rowY[k][k];
            diagY[1][k] = rowY[k][SIZE - 1 - k];
        }

        /*
        // print all for debug
        std::cout << "--X--\n";
        std::cout << rowX[0] << "\n";
        std::cout << rowX[1] << "\n";
        std::cout << rowX[2] << "\n";
        std::cout << rowX[3] << "\n";
        std::cout << "--XT--\n";
        std::cout << rowXT[0] << "\n";
        std::cout << rowXT[1] << "\n";
        std::cout << rowXT[2] << "\n";
        std::cout << rowXT[3] << "\n";

        std::cout << "--Y--\n";
        std::cout << rowY[0] << "\n";
        std::cout << rowY[1] << "\n";
        std::cout << rowY[2] << "\n";
        std::cout << rowY[3] << "\n";
        std::cout << "--YT--\n";
        std::cout << rowYT[0] << "\n";
        std::cout << rowYT[1] << "\n";
        std::cout << rowYT[2] << "\n";
        std::cout << rowYT[3] << "\n";

        std::cout << "--DIAGX--\n";
        std::cout << diagX[0] << "\n";
        std::cout << diagX[1] << "\n";
        std::cout << "--DIAGY--\n";
        std::cout << diagY[0] << "\n";
        std::cout << diagY[1] << "\n";
        */

        bool xwon = false;
        bool ywon = false;
        
        // check if X won
        for (int j = 0; j < SIZE; j++) {
            if (rowX[j] == "XXXX" || rowXT[j] == "XXXX") {
                xwon = true;
                break;
            }
        }
        if (diagX[0] == "XXXX" || diagX[1] == "XXXX") xwon = true;
        if (xwon == true) {
            std::cout << "Case #" << i + 1 << ": X won\n";
            // std::cin >> empty;
            continue;
        }

        // check if Y won
        for (int j = 0; j < SIZE; j++) {
            if (rowY[j] == "OOOO" || rowYT[j] == "OOOO") {
                ywon = true;
                break;
            }
        }
        if (diagY[0] == "OOOO" || diagY[1] == "OOOO") ywon = true;
        if (ywon == true) {
            std::cout << "Case #" << i + 1 << ": O won\n";
            // std::cin >> empty;
            continue;
        }

        bool finished = true;
        for (int j = 0; j < SIZE; j++) {
            if (rowX[j].find('.') != std::string::npos ||
                    rowY[j].find('.') != std::string::npos)
            {
                finished = false;
                break;
            }
        }

        if (finished == false) {
            std::cout << "Case #" << i + 1 << ": Game has not completed\n";
        } else {
            std::cout << "Case #" << i + 1 << ": Draw\n";
        }

        // std::cin >> empty;
    }
}
